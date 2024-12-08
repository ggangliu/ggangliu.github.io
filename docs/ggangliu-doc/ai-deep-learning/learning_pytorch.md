# Learning Pytorch with Example

## Python on RISC-V

<https://riscv.readthedocs.io/en/latest/>
<https://github.com/litex-hub/micropython/tree/litex-rebase/ports/litex>
<https://github.com/r4d10n/micropython-wch-ch32v307/tree/master/ports/wch>

## Pytorch support OpenCL by PyOpenCL

``` python
import pyopencl as cl

import torch

def add(x, y):
    return x + y

# 创建 OpenCL 上下文
ctx = cl.create_context()

# 创建 OpenCL 设备
device = ctx.get_devices()[0]

# 创建 OpenCL 内核
kernel = cl.Program(ctx, """
__kernel void add(__global float *x, __global float *y, __global float *z) {
    int gid = get_global_id(0);
    z[gid] = x[gid] + y[gid];
}
""").build()

# 创建 OpenCL 缓冲区
x_buf = cl.Buffer(ctx, cl.mem_flags.READ_ONLY | cl.mem_flags.HOST_NO_ACCESS, x.nbytes)
y_buf = cl.Buffer(ctx, cl.mem_flags.READ_ONLY | cl.mem_flags.HOST_NO_ACCESS, y.nbytes)
z_buf = cl.Buffer(ctx, cl.mem_flags.WRITE_ONLY, z.nbytes)

# 将 PyTorch Tensor 数据复制到 OpenCL 缓冲区
cl.enqueue_copy(ctx, x_buf, x.cpu().numpy())
cl.enqueue_copy(ctx, y_buf, y.cpu().numpy())

# 执行 OpenCL 内核
kernel.set_arg(0, x_buf)
kernel.set_arg(1, y_buf)
kernel.set_arg(2, z_buf)
cl.enqueue_kernel(ctx, kernel, (x.shape[0],), None)

# 从 OpenCL 缓冲区中读取数据到 PyTorch Tensor
z = torch.from_numpy(cl.enqueue_read_buffer(ctx, z_buf))

return z

x = torch.randn(10)
y = torch.randn(10)

z = add(x, y)

print(z)
```

## CFU