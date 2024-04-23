import cocotb
from cocotb.triggers import FallingEdge, Timer

import random

async def generar_reloj_10MHz (dut):
    while True:
        dut.clk_i.value = 0
        await Timer (100, units = 'ns')
        dut.clk_i.value = 1
        await Timer (100, units = 'ns')

@cocotb.test()
async def prueba_reset(dut):
    pc_actual = 0
    pc_salto  = 0
    operacion = 0
    for test in range (16):
        await cocotb.start(generar_reloj_10MHz(dut))
        dut.pc_op_i.value = operacion
        await FallingEdge(dut.clk_i)

        assert dut.pc_o.value == pc_actual, f"El valor de LED_po esperado es {pc_actual}, se recibió {dut.pc_o.value}"
        assert dut.pcinc_o.value == pc_actual, f"El valor de LED_po esperado es {pc_salto}, se recibió {dut.pcinc_o.value}"
