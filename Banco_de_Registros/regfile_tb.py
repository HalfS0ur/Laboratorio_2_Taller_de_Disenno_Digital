import cocotb
from cocotb.triggers import Timer, FallingEdge, RisingEdge

import random

async def generar_reloj_10MHz(dut):
    while True:
        dut.clk_i.value = 0
        await Timer (100, units = 'ns')
        dut.clk_i.value = 1
        await Timer (100, units = 'ns')

async def reiniciar_modulo(dut):
    dut.reset_i.value = 1
    dut.we_i = 0
    dut.data_in = 0
    dut.addr_rd = 0
    dut.addr_rs1 = 0
    dut.addr_rs2 = 0
    await Timer (400, units = 'ns')
    dut.reset_i.value = 0


@cocotb.test()
async def prueba_escritura_secuencial(dut):
    NUMERO_REGISTROS = 2**5
    
    await (reiniciar_modulo(dut))

    for escritura in range (NUMERO_REGISTROS):
        await cocotb.start(generar_reloj_10MHz(dut))
        dut.we_i.value = 1
        dut.data_in.value = escritura
        dut.addr_rd.value = escritura
        await FallingEdge(dut.clk_i)

    for dato in range (NUMERO_REGISTROS):
        dut.we_i.value = 0
        dut.addr_rs1.value = dato
        dut.addr_rs2.value = dato
        await FallingEdge(dut.clk_i)
        assert dut.rs1.value == dato, f"El valor de rs1 esperado es {dato}, se recibió {dut.rs1.value}"
        assert dut.rs2.value == dato, f"El valor de rs1 esperado es {dato}, se recibió {dut.rs2.value}"