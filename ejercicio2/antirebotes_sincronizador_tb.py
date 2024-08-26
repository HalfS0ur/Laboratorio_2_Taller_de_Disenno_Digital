import cocotb
from cocotb.triggers import FallingEdge, Timer
from cocotb.clock import Clock
import random

periodo_boton = 4
numero_pruebas = 2**8

async def reset_dut(dut, duration=100):
    dut.reset_pi.value = 1
    dut.boton_pi.value = 0
    await Timer(duration, units='us')
    dut.reset_pi.value = 0
    await Timer(duration, units='us')
    await FallingEdge(dut.clk_i)

@cocotb.test()
async def prueba_contador(dut):
    clock = Clock(dut.clk_i, 100, 'ns')
    await cocotb.start(clock.start())
    await reset_dut(dut)
    
    dut.boton_pi.value = 0
    cuenta = 0

    for test in range(numero_pruebas):
        tiempo_pulso = random.randint(1, 16)
        dut.boton_pi.value = 1
        await Timer(tiempo_pulso, units='us')
        dut.boton_pi.value = 0
        await Timer(10, units='us')

        if tiempo_pulso >= periodo_boton:
            cuenta += 1

        await FallingEdge(dut.clk_i)
        assert dut.conta_o.value == cuenta, f"El valor del contador esperado es {cuenta}, se recibió {dut.conta_o.value}"