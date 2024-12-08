# How to add a new backend for pytorch

first-riscv-pytorh = FRP
icube

- [How to add a new backend for pytorch](#how-to-add-a-new-backend-for-pytorch)
  - [为新后端注册内核](#为新后端注册内核)
  - [为新后端注册生成器](#为新后端注册生成器)
  - [为新后端注册设备防护](#为新后端注册设备防护)
  - [为新后端元数据注册序列化和反序列化函数](#为新后端元数据注册序列化和反序列化函数)
  - [其他模块](#其他模块)
  - [提升用户的易用性](#提升用户的易用性)
    - [向PyTorch注册新的后端模块](#向pytorch注册新的后端模块)
    - [将 PrivateUse1 重命名为新后端的自定义名称](#将-privateuse1-重命名为新后端的自定义名称)
    - [生成与新后端相关的方法和属性](#生成与新后端相关的方法和属性)
    - [构建扩展](#构建扩展)
  - [Defining schema and backend implementations](#defining-schema-and-backend-implementations)
  - [Reference](#reference)

## 为新后端注册内核

1. 将新后端支持的所有前向算子注册到调度程序，同时注册回退 ，这样当新后端不支持某些算子时，这些算子可以回落到CPU执行确保功能的可用性

``` c++
at::Tensor wrapper_Custom_Tensor_add(const at::Tensor & self, const at::Tensor & other, const at::Scalar & alpha) {
    // Implementation of add kernel in new backend
    ...
}

TORCH_LIBRARY_IMPL(aten, PrivateUse1, m) {
    ...
    m.impl("add.Tensor", TORCH_FN(wrapper_Custom_Tensor_add));
    ...
}

void custom_cpu_fallback(const c10::OperatorHandle& op, torch::jit::Stack* stack) {
    // Add some hints about new devices that do not support and need to fall back to cpu
    at::native::cpu_fallback(op, stack);
}

TORCH_LIBRARY_IMPL(_, PrivateUse1, m) {
    m.fallback(torch::CppFunction::makeFromBoxedFunction<&custom_cpu_fallback>());
}
```

2. 如果新后端需要覆盖PyTorch Autograd Layer，则通过 AutogradPrivateUse1 将 torch::autograd::Function 的内核注册到调度程序，调度程序和自动求导系统将自动调用这些算子的前向和后向实现

``` c++
class MyAddFunction : public torch::autograd::Function<MyAddFunction> {
 public:
 static Tensor forward(AutogradContext *ctx, torch::Tensor self, torch::Tensor other) {
    at::AutoNonVariableTypeMode g;
    return myadd(self, other);
 }

 static tensor_list backward(AutogradContext *ctx, tensor_list grad_outputs) {
    auto grad_output = grad_outputs[0];
    return {grad_output, grad_output};
 }
};

Tensor myadd_autograd(const Tensor& self, const Tensor& other) {
    return MyAddFunction::apply(self, other)[0];
}

// Register the autograd kernel to AutogradPrivateUse1
TORCH_LIBRARY_IMPL(aten, AutogradPrivateUse1, m) {
    m.impl(<myadd_schema>, &myadd_autograd);
}

// Register the inference kernel to PrivateUse1
TORCH_LIBRARY_IMPL(aten, PrivateUse1, m) {
    m.impl(<myadd_schema>, &myadd);
}
```

3. 通过 AutocastPrivateUse1 将想要支持自动混合精度（AMP）和回退机制的内核注册到调度程序，当需要时，自动转换系统将自动调用这些内核

``` c++
TORCH_LIBRARY_IMPL(aten, AutocastPrivateUse1, m) {
    ...
    KERNEL_PRIVATEUSEONE(<operator>, <policy>)
    ...
}

TORCH_LIBRARY_IMPL(_, AutocastPrivateUse1, m) {
    m.fallback(torch::CppFunction::makeFallthrough());
}
```

需要补充的是，如果要在新后端支持 AMP，需要通过torch._register_device_module("backend_name", BackendModule)注册一个新的BackendModule，并且BackendModule需要具有以下 API：

- `get_amp_supported_dtype() -> List[torch.dtype]` 在 AMP 中获取新后端支持的dtype，可能支持一个以上的dtype
- `is_autocast_enabled() -> bool` 检查新后端是否启用 AMP
- `get_autocast_dtype() -> torch.dtype` 在 AMP 中获取新后端支持的dtype，该dtype由set_autocast_dtype或默认dtype设置，而默认dtype为torch.float16
- `set_autocast_enabled(bool) -> None` 在新后端上启用或禁用 AMP
- `set_autocast_dtype(dtype) -> None` 在 AMP 中设置新后端支持的dtype，并且dtype包含在从get_amp_supported_dtype获取的dtypes中

## 为新后端注册生成器

需要支持与新设备对应的生成器

``` c++
struct CustomGeneratorImpl : public c10::GeneratorImpl {
    // Implementation of generator in new backend
}

at::Generator make_custom_generator(c10::DeviceIndex device_index) {
    return at::make_generator<CustomGeneratorImpl>(device_index);
}

REGISTER_GENERATOR_PRIVATEUSE1(make_cumstom_generator)
```

## 为新后端注册设备防护

``` c++
struct CustomGuardImpl final : public c10::impl::DeviceGuardImplInterface {
    // Implementation of guard in new backend
}

C10_REGISTER_GUARD_IMPL(PrivateUse1, CustomGuardImpl);
```

## 为新后端元数据注册序列化和反序列化函数

PyTorch 目前能够动态注册序列化/反序列化函数，以支持在TensorImpl.ExtraMeta类中命名为backend_meta_的新后端附加元数据的序列化和反序列化。

``` c++
struct CustomBackendMetadata : public c10::BackendMeta {
    // Implementation of backend metadata in new backend
}

void for_serialization(const at::Tensor& t, std::unordered_map<std::string, bool>& m) {
    // Implementation of serialization
}

void for_deserialization(const at::Tensor& t, std::unordered_map<std::string, bool>& m) {
    // Implementation of deserialization
}

TensorBackendMetaRegistry(c10::DeviceType::PrivateUse1, &for_serialization, &for_deserialization);    
```

## 其他模块

## 提升用户的易用性

### 向PyTorch注册新的后端模块

PyTorch 中一些 CUDA 相关的接口可以通过以下形式调用： `torch.cuda.xxx` 。因此，为了符合用户习惯，通过PrivateUse1机制实现的新后端也应该提供类似的接口。例如，Ascend NPU:

``` c++
torch._register_device_module('npu', torch_npu.npu)
```

完成上述操作后，用户可以通过 `torch.npu.xxx`

### 将 PrivateUse1 重命名为新后端的自定义名称

PrivateUse1 Key 是集成到 PyTorch 中的新后端的内部机制。对于用户来说，与 PrivateUse1 相比，使用新后端强相关的自定义名称应该更加友好。

以 `Ascend NPU` 为例，第一个使用会更方便。

``` c++
torch.rand((2,2),device='npu:0')
torch.rand((2,2),device='privateuse1:0')
```

PyTorch 为自命名的 PrivateUse1 后端提供了一个新的 C++/Python API，使用起来非常简单。

Python

``` python
torch.rename_privateuse1_backend("npu")
```

C++

``` c++
c10::register_privateuse1_backend("npu")
```

### 生成与新后端相关的方法和属性

将 PrivateUse1 重命名为自定义名称后，在新后端的 Tensor, nn, Storage 模块中自动生成与新后端名称相关的属性和方法。

``` python
torch.rename_privateuse1_backend("npu")
unsupported_dtype = [torch.quint8]
torch.utils.generate_methods_for_privateuse1_backend(for_tensor=True, for_module=True, for_storage=True, unsupported_dtype=unsupported_dtype) 

torch.Tensor.npu()
torch.Tensor.is_npu
torch.Storage.npu()
torch.Storage.is_npu
```

### 构建扩展

通过向 PyTorch 添加 C++ 扩展来支持树外后端。 一旦准备好内核和注册，您就可以通过编写一个 setup.py 脚本来构建 C++ 扩展，该脚本使用 setuptools 编译 C++ 代码。

``` python
from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CppExtension

setup(
    name='torch_xla',
    version= VERSION,
    ext_modules=[
        CppExtension(
            '_XLAC',
            torch_xla_sources,
            include_dirs=include_dirs,
            extra_compile_args=extra_compile_args,
            library_dirs=library_dirs,
            extra_link_args=extra_link_args + \
                [make_relative_rpath('torch_xla/lib')],
        ),
    ],
    cmdclass={
        'build_ext': Build,  # Build is a derived class of BuildExtension
    }
    # more configs...
)
```

## Defining schema and backend implementations

``` python
TORCH_LIBRARY(myops, m) {
  m.def("myadd(Tensor self, Tensor other) -> Tensor");
}

Tensor myadd_cpu(const Tensor& self_, const Tensor& other_) {
  TORCH_CHECK(self_.sizes() == other_.sizes());
  TORCH_INTERNAL_ASSERT(self_.device().type() == DeviceType::CPU);
  TORCH_INTERNAL_ASSERT(other_.device().type() == DeviceType::CPU);
  Tensor self = self_.contiguous();
  Tensor other = other_.contiguous();
  Tensor result = torch::empty(self.sizes(), self.options());
  const float* self_ptr = self.data_ptr<float>();
  const float* other_ptr = other.data_ptr<float>();
  float* result_ptr = result.data_ptr<float>();
  for (int64_t i = 0; i < result.numel(); i++) {
    result_ptr[i] = self_ptr[i] + other_ptr[i];
  }
  return result;
}

TORCH_LIBRARY_IMPL(myops, CPU, m) {
  m.impl("myadd", myadd_cpu);
}
```

## Reference

- <https://pytorch.org/tutorials/advanced/extend_dispatcher.html>
- <https://github.com/ascend/pytorch>
- <https://www.cnblogs.com/apachecn/p/18006835>
- <http://blog.ezyang.com/2020/09/lets-talk-about-the-pytorch-dispatcher/>
- <https://pytorch.org/tutorials/advanced/torch_script_custom_ops.html>
- <https://github.com/sandeepkumar-skb/pytorch_custom_op>
