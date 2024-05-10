import cocotb
from cocotb.triggers import Timer, FallingEdge, RisingEdge

async def generar_reloj_10MHz(dut):
    while True:
        dut.clk_i.value = 1
        await Timer (100, units = 'ns')
        dut.clk_i.value = 0
        await Timer (100, units = 'ns')

async def reiniciar_modulo(dut):
    dut.reset_i.value = 1
    dut.sw_i.value = 0
    dut.key_detect_i.value = 0
    dut.teclado_i.value = 0
    await Timer (200, units = 'ns')
    dut.reset_i.value = 0

@cocotb.test()
async def prueba(dut):
    await cocotb.start(generar_reloj_10MHz(dut))
    await (reiniciar_modulo(dut))
    await RisingEdge(dut.clk_i)

    #Vamos pasito a pasito
    await Timer (200, units = 'ns') #sel_modo
    await Timer (200, units = 'ns') #esp_dato_1
    dut.key_detect_i.value = 1
    await Timer (200, units = 'ns') #rec_dato_1
    dut.key_detect_i.value = 0
    dut.teclado_i.value = 2
    await Timer (200, units = 'ns') #grd dato 1
    await Timer (200, units = 'ns') #leer dato 1
    await Timer (200, units = 'ns') #most dato 1
    await Timer (200, units = 'ns') #esp opr
    dut.key_detect_i.value = 1
    await Timer (200, units = 'ns') #rec op
    dut.key_detect_i.value = 0
    dut.teclado_i.value = 10
    await Timer (200, units = 'ns') #most op
    await Timer (200, units = 'ns') #esp dato 2
    dut.key_detect_i.value = 1
    await Timer (200, units = 'ns') #rec_dato_2
    dut.key_detect_i.value = 0
    dut.teclado_i.value = 5
    await Timer (200, units = 'ns')
    await Timer (200, units = 'ns') #grd dato 2
    await Timer (200, units = 'ns') #lee dato 2
    await Timer (200, units = 'ns') #esp enter
    dut.key_detect_i.value = 1
    await Timer (200, units = 'ns') #rec_enter
    dut.key_detect_i.value = 0
    dut.teclado_i.value = 15
    await Timer (200, units = 'ns')
    await Timer (200, units = 'ns')
    await Timer (200, units = 'ns')
    await Timer (200, units = 'ns')
    await Timer (200, units = 'ns')
    await Timer (200, units = 'ns')
    await Timer (200, units = 'ns')
    await Timer (200, units = 'ns')