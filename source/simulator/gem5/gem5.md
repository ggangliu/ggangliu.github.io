# GEM5

gem5 is a modular discrete event driven computer system simulator platform.

gem5 is written primarily in C++ and python and most components are provided under a BSD style license. It can simulate a complete system with devices and an operating system in full system mode (FS mode), or user space only programs where system services are provided directly by the simulator in syscall emulation mode (SE mode). There are varying levels of support for executing Alpha, ARM, MIPS, Power, SPARC, RISC-V, and 64 bit x86 binaries on CPU models including two simple single CPI models, an out of order model, and an in order pipelined model. A memory system can be flexibly built out of caches and crossbars or the Ruby simulator which provides even more flexible memory system modeling.

## Building gem5

The required dependencies

~~~ bash
sudo apt install build-essential git m4 scons zlib1g zlib1g-dev libprotobuf-dev protobuf-compiler libprotoc-dev libgoogle-perftools-dev python-dev python
~~~

First gem5 build

~~~ bash
python3 `which scons` build/X86/gem5.opt -j9
~~~

## Creating a simple configuration script

Our configuration script is going to model a very simple system. We’ll have just one simple CPU core. This CPU core will be connected to a system-wide memory bus. And we’ll have a single DDR3 memory channel, also connected to the memory bus.

gem5’s modular design is built around the **SimObject** type. Most of the components in the simulated system are SimObjects: CPUs, caches, memory controllers, buses, etc. gem5 exports all of these objects from their C++ implementation to python. Thus, from the python configuration script you can create any SimObject, set its parameters, and specify the interactions between SimObjects.

The first thing we’ll do in this file is import the m5 library and all SimObjects that we’ve compiled.

~~~ python
import m5
from m5.objects import *

system = System()

system.clk_domain = SrcClockDomain()
system.clk_domain.clock = '1GHz'
system.clk_domain.voltage_domain = VoltageDomain()

system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('512MB')]

system.cpu = X86TimingSimpleCPU() #RiscvTimingSimpleCPU() or ArmTimingSimpleCPU()
system.membus = SystemXBar()

system.cpu.icache_port = system.membus.cpu_side_ports
system.cpu.dcache_port = system.membus.cpu_side_ports

system.cpu.createInterruptController()
system.cpu.interrupts[0].pio = system.membus.mem_side_ports
system.cpu.interrupts[0].int_requestor = system.membus.cpu_side_ports
system.cpu.interrupts[0].int_responder = system.membus.mem_side_ports

system.system_port = system.membus.cpu_side_ports

system.mem_ctrl = MemCtrl()
system.mem_ctrl.dram = DDR3_1600_8x8()
system.mem_ctrl.dram.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.mem_side_ports

~~~

After those final connections, we’ve finished instantiating our simulated system! Our system should look like the figure below.
![Alt text](image.png)

gem5 can run in two different modes called **“syscall emulation”** and **“full system”** or SE and FS modes.

Syscall emulation
:   Syscall emulation mode, on the other hand, does not emulate all of the devices in a system and focuses on simulating the CPU and memory system. Syscall emulation is much easier to configure since you are not required to instantiate all of the hardware devices required in a real system. However, syscall emulation only emulates Linux system calls, and thus only models user-mode code.

Full system
:    However, if you need high fidelity modeling of the system, or OS interaction like page table walks are important, then you should use FS mode.

~~~ python
binary = 'tests/test-progs/hello/bin/x86/linux/hello'

# for gem5 V21 and beyond
system.workload = SEWorkload.init_compatible(binary)

process = Process()
process.cmd = [binary]
system.cpu.workload = process
system.cpu.createThreads()

root = Root(full_system = False, system = system)
m5.instantiate()

print("Beginning simulation!")
exit_event = m5.simulate()
print('Exiting @ tick {} because {}'.format(m5.curTick(), exit_event.getCause()))
~~~

Now that we’ve created a simple simulation script (the full version of which can be found in the gem5 code base at configs/learning_gem5/part1/simple.py ) we’re ready to run gem5.

~~~ bash
build/X86/gem5.opt configs/tutorial/part1/simple.py
~~~

## Adding cache to the configuration script

![Alt text](image-1.png)

Now, to create caches with specific parameters, we are first going to create a new file, caches.py, in the same directory as simple.py, configs/tutorial/part1. Next, let’s two more sub-classes of L1Cache, an L1DCache and L1ICache

~~~ python
from m5.objects import Cache

class L1Cache(Cache):
    assoc = 2
    tag_latency = 2
    data_latency = 2
    response_latency = 2
    mshrs = 4
    tgts_per_mshr = 20

    def connectCPU(self, cpu):
    # need to define this in a base class!
    raise NotImplementedError

    def connectBus(self, bus):
        self.mem_side = bus.cpu_side_ports

class L1ICache(L1Cache):
    size = '16kB'

    def connectCPU(self, cpu):
        self.cpu_side = cpu.icache_port

class L1DCache(L1Cache):
    size = '64kB'

    def connectCPU(self, cpu):
        self.cpu_side = cpu.dcache_port

class L2Cache(Cache):
    size = '256kB'
    assoc = 8
    tag_latency = 20
    data_latency = 20
    response_latency = 20
    mshrs = 20
    tgts_per_mshr = 12

    def connectCPUSideBus(self, bus):
        self.cpu_side = bus.mem_side_ports

    def connectMemSideBus(self, bus):
        self.mem_side = bus.cpu_side_ports
~~~

## Adding caches to the simple config file

Now, let’s add the caches we just created to the configuration script we created in the last chapter. We can’t directly connect the L1 caches to the L2 cache since the L2 cache only expects a single port to connect to it. Therefore, we need to create an L2 bus to connect our L1 caches to the L2 cache.

~~~ python
from caches import *

system.cpu.icache = L1ICache()
system.cpu.dcache = L1DCache()

system.cpu.icache.connectCPU(system.cpu)
system.cpu.dcache.connectCPU(system.cpu)

system.l2bus = L2XBar()

system.cpu.icache.connectBus(system.l2bus)
system.cpu.dcache.connectBus(system.l2bus)

system.l2cache = L2Cache()
system.l2cache.connectCPUSideBus(system.l2bus)
system.membus = SystemXBar()
system.l2cache.connectMemSideBus(system.membus)
~~~

Now we have a complete configuration with a two-level cache hierarchy. If you run the current file, hello should now finish in 57467000 ticks. The full script can be found in the gem5 source at configs/learning_gem5/part1/two_level.py.

## Understanding gem5 statistics and output

In addition to any information which your simulation script prints out, after running gem5, there are three files generated in a directory called m5out:

config.ini
:   Contains a list of every SimObject created for the simulation and the values for its parameters.

config.json
:   The same as config.ini, but in json format.

stats.txt
:   A text representation of all of the gem5 statistics registered for the simulation.

## Reference

- <https://www.gem5.org/documentation/learning_gem5/introduction/>
- <https://github.com/ggangliu/gem5/blob/stable/configs/learning_gem5/part1/simple.py>
