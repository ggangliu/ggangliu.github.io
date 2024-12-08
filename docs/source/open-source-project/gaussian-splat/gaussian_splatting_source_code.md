# Gaussian Splatting 源码学习理解

## 代码结构


### Forward

- 计算每个高斯球的属性（guassian球的每个参数的梯度）
  - 初始化每个高斯球的属性<https://github.com/graphdeco-inria/gaussian-splatting/blob/main/scene/gaussian_model.py#L47-L52>
  - 给每个高斯球的属性赋值<https://github.com/graphdeco-inria/gaussian-splatting/blob/main/scene/gaussian_model.py#L220>
  - 将3D高斯球投影到2D空间
    - 基于Scaling和rotation计算3D covariance
  - 高斯球投影到2D空间上的2D属性radius, uv and cov
    - cov <https://github.com/graphdeco-inria/diff-gaussian-rasterization/blob/main/cuda_rasterizer/forward.cu#L99-L106>
    - radius of a gaussian
    - uv (image coordinates) of the gaussian
  - 计算每个Guassian覆盖的tiles

- 计算每个像素的颜色

### Backward

- 将loss根据梯度分配并更新到高斯球的每个参数上

## Reference

- <https://github.com/kwea123/gaussian_splatting_notes>