---
layout: post
title: "OpenCL"
tag: Archived
---

## OpenCL API

### async_work_group_copy

The OpenCL C programming language implements the following functions that provide asynchronous copies between global and local memory and a prefetch from global memory.

- Interface Definition

```OpenCL
event_t async_work_group_copy ( __local gentype *dst,
                          const __global gentype *src,
                          size_t  num_elements,
                          event_t event)
event_t async_work_group_copy ( __global gentype *dst,
                          const __local gentype *src,
                          size_t num_elements,
                          event_t event)
void wait_group_events (int num_events, event_t *event_list)
void prefetch (const __global gentype *p, size_t num_elements)
```

- Function description

|Function |Description|
|:--------|:----------|
| async_work_group_copy | Perform an async copy of num_gentypes gentype elements from src to dst; </br> The async copy is performed by **all work-items in a work-group** and this built-in function must therefore be encountered by all work-items in a work-group executing the kernel with **the same argument values**; </br> otherwise the results are undefined; |
|async_work_group_strided_copy|Perform an async gather of num_gentypes gentype elements from src to dst.|
|wait_group_events|Wait for events that identify the async_work_group_copy operations to complete.|
|prefetch|Prefetch num_gentypes * sizeof(gentype) bytes into the global cache.|

- Example

```OpenCL
__kernel void test(__global float *x) {
    __local xcopy[GROUP_SIZE];
    int globalid = get_global_id(0);
    int localid = get_local_id(0);
    event_t e = async_work_group_copy(xcopy, x+globalid-localid, GROUP_SIZE, 0);
    wait_group_events(1, &e);   
}
```

### Usage

- The call to async_work_group_copy() must be executed by all work-items in the group
- Source and destination address need to be the same for all work items
- num_gentypes is the number of elements, not the size in bytes

### Reference

- <https://stackoverflow.com/questions/15545841/how-to-use-async-work-group-copy-in-opencl>
- <https://registry.khronos.org/OpenCL/specs/opencl-1.0.pdf#page=201>
- <https://man.opencl.org/async_work_group_copy.html>

### Download

[[PDF]](/assets/OpenCL_Note.pdf)
