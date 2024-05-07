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

def mapeo_key_encoding(valor_teclado):
        mapeo = {
        '0000': int('0111', 2),  # 7
        '0001': int('1010', 2),  # A
        '0010': int('1001', 2),  # 9
        '0011': int('1000', 2),  # 8
        '0100': int('0100', 2),  # 4
        '0101': int('1011', 2),  # B
        '0110': int('0110', 2),  # 6
        '0111': int('0101', 2),  # 5
        '1000': int('0001', 2),  # 1
        '1001': int('1100', 2),  # C
        '1010': int('0011', 2),  # 3
        '1011': int('0010', 2),  # 2
        '1100': int('1111', 2),  # F
        '1101': int('1101', 2),  # D
        '1110': int('1110', 2),  # E
        '1111': int('0000', 2)   # 0
    }
        return mapeo.get(valor_teclado, int('1111', 2))

async def procesar_datos(valor_codificador, valor_contador):
     concatenacion = (valor_contador << 2) | valor_codificador
     valor_binario = f'{concatenacion:04b}'
     return valor_binario

@cocotb.test()
async def prueba_columna_11(dut):
    await cocotb.start(generar_reloj_10MHz(dut))
    await reiniciar_modulo(dut)
    await RisingEdge(dut.clk_i)

    dato_codificador = 0
    valor_contador = 3

    valor_codificado = mapeo_key_encoding(procesar_datos(dato_codificador, valor_contador))

    while dut.cuenta_dos_bits_o.value != 0:
        await RisingEdge(dut.clk_i)

    dut.pulso_teclas_pi.value = 1
    dut.dato_codificador_i.value = dato_codificador
    await FallingEdge(dut.data_available_o)
    assert dut.dato_codificado_o.value == valor_codificado
    dut.pulso_teclas_pi.value = 0

    await reiniciar_modulo(dut)
    await Timer (100, units = 'ns')
    dato_codificador = 1
    valor_codificado = mapeo_key_encoding(procesar_datos(dato_codificador, valor_contador))

    while dut.cuenta_dos_bits_o.value != 0:
        await RisingEdge(dut.clk_i)

    dut.pulso_teclas_pi.value = 1
    dut.dato_codificador_i.value = dato_codificador
    await FallingEdge(dut.data_available_o)
    assert dut.dato_codificado_o.value == valor_codificado
    dut.pulso_teclas_pi.value = 0
 #######################################################################################3

@cocotb.test()
async def aver(dut):
    await cocotb.start(generar_reloj_10MHz(dut))
    await reiniciar_modulo(dut)
    await RisingEdge(dut.clk_i)

    for test in range (1):
        dato_codificador = test
        valor_contador = 3

        valor_codificado = mapeo_key_encoding(procesar_datos(dato_codificador, valor_contador))

        while dut.cuenta_dos_bits_o.value != 0:
            await RisingEdge(dut.clk_i)

        dut.pulso_teclas_pi.value = 1
        dut.dato_codificador_i.value = dato_codificador
        await FallingEdge(dut.data_available_o)
        assert dut.dato_codificado_o.value == valor_codificado
        dut.pulso_teclas_pi.value = 0
        await reiniciar_modulo(dut)
        await Timer (100, units = 'ns')