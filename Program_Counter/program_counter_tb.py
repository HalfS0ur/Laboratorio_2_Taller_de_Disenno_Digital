import cocotb
from cocotb.triggers import FallingEdge, Timer, RisingEdge

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

        assert dut.pc_o.value == pc_actual, f"El valor de pc_o esperado es {pc_actual}, se recibió {dut.pc_o.value}"
        assert dut.pcinc_o.value == pc_salto, f"El valor de pcinc_o esperado es {pc_salto}, se recibió {dut.pcinc_o.value}"


@cocotb.test()
async def prueba_cuenta_hold(dut):
    pc_actual = 4
    pc_salto = 0
    operacion = 2
    for test in range (5):  #32768
        await cocotb.start(generar_reloj_10MHz(dut))
        dut.pc_op_i.value = operacion
        await FallingEdge(dut.clk_i)
        #pc_actual = pc_actual + 4

        assert dut.pc_o.value == pc_actual, f"El valor de pc_o esperado es {pc_actual}, se recibió {dut.pc_o.value}"
        assert dut.pcinc_o.value == pc_salto, f"El valor de pcinc_o esperado es {pc_salto}, se recibió {dut.pcinc_o.value}"

        pc_actual = pc_actual + 4

    dut.pc_op_i.value = 1
    pc_hold = pc_actual - 4
    await Timer (20, units = 'us')
    assert dut.pc_o.value == pc_hold, f"El valor de pc_o esperado al detener la cuenta es {pc_hold}, se recibió {dut.pc_o.value}"
    assert dut.pcinc_o.value == pc_salto, f"El valor de pcinc_o esperado al detener la cuenta es {pc_salto}, se recibió {dut.pcinc_o.value}"

    await Timer (4, units = 'us')
    dut.pc_op_i.value = 0
    await Timer (4, units = 'us')

@cocotb.test()
async def prueba_salto(dut):
    pc_actual = 0
    pc_salto = 0
    dir_salto = 0
    operacion = 3
    for test in range (256):
        await cocotb.start(generar_reloj_10MHz(dut))
        dut.pc_op_i.value = operacion
        dir_salto = random.randint(0, 65536)
        dut.pc_i.value = dir_salto
        await RisingEdge(dut.clk_i)
        await FallingEdge(dut.clk_i)

        assert dut.pc_o.value == dir_salto, f"El valor de pc_o esperado al realizar el salto es {dir_salto}, se recibió {dut.pc_o.value}"

        pc_salto = pc_actual + 4
        pc_actual = dir_salto

        assert dut.pcinc_o.value == pc_salto, f"El valor de pcinc_o esperado al realizar el salto es {pc_salto}, se recibió {dut.pcinc_o.value}"