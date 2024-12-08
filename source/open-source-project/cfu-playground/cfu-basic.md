# CFU

## Software needed

- picocom
  picocom --baud 115200 /dev/ttyUSB1
- openocd
  openocd -f ./openocd_xilinx.cfg -c "init ; pld load 0 top.bit ; exit"
  [openocd_xilinx.cfg](https://github.com/litex-hub/linux-on-litex-vexriscv/blob/master/prog/openocd_xilinx.cfg)
