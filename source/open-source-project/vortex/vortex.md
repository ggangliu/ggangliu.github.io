# Vortex

## Installation

There are some github connection issue because unstable network, just need to try it again and again. Or you can download it as local source to install.

## Building

Ubuntu 20.04 will miss libhwloc.so.5 when "make -s". You can solve it through copying a libhwloc.so.5.7.6 from ubuntu 18.04.

## FPGA

### How to syn

``` bash
$ cd hw/syn/altera/opae
$ PREFIX=test1 TARGET=fpga NUM_CORES=4 make
CONFIGS="-DNUM_THREADS=4" make fpga
```

## Simulator

### Simx (Cycle Level Simulator)

``` bash
CONFIGS="-DNUM_CORES=2 -DNUM_WARPS=2" ./ci/blackbox.sh --app=vecadd 
```

### Rtlsim/Opae (RTL Level Simulator)

``` bash
./ci/blackbox.sh --driver=opae --app=demo --debug=3 --log=run_demo_opae.log
```

#### Workflow

1. 