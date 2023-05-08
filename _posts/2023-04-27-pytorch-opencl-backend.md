---
layout: post
title: "Pytorch OpenCL backend"
tags: opencl
---

## Pytorch OpenCL backend - simplified

- Install nighly version of pytorch for CPU in virtual environment
- Clone dlrpim_backend repository and checkout true_out_of_tree_support branch
- Update submodules
- Run few commands inside repo

    ```bash
    mkdir build
    cd build
    cmake -DCMAKE_PREFIX_PATH=$VIRTUAL_ENV/lib/python3.8/site-packages/torch/share/cmake/Torch ..
    make
    cd ..
    ```

## Run mnist training

```bash
python mnist.py --device=ocl:0
```

## Reference

[dlprimitives.org](http://blog.dlprimitives.org/)
