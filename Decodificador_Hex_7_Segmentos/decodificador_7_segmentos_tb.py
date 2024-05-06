import cocotb
from cocotb.triggers import Timer, FallingEdge

async def generar_reloj_10MHz(dut):
    while True:
        dut.clk_i.value = 0
        await Timer (100, units = 'ns')
        dut.clk_i.value = 1
        await Timer (100, units = 'ns')

async def reiniciar_modulo(dut):
    dut.reset_i.value = 1
    dut.we_i.value = 0
    dut.data_i.value = 0
    await Timer (100, units = 'ns')
    dut.reset_i.value = 0


@cocotb.test()
async def prueba_dosplay_7_segmentos(dut):
    indice_display = [13, 11, 7, 14]

    await cocotb.start(generar_reloj_10MHz(dut))
    await (reiniciar_modulo(dut))

    NUMERO_PRUEBAS = 2**6 #16

    for prueba in range (NUMERO_PRUEBAS):
        dato_entrada = prueba
        for display in range (4):
            display_activo = indice_display[display]
            dut.data_i.value = dato_entrada
            dut.we_i.value = 1
            await FallingEdge(dut.clk_i)

            assert dut.an_o.value == display_activo, f"El valor de an_o esperado es {display_activo}, se recibió {dut.an_o.value}"


