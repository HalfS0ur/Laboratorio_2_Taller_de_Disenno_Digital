import cocotb
from cocotb.triggers import FallingEdge, Timer

async def generar_reloj_10MHz (dut):
    while True:
        dut.clk_i.value = 0
        await Timer (100, units = 'ns')
        dut.clk_i.value = 1
        await Timer (100, units = 'ns')

@cocotb.test()
async def verificacion_reloj (dut):
    valor_LED = 0
    for i in range (20):
        await cocotb.start(generar_reloj_10MHz(dut))
        await Timer (20, units = 'us')
        valor_LED = 1 if valor_LED == 0 else 0
        await FallingEdge(dut.clk_i)

        dut._log.info("my_signal_1 is %s", dut.LED_po.value)
        assert dut.LED_po.value == valor_LED, f"El valor de LED_po esperado es {valor_LED}, se recibió {dut.LED_po.value}"