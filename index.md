---
layout: default
---

  <h2>Overview</h2>

  Chai is a benchmark suite of Collaborative Heterogeneous Applications for Integrated-architectures.
  The Chai benchmarks are designed to use the latest features of heterogeneous architectures such as shared virtual memory and system-wide atomics to achieve efficient simultaneous collaboration between host and accelerator devices.

  Each benchmark has multiple implementations: OpenCL-U, OpenCL-D, CUDA-U, CUDA-D, CUDA-U-Sim, CUDA-D-Sim, and C++AMP.
  The versions suffixed with -U use unified memory and system-wide atomics while the versions suffixed with -D use the traditional communication techniques of discrete architectures.
  The versions suffixed with -Sim run on the gem5-gpu simulator.

  Check out our [Getting Started](gettingstarted) page for instructions on how to download and use the benchmarks.

Please cite the following paper if you find our benchmark suite useful:

* J. Gómez-Luna, I. El Hajj, L.-W. Chang, V. Garcia-Flores, S. Garcia de Gonzalo, T. Jablin, A. J. Peña, W.-M. Hwu.
  **Chai: Collaborative Heterogeneous Applications for Integrated-architectures.**
  In *Proceedings of IEEE International Symposium on Performance Analysis of Systems and Software (ISPASS)*, 2017.
  [\[pdf\]](/assets/ispass17.pdf)
  [\[slides\]](/assets/ispass17.pptx)
  [\[bibtex\]](/assets/ispass17.bib)

