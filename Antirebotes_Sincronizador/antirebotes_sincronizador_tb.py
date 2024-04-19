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
async def prueba_contador(dut):
    cuenta = 0
    await cocotb.start(generar_reloj_10MHz(dut))
    dut.reset_pi.value = 1
    dut.boton_pi.value = 0
    await Timer (100, units = 'us')
    dut.reset_pi.value = 0
    dut.boton_pi.value = 0
    await Timer (100, units = 'us')

    for test in range (128):
        tiempo_pulso = random.randint(1, 16)
        dut.boton_pi.value = 1
        await Timer (tiempo_pulso, units = 'us')
        dut.boton_pi.value = 0
        await Timer (10, units = 'us')

        if tiempo_pulso >= 7:
            cuenta = cuenta + 1
        else:
            cuenta = cuenta

        await FallingEdge(dut.clk_i)
        assert dut.conta_o.value == cuenta, f"El valor del contador esperado es {cuenta}, se recibió {dut.conta_o.value}"
    

    #dut.boton_pi.value = 1
    #await Timer (7, units = 'us') #Unidad minima de tiempo para que cambie el contador

    #dut.boton_pi.value = 0
    #await Timer (250, units = 'us')