# Amaranth

The Amaranth toolchain consists of the Amaranth language, the standard library, the simulator, and the build system, covering all steps of a typical FPGA development workflow.

## Amaranth language

### Signal

``` python
a = Signal(5)
b = Signal(8, init=1)
```

### Control flow

- If/Elif/Else

``` python
timer = Signal(8)
with m.If(up):
    m.d.sync += timer.eq(timer + 1)
with m.Elif(down):
    m.d.sync += timer.eq(timer - 1)
```

- Switch/Case


- FSM/State

``` python
bus_addr = Signal(16)
with m.FSM():
    with m.State("Set Address"):
        m.d.sync += addr.eq(0x1234)
        m.next = "Strobe Read Enable"
    with m.State("Strobe Read Enable"):
        m.d.comb += r_en.eq(1)
        m.next = "Sample Data"
    with m.State("Sample Data"):
        m.d.sync += latched.eq(r_data)
        with m.If(r_data == 0):
            m.next = "Set Address"

with m.FSM(init="Set Address")

with m.FSM(domain="sync")

with m.FSM() as fsm:
    ...

with m.If(fsm.ongoing("Set Address")):
    ...
```

### Clock domains

``` python
m.domains.video = cd_video = ClockDomain(local=True)

def add_video_domain(n):
    cd = ClockDomain(f"video_{n}", local=True)
    m.domains += cd
    return cd

add_video_domain(2)
```

### Elaboration

``` python
class Counter(Elaboratable):
    def elaborate(self, platform):
        m = Module()

        ...

        return m
```

- Submodules

``` python
m.submodules.counter = counter = Counter()

for n in range(3):
    m.submodules[f"counter_{n}"] = Counter()

counter = Counter()
m.submodules += counter
```

### Memories

amaranth.lib.memory

### Instances

A submodule written in a non-Amaranth language is called an instance. An instance can be written in any language supported by the synthesis toolchain; usually, that is (System)Verilog, VHDL, or a language that is translated to one of those two.

``` python
m.submodules.name = Instance("type", ...)
```

## Amaranth standard library

amaranth.lib
amaranth.lib.enum
amaranth.lib.data
amaranth.lib.wiring
amaranth.lib.cdc
amaranth.lib.memory
amaranth.lib.coding
amaranth.lib.fifo
amaranth.lib.crc

## Amaranth simulator

## Amaranth build system

## Reference

- [amaranth-lang.org](https://amaranth-lang.org/docs/amaranth/latest/)