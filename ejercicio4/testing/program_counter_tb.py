import cocotb
from cocotb.triggers import FallingEdge, Timer, RisingEdge
from cocotb.clock import Clock
import random

NUMERO_PRUEBAS = 2**16

async def reiniciar_modulo(dut):
    dut.pc_op_i.value = 0
    dut.pc_i.value = 0
    await Timer(200, units = 'ns')


@cocotb.test()
async def prueba_reset(dut):
    clock = Clock(dut.clk_i, 100, 'ns')
    await cocotb.start(clock.start())

    pc_actual = 0
    pc_salto  = 0
    operacion = 0

    for test in range(128):
        dut.pc_op_i.value = operacion

        await FallingEdge(dut.clk_i)
        assert dut.pc_o.value == pc_actual, f"El valor de pc_o esperado es {pc_actual}, se recibió {dut.pc_o.value}"
        assert dut.pcinc_o.value == pc_salto, f"El valor de pcinc_o esperado es {pc_salto}, se recibió {dut.pcinc_o.value}"


@cocotb.test()
async def prueba_cuenta(dut):
    clock = Clock(dut.clk_i, 100, 'ns')
    await cocotb.start(clock.start())

    pc_actual = 4
    pc_salto = 0
    operacion = 2

    await(reiniciar_modulo(dut))

    for test in range(NUMERO_PRUEBAS): 
        dut.pc_op_i.value = operacion

        await FallingEdge(dut.clk_i)
        assert dut.pc_o.value == pc_actual, f"El valor de pc_o esperado es {pc_actual}, se recibió {dut.pc_o.value}"
        assert dut.pcinc_o.value == pc_salto, f"El valor de pcinc_o esperado es {pc_salto}, se recibió {dut.pcinc_o.value}" 

        pc_actual = (pc_actual + 4) & 0xFFFF


@cocotb.test()
async def prueba_hold(dut):
    clock = Clock(dut.clk_i, 100, 'ns')
    await cocotb.start(clock.start())

    pc_actual = 0
    pc_salto = 0
    operacion = 1

    await(reiniciar_modulo(dut))

    for test in range(NUMERO_PRUEBAS):
        dut.pc_op_i.value = operacion

        await Timer(400, units = 'ns')
        assert dut.pc_o.value == pc_actual, f"El valor de pc_o esperado es {pc_actual}, se recibió {dut.pc_o.value}"
        assert dut.pcinc_o.value == pc_salto, f"El valor de pcinc_o esperado es {pc_salto}, se recibió {dut.pcinc_o.value}" 

        dut.pc_op_i.value = 2
        await Timer(100, units = 'ns')
        pc_actual = (pc_actual + 4) & 0xFFFF
    

@cocotb.test()
async def prueba_salto(dut):
    clock = Clock(dut.clk_i, 100, 'ns')
    await cocotb.start(clock.start())

    dir_salto = 4
    pc_salto = dir_salto
    operacion = 3

    await(reiniciar_modulo(dut))

    for test in range(NUMERO_PRUEBAS):
        dut.pc_op_i.value = operacion
        dut.pc_i.value = dir_salto

        await FallingEdge(dut.clk_i)
        assert dut.pc_o.value == dir_salto, f"El valor de pc_o esperado luego del salto es es {dir_salto}, se recibió {dut.pc_o.value}"
        assert dut.pcinc_o.value == pc_salto, f"El valor de pcinc_o esperado es {pc_salto}, se recibió {dut.pcinc_o.value}" 

        dir_salto = (dir_salto + 4) & 0xFFFF
        pc_salto = dir_salto


@cocotb.test()
async def prueba_salto_aleatorio(dut):
    clock = Clock(dut.clk_i, 100, 'ns')
    await cocotb.start(clock.start())

    operacion = 3

    await(reiniciar_modulo(dut))

    for test in range(NUMERO_PRUEBAS):
        direccion_salto = random.randint(0, (NUMERO_PRUEBAS - 1))
        pc_inc = ((dut.pc_i.value + 4) & 0xFFFF)

        dut.pc_op_i.value = operacion
        dut.pc_i.value = direccion_salto

        await FallingEdge(dut.clk_i)
        assert dut.pc_o.value == direccion_salto, f"El valor de pc_o esperado luego del salto es es {direccion_salto}, se recibió {dut.pc_o.value}"
        assert dut.pcinc_o.value == pc_inc, f"El valor de pcinc_o esperado es {pc_inc}, se recibió {dut.pcinc_o.value}"
