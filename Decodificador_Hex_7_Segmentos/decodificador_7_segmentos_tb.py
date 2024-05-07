import cocotb
from cocotb.triggers import Timer, FallingEdge, RisingEdge

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
    await Timer (200, units = 'ns')
    dut.reset_i.value = 0


@cocotb.test()
async def prueba_dosplay_7_segmentos(dut):
    def mapeo_codificacion_display(segmento):
        mapeo = {
        '0000': int('1000000', 2),  # 0
        '0001': int('1111001', 2),  # 1
        '0010': int('0100100', 2),  # 2
        '0011': int('0110000', 2),  # 3
        '0100': int('0011001', 2),  # 4
        '0101': int('0010010', 2),  # 5
        '0110': int('0000010', 2),  # 6
        '0111': int('1111000', 2),  # 7
        '1000': int('0000000', 2),  # 8
        '1001': int('0010000', 2),  # 9
        '1010': int('0001000', 2),  # A
        '1011': int('0000011', 2),  # B
        '1100': int('1000110', 2),  # C
        '1101': int('0100001', 2),  # D
        '1110': int('0000110', 2),  # E
        '1111': int('0001110', 2)   # F
    }
        return mapeo.get(segmento, int('1111111', 2))

    indice_display = [13, 11, 7, 14]

    await cocotb.start(generar_reloj_10MHz(dut))
    await (reiniciar_modulo(dut))
    await RisingEdge(dut.clk_i)


    NUMERO_PRUEBAS = 2**16

    for prueba in range (NUMERO_PRUEBAS):
        dato_entrada = prueba
        for display in range (4):
            display_activo = indice_display[display]
            dut.data_i.value = dato_entrada
            dut.we_i.value = 1

            if display_activo == 14:
                segmento = dato_entrada & 0xF
            
            elif display_activo == 7:
                segmento = (dato_entrada >> 4) & 0xF

            elif display_activo == 11:
                segmento = (dato_entrada >> 8) & 0xF

            elif display_activo == 13:
                segmento = (dato_entrada >> 12) & 0xF

            segmento_binario = f'{segmento:04b}'
            led = mapeo_codificacion_display(segmento_binario)

            await FallingEdge(dut.clk_i)

            assert dut.an_o.value == display_activo, f"El valor de an_o esperado es {display_activo}, se recibió {dut.an_o.value}"
            assert dut.seg_o.value == led, f"El valor de seg_o esperado es {led}, se recibió {dut.seg_o.value} en la posición {dut.an_o.value}"


