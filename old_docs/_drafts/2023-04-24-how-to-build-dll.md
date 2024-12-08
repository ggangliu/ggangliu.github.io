---
layout: post
title: "How to build dynamic link lib based on CMakeLists.txt"
tags: cmake
---

在构建应用程序和动态链接库时，使用CMakeLists.txt更便捷和清晰一些，动态库链接库是一个较好的给其他人提供交付件的方式。在软件架构设计中，如果采用模块化，各个模块也可以动态链接库的形式存在和被其他模块使用。

## Dynamic building

动态链接库的CMakeLists.txt如下

```cmake
cmake_minimum_required(VERSION 3.10)
SET(CMAKE_C_COMPILER "/usr/bin/gcc-9")
SET(CMAKE_CXX_COMPILER "/usr/bin/g++-9")

project(Rasterizer)

find_package(OpenCV REQUIRED)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS   "-g") 
set(CMAKE_CXX_FLAGS_DEBUG   "-O0" ) 
set(CMAKE_CXX_FLAGS_RELEASE "-O2 -DNDEBUG " ) 

include_directories(/usr/local/include/opencv4 include texture rast pa rop)

add_library(Graphic SHARED OBJ_Loader.cpp pa/Primitive_assemble.hpp pa/Primitive_assemble.cpp rast/Rasterizer.hpp 
            rast/Rasterizer.cpp include/global.hpp Triangle.hpp Triangle.cpp texture/Texture.hpp texture/Texture.cpp 
            rop/Render_output.hpp rop/Render_output.cpp include/Shader.hpp include/OBJ_Loader.h gpuc.cpp)

add_custom_command( TARGET Graphic
                    POST_BUILD
                    COMMAND ${CMAKE_COMMAND} -E copy ./libGraphic.so $(GPGPUSIM_ROOT)/lib/libGraphic.so 
)

```

## Application building

应用程序的CMakeLists.txt如下

```cmake
cmake_minimum_required(VERSION 3.10)
SET(CMAKE_C_COMPILER "/usr/bin/gcc-9")
SET(CMAKE_CXX_COMPILER "/usr/bin/g++-9")

project(Rasterizer)

find_package(OpenCV REQUIRED)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS   "-g") 
set(CMAKE_CXX_FLAGS_DEBUG   "-O0" ) 
set(CMAKE_CXX_FLAGS_RELEASE "-O2 -DNDEBUG " ) 

include_directories(/usr/local/include/opencv4 $ENV{GPGPUSIM_ROOT}/gpu/graphics/include $ENV{GPGPUSIM_ROOT}/gpu/graphics/texture)
link_directories($ENV{GPGPUSIM_ROOT}/lib)

add_executable(Rasterizer main.cpp)

target_link_libraries(Rasterizer PRIVATE Graphic ${OpenCV_LIBRARIES})
```
