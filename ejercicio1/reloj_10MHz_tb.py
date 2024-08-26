import cocotb
from cocotb.triggers import FallingEdge, Timer
from cocotb.clock import Clock

numero_pruebas = 2**8

@cocotb.test()
async def verificacion_reloj(dut):
    clock = Clock(dut.clk_i, 100, 'ns')
    valor_LED = 0
    await cocotb.start(clock.start())

    for i in range (numero_pruebas):   
        await Timer (10, units = 'us')
        valor_LED = 1 if valor_LED == 0 else 0
        await FallingEdge(dut.clk_i)

        assert dut.LED_po.value == valor_LED, f"El valor de LED_po esperado es {valor_LED}, se recibió {dut.LED_po.value}"