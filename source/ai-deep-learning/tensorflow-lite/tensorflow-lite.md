# Tensorflow-Lite

Running on RISC-V based on CFU

端到端工作流包括以下步骤：

1. 训练模型（用 Python 编写）：Jupyter 笔记本，用于训练、转换和优化模型供设备端使用。
2. 运行推断（用 C++ 11 编写）：端到端单元测试，使用 C++ 库在模型上运行推断。

## 训练模型

https://github.com/tensorflow/tflite-micro/tree/main/tensorflow/lite/micro/examples/hello_world

## 运行推断

https://github.com/tensorflow/tflite-micro/tree/main/tensorflow/lite/micro/examples/hello_world

示例的 hello_world_test.cc演示如何使用 TensorFlow Lite for Microcontrollers 运行推断。

1. 包括库头文件
2. 包含模型头文件
   TensorFlow Lite for Microcontrollers 解释器希望以 C++ 数组的形式提供模型。模型在 model.h 和 model.cc 文件中进行定义
3. 包含单元测试框架头文件
4. 设置日志记录
5. 加载模型
6. 实例化运算解析器
   AllOpsResolver 会加载 TensorFlow Lite for Microcontrollers 中可用的所有运算，而这些运算会占用大量内存。由于给定的模型仅会用到这些运算中的一部分，因此建议在实际应用中仅加载所需的运算。这是使用另一个类 MicroMutableOpResolver 来实现的。
7. 分配内存
8. 实例化解释器
9. 分配张量
10. 验证输入形状
    MicroInterpreter 实例可以通过调用 .input(0) 为我们提供指向模型输入张量的指针，其中 0 代表第一个（也是唯一的）输入张量：

    ``` c++
      // Obtain a pointer to the model's input tensor
      TfLiteTensor* input = interpreter.input(0);
    ```

11. 提供输入值
    为了给模型提供输入，我们设置输入张量的内容，如下所示：

    ``` c++
      input->data.f[0] = 0.;
    ```

12. 运行模型
    要运行模型，我们可以在 tflite::MicroInterpreter 实例上调用 Invoke()：

    ``` c++
      TfLiteStatus invoke_status = interpreter.Invoke();
      if (invoke_status != kTfLiteOk) {
        TF_LITE_REPORT_ERROR(error_reporter, "Invoke failed\n");
      }
    ```

13. 获得输出
    可以通过在 tflite::MicroInterpreter 上调用 output(0) 来获得模型的输出张量，其中 0 表示第一个（也是唯一的）输出张量。

## TensorFlow Lite for Microcontrollers C++ 库

TensorFlow Lite for Microcontrollers 能够使用 Makefile 生成包含所有必要源文件的独立项目。

``` c++
make -f tflite-micro/tensorflow/lite/micro/tools/make/Makefile generate_projects
make -f tensorflow/lite/micro/tools/make/Makefile test
make -f tensorflow/lite/micro/tools/make/Makefile test_<test_name>
```

构建二进制文件

``` c++
make -f tensorflow/lite/micro/tools/make/Makefile hello_world_bin
make -f tensorflow/lite/micro/tools/make/Makefile TARGET=sparkfun_edge hello_world_bin
```

## Porting to a new platform

<https://github.com/tensorflow/tflite-micro/blob/main/tensorflow/lite/micro/docs/new_platform_support.md>

## Reference

- <https://www.tensorflow.org/lite/microcontrollers/get_started_low_level?hl=zh-cn>
- <https://github.com/tensorflow/tflite-micro/tree/main/tensorflow/lite/micro/examples/hello_world>