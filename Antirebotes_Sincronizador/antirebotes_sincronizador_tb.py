import cocotb
from cocotb.triggers import FallingEdge, Timer

async def generar_reloj_10MHz (dut):
    while True:
        dut.clk_i.value = 0
        await Timer (100, units = 'ns')
        dut.clk_i.value = 1
        await Timer (100, units = 'ns')

@cocotb.test()
async def prueba_contador(dut):
    cuenta = 0
    await cocotb.start(generar_reloj_10MHz(dut))
    dut.reset_pi.value = 1
    await Timer (1, units = 'us')
    dut.reset_pi.value = 0
    await Timer (1, units = 'us')