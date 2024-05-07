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
    dut.pulso_teclas_pi.value = 0
    dut.dato_codificador_i.value = 0
    await Timer (200, units = 'ns')
    dut.reset_i.value = 0

def mapeo_key_encoding(segmento):
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

@cocotb.test()
async def prueba_columna_11(dut):
    await cocotb.start(generar_reloj_10MHz(dut))
    await reiniciar_modulo(dut)
    await RisingEdge(dut.clk_i)

    dato_codificador = 0
    valor_contador = 3

    valor_concatenado = (valor_contador << 2) | dato_codificador

    while dut.cuenta_dos_bits_o.value != 0:
        await RisingEdge(dut.clk_i)

    dut.pulso_teclas_pi.value = 1
    dut.dato_codificador_i.value = dato_codificador
    await RisingEdge(dut.data_available_o)