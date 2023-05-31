---
layout: post
title: "Understanding vertex transformation"
tags: opengl graphics
---

Vertex Shader -> Clip Space -> 透视除法 -> NDC -> 视口变换[^3] -> Window Space -> Fragment Shader

根据OpenGL，使用VS来进行顶点的坐标变化，即用MVP矩阵对顶点进行变换。此时，顶点从物体空间(Local Space)转换到了裁剪空间（Clip Space）。在投影变化（From View space to Clip space）中，顶点总是被投影到近平面上，然后再被变换到裁剪空间中。投影矩阵会将观察坐标系下顶点的Zveiw值存放到裁剪坐标系下的Wclip分量上。在ST模块中，顶点转换的第一步即为将顶点坐标由裁剪坐标系转换到NDC[^1]，这一步是通过将裁剪坐标除以Wclip分量实现的。

Clip Space
: 顶点乘以MVP矩阵之后所在的空间，Vertex Shader的输出就是在Clip Space上，接着由GPU自己做透视除法[^2]将顶点转到NDC

![vertex transformation](/assets/snip-images/tranformation-render-pipeline.png)

## Question

1. Screen Space中的w分量存的是View Space中的Z
[Answer]

[^1]: 标准化设备坐标(normalized device coordinates)，是一个长宽高取值范围为[-1, 1]的立方体，超过这个范围的顶点都会被GPU裁剪掉
[^2]: 透视除法就是将Clip Space顶点的4个分量都除以W分量，就从Clip Space转换到NDC了
[^3]: 视口变换的计算方法简单，假设视口的原点为(x,y)，长宽为(width, height)。以x轴为例，变换只是将NDC的[-1, 1]线性映射到[x, x+width]范围内。z轴则会从NDC的[-1, 1]映射到[nearVal, farVal]内(默认near=0, far=1)。width, height, near, far等参数可以通过如下函数指定：

```c++
  void glViewport(GLint *x*, GLint *y*, GLsizei *width*, GLsizei *height*);
  void glDepthRangef(GLfloat *nearVal*, GLfloat *farVal*);
  ```
