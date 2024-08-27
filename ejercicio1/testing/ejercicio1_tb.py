import cocotb
from cocotb.triggers import Timer, FallingEdge
from cocotb.clock import Clock

NUMERO_PRUEBAS = 2**8

async def iniciar_reloj(dut, periodo = 100, unidad = 'ns'):
    clock = Clock(dut.clk_pi, periodo, unidad)
    await cocotb.start(clock.start())

@cocotb.test()
async def prueba_reloj(dut):
    valor_LED = 0
    await iniciar_reloj(dut)

    for i in range(NUMERO_PRUEBAS):
        await Timer (10, units = 'us')

        if valor_LED == 0:
            valor_LED = 1
        else:
            valor_LED = 0

        await FallingEdge(dut.clk_pi)

        assert dut.led_po.value == valor_LED, f"El valor de LED_po esperado es {valor_LED}, se recibió {dut.led_po.value}"
