
<script src="/assets/css/mermaid.min.js"></script>

# GGangLiu Doc

## Overall Project Schedule

```mermaid
gantt
dateFormat YYYY-MM-DD
%%axisFormat WK%W
inclusiveEndDates
todayMarker stroke-width:3px,stroke:#0f0,opacity:0.5
title 性能模拟器开发计划概览

section 第一阶段
    %% 着力在整体框架及完整性，细节不追求完全一致
    GPU的整体框架完整(GPC/Mem)                  :t1, 2023-07-11, 3w
    Graphics流水线的基本框架及性能统计           :t2, 2023-07-11, 4w
    SMD对接复用当前软件栈                       :t3, 2023-07-17, 6w
    Performance可视化分析工具                   :t4, 2023-07-17, 3w
    分析确定MVP v3.0中各Feature参数             :t5,   after t1, 4w
    Release MVP v3.0的架构分析报告              :milestone, crit, t6, after t5, 0d
    校准性能模拟器的性能参数                     :t7,   after t4, 6w

    click t1 href "project-plan/mvp-v30-performance-evalution-plan.html"
    click t3 href "project-plan/smd-development-plan.html"
```

## Release

> Vx.x   means that this is a new feature release version
> Vx.x.x means that this a bug fix version which based on the Vx.x version

- [MVPGPU-SIM V1.0](/release/) [[Download]](/release/)
  - [x] Support OpenCL API v1.2
  - [x] Support OpenCL CTS
- MVPGPU-SIM V1.1 [[Download]](/release/)
  - Support Pytorch based on OpenCL
- MVPGPU-SIM V1.2 [[Download]](/release/)
  - Support Graphics rendering
  - Support Graphics pipeline
- MVPGPU-SIM V1.3 [[Download]](/release/)
  - Support OpenGL API v3.3
  - Support OpenGL "hello world"
- MVPGPU-SIM V1.4 [[Download]](/release/)
  - Support OpenGL CTS
- MVPGPU-SIM V1.5
  - Support MVP-libs
- MVPGPU-SIM V1.6
  - Performance Tool
  - Pipeline visualization
- MVPGPU-SIM V1.7
  - Power evaluation
- MVPGPU-SIM V1.8
  - Tensor Core
- MVPGPU-SIM V1.9
  - Ray tracing

## Directory structure

- **images** folder is used for storing all pictures docs needed
- **[ebook](/ebook/)** some ebooks
- **[release](/release/)** archive formal released version files

## Doc index

- [MVPGPU-Sim Architecture Manual](MVPGPU-Sim-Architecture-Manual.md)
- [MVPGPU-Sim User Guide](MVPGPU-Sim-User-Guide.md)
- [How to clone and commit code](how-to-clone-and-commit-code.md)
- [Project/Feature Development Flow](project-feature-development-flow.md)
- [MVPGPU-Sim Architecture Refactoring Design Principles](MVPGPU-SIM-Architecture-Refactoring-Design.md)
- OpenCL
  - [OpenCL API]mvp_notes/opencl/opencl_api.md)
  - [OpenCL CTS](mvp_notes/opencl/)
- OpenGL
  - [Graphics Support Approach](MVPGPU-SIM-Graphic-Support-Approach.md)
  - [OpenGL FS/VS Shader Program Compiling Flow](mvp_notes/opengl/shader-program-compiling-flow.md)
- Ebook
  - [Ebook list](/ebook/)

## Markdown guide

Here you are able to find out lots of intereting things about markdown

- <https://www.markdownguide.org/getting-started/>
- <https://daringfireball.net/projects/markdown/>
- <https://www.markdowntutorial.com/>
