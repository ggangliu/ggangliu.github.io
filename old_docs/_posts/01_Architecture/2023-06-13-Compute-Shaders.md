---
layout: post
title: "An Introduction to Compute Shaders"
tags: graphics
---

## GPU Computing

See a demo: [Mythbusters Demo GPU versus CPU](https://www.youtube.com/watch?v=-P28LKWTzrI)
<iframe width="840" height="515" src="https://www.youtube.com/embed/-P28LKWTzrI" title="Mythbusters Demo GPU versus CPU" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Compute Shader Stage

To make GPU computing easier accessible especially for graphics applications while sharing common memory mappings, the OpenGL standard introduced the compute shader in OpenGL version 4.3 as a shader stage for computing arbitrary information. OpenGL compute shader is intentionally designed to incorporate with other OpenGL functionality and uses GLSL to make it easier to integrate with the existing OpenGL graphics pipeline/application.

Compute shaders are general-purpose shaders and in contrast to the other shader stages, they operate differently as they are not part of the graphics pipeline.

To pass data to the compute shader, the shader needs to fetch the data for example via texture access, image loads or shader storage block access, which has to be used as target to explicitly write the computed data to an image or shader storage block as well.

### Compute space

![local space](/assets/snip-images/local_space.png)

### Create your first compute shader

Now that we have a broad overview about compute shaders let's put it into practice by creating a "Hello-World" program. The program should write (color) data to the pixels of an image/texture object in the compute shader. After finishing the compute shader execution it will display the texture on the screen using a second shader program which uses a vertex shader to draw a simple screen filling quad and a fragment shader.

## Reference

- <https://learnopengl.com/Guest-Articles/2022/Compute-Shaders/Introduction>
- <https://antongerdelan.net/opengl/compute.html>
