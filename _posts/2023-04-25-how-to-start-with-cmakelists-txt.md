---
layout: post
title: "How to start CMake build system with CMakeLists.txt"
tags: cmake
---

A project can have multiple CMakeLists.txt, but only one in each directory.

For the one in the top level of directory of the project, the following must be present at the top of the file.

```cmake
cmake_minimum_required(VERSION 3.6) 
project(foo)
```

Let's take a look at a sample project layout below:

```yaml
- CMakeLists.txt
- some.h
- some.cpp
- main.cpp
```

## Building the library

Variables are created and destroyed using the set() and unset() functions.

```cmake
set(some_var "a" "b" "c")
message("${some_var}")
```

Now, to build our library, we must add the following to the build file, CMakeLists.txt:

```cmake
set(FOO_SOURCES some.cpp)
add_library(foos STATIC "${FOO_SOURCES}")
```

In the call to add_library(), the STATIC/SHARED tells CMake whether we want a static library or shared library.

## Adding the executable

Let's make up a sample C++ file, *main.cpp*, that calls a function from our library:

```cpp
#include "some.h"
int main(int argc, char const* argv[]) {
    someFunc(); // defined in some.cpp
    return 0;
}
```

Then, we can add to the build file the following:

```cmake
add_executable(foot main.cpp)
target_link_libraries(foot foos)
```

The *target_link_libraries* function takes a target as the first argument, and then a list of other targets that must be libraries, to like to the first argument.

## Putting it all together

If one is currently in the directory of the project, these commands are often used:

```bat
mkdir build
cd build
cmake ..
make
```

This will run CMake, and get it to produce build files in the current directory.

## Understanding the CMakeLists.txt Files

- *include_directories* command add a directory for the compiler to search in for your header(.h) files
- *add_subdirectory* commands instructs CMake to go into a subdirectory and look for another *CMakeLists.txt* to run

## Reference

- [CMakeLists.txt](https://www.jetbrains.com/help/clion/cmakelists-txt-file.html)
- [CMake Tutorial](https://cmake.org/cmake/help/latest/guide/tutorial/index.html)
- [Adding a Custom Command and Generated File](https://cmake.org/cmake/help/latest/guide/tutorial/Adding%20a%20Custom%20Command%20and%20Generated%20File.html)
