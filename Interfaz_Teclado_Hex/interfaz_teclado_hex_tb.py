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

@cocotb.test()
async def Prueba_tecla_0(dut):
    await cocotb.start(generar_reloj_10MHz(dut))
    await reiniciar_modulo(dut)
    await RisingEdge(dut.clk_i)

    dato_codificador = 3
    valor_contador = 3

    valor_concatenado = (valor_contador << 2) | dato_codificador
    valor_binario = f'{valor_concatenado:04b}'
    valor_codificado = mapeo_key_encoding(valor_binario)

    while dut.cuenta_dos_bits_o.value != 0:
        await RisingEdge(dut.clk_i)

    dut.pulso_teclas_pi.value = 1
    dut.dato_codificador_i.value = dato_codificador
    await FallingEdge(dut.data_available_o)
    assert dut.dato_codificado_o.value == valor_codificado
    dut.pulso_teclas_pi.value = 0


@cocotb.test()
async def Prueba_tecla_1(dut):
    await cocotb.start(generar_reloj_10MHz(dut))
    await reiniciar_modulo(dut)
    await RisingEdge(dut.clk_i)

    dato_codificador = 0
    valor_contador = 2

    valor_concatenado = (valor_contador << 2) | dato_codificador
    valor_binario = f'{valor_concatenado:04b}'
    valor_codificado = mapeo_key_encoding(valor_binario)

    while dut.cuenta_dos_bits_o.value != 3:
        await RisingEdge(dut.clk_i)

    dut.pulso_teclas_pi.value = 1
    dut.dato_codificador_i.value = dato_codificador
    await FallingEdge(dut.data_available_o)
    assert dut.dato_codificado_o.value == valor_codificado
    dut.pulso_teclas_pi.value = 0


@cocotb.test()
async def Prueba_tecla_2(dut):
    await cocotb.start(generar_reloj_10MHz(dut))
    await reiniciar_modulo(dut)
    await RisingEdge(dut.clk_i)

    dato_codificador = 3
    valor_contador = 2

    valor_concatenado = (valor_contador << 2) | dato_codificador
    valor_binario = f'{valor_concatenado:04b}'
    valor_codificado = mapeo_key_encoding(valor_binario)

    while dut.cuenta_dos_bits_o.value != 3:
        await RisingEdge(dut.clk_i)

    dut.pulso_teclas_pi.value = 1
    dut.dato_codificador_i.value = dato_codificador
    await FallingEdge(dut.data_available_o)
    assert dut.dato_codificado_o.value == valor_codificado
    dut.pulso_teclas_pi.value = 0


@cocotb.test()
async def Prueba_tecla_3(dut):
    await cocotb.start(generar_reloj_10MHz(dut))
    await reiniciar_modulo(dut)
    await RisingEdge(dut.clk_i)

    dato_codificador = 2
    valor_contador = 2

    valor_concatenado = (valor_contador << 2) | dato_codificador
    valor_binario = f'{valor_concatenado:04b}'
    valor_codificado = mapeo_key_encoding(valor_binario)

    while dut.cuenta_dos_bits_o.value != 3:
        await RisingEdge(dut.clk_i)

    dut.pulso_teclas_pi.value = 1
    dut.dato_codificador_i.value = dato_codificador
    await FallingEdge(dut.data_available_o)
    assert dut.dato_codificado_o.value == valor_codificado
    dut.pulso_teclas_pi.value = 0


@cocotb.test()
async def Prueba_tecla_4(dut):
    await cocotb.start(generar_reloj_10MHz(dut))
    await reiniciar_modulo(dut)
    await RisingEdge(dut.clk_i)

    dato_codificador = 0
    valor_contador = 1

    valor_concatenado = (valor_contador << 2) | dato_codificador
    valor_binario = f'{valor_concatenado:04b}'
    valor_codificado = mapeo_key_encoding(valor_binario)

    while dut.cuenta_dos_bits_o.value != 2:
        await RisingEdge(dut.clk_i)

    dut.pulso_teclas_pi.value = 1
    dut.dato_codificador_i.value = dato_codificador
    await FallingEdge(dut.data_available_o)
    assert dut.dato_codificado_o.value == valor_codificado
    dut.pulso_teclas_pi.value = 0


@cocotb.test()
async def Prueba_tecla_5(dut):
    await cocotb.start(generar_reloj_10MHz(dut))
    await reiniciar_modulo(dut)
    await RisingEdge(dut.clk_i)

    dato_codificador = 3
    valor_contador = 1

    valor_concatenado = (valor_contador << 2) | dato_codificador
    valor_binario = f'{valor_concatenado:04b}'
    valor_codificado = mapeo_key_encoding(valor_binario)

    while dut.cuenta_dos_bits_o.value != 2:
        await RisingEdge(dut.clk_i)

    dut.pulso_teclas_pi.value = 1
    dut.dato_codificador_i.value = dato_codificador
    await FallingEdge(dut.data_available_o)
    assert dut.dato_codificado_o.value == valor_codificado
    dut.pulso_teclas_pi.value = 0


@cocotb.test()
async def Prueba_tecla_6(dut):
    await cocotb.start(generar_reloj_10MHz(dut))
    await reiniciar_modulo(dut)
    await RisingEdge(dut.clk_i)

    dato_codificador = 2
    valor_contador = 1

    valor_concatenado = (valor_contador << 2) | dato_codificador
    valor_binario = f'{valor_concatenado:04b}'
    valor_codificado = mapeo_key_encoding(valor_binario)

    while dut.cuenta_dos_bits_o.value != 2:
        await RisingEdge(dut.clk_i)

    dut.pulso_teclas_pi.value = 1
    dut.dato_codificador_i.value = dato_codificador
    await FallingEdge(dut.data_available_o)
    assert dut.dato_codificado_o.value == valor_codificado
    dut.pulso_teclas_pi.value = 0


@cocotb.test()
async def Prueba_tecla_7(dut):
    await cocotb.start(generar_reloj_10MHz(dut))
    await reiniciar_modulo(dut)
    await RisingEdge(dut.clk_i)

    dato_codificador = 0
    valor_contador = 0

    valor_concatenado = (valor_contador << 2) | dato_codificador
    valor_binario = f'{valor_concatenado:04b}'
    valor_codificado = mapeo_key_encoding(valor_binario)

    while dut.cuenta_dos_bits_o.value != 1:
        await RisingEdge(dut.clk_i)

    dut.pulso_teclas_pi.value = 1
    dut.dato_codificador_i.value = dato_codificador
    await FallingEdge(dut.data_available_o)
    assert dut.dato_codificado_o.value == valor_codificado
    dut.pulso_teclas_pi.value = 0


@cocotb.test()
async def Prueba_tecla_8(dut):
    await cocotb.start(generar_reloj_10MHz(dut))
    await reiniciar_modulo(dut)
    await RisingEdge(dut.clk_i)

    dato_codificador = 3
    valor_contador = 0

    valor_concatenado = (valor_contador << 2) | dato_codificador
    valor_binario = f'{valor_concatenado:04b}'
    valor_codificado = mapeo_key_encoding(valor_binario)

    while dut.cuenta_dos_bits_o.value != 1:
        await RisingEdge(dut.clk_i)

    dut.pulso_teclas_pi.value = 1
    dut.dato_codificador_i.value = dato_codificador
    await FallingEdge(dut.data_available_o)
    assert dut.dato_codificado_o.value == valor_codificado
    dut.pulso_teclas_pi.value = 0


@cocotb.test()
async def Prueba_tecla_9(dut):
    await cocotb.start(generar_reloj_10MHz(dut))
    await reiniciar_modulo(dut)
    await RisingEdge(dut.clk_i)

    dato_codificador = 2
    valor_contador = 0

    valor_concatenado = (valor_contador << 2) | dato_codificador
    valor_binario = f'{valor_concatenado:04b}'
    valor_codificado = mapeo_key_encoding(valor_binario)

    while dut.cuenta_dos_bits_o.value != 1:
        await RisingEdge(dut.clk_i)

    dut.pulso_teclas_pi.value = 1
    dut.dato_codificador_i.value = dato_codificador
    await FallingEdge(dut.data_available_o)
    assert dut.dato_codificado_o.value == valor_codificado
    dut.pulso_teclas_pi.value = 0


@cocotb.test()
async def Prueba_tecla_A(dut):
    await cocotb.start(generar_reloj_10MHz(dut))
    await reiniciar_modulo(dut)
    await RisingEdge(dut.clk_i)

    dato_codificador = 1
    valor_contador = 0

    valor_concatenado = (valor_contador << 2) | dato_codificador
    valor_binario = f'{valor_concatenado:04b}'
    valor_codificado = mapeo_key_encoding(valor_binario)

    while dut.cuenta_dos_bits_o.value != 1:
        await RisingEdge(dut.clk_i)

    dut.pulso_teclas_pi.value = 1
    dut.dato_codificador_i.value = dato_codificador
    await FallingEdge(dut.data_available_o)
    assert dut.dato_codificado_o.value == valor_codificado
    dut.pulso_teclas_pi.value = 0


@cocotb.test()
async def Prueba_tecla_B(dut):
    await cocotb.start(generar_reloj_10MHz(dut))
    await reiniciar_modulo(dut)
    await RisingEdge(dut.clk_i)

    dato_codificador = 1
    valor_contador = 1

    valor_concatenado = (valor_contador << 2) | dato_codificador
    valor_binario = f'{valor_concatenado:04b}'
    valor_codificado = mapeo_key_encoding(valor_binario)

    while dut.cuenta_dos_bits_o.value != 2:
        await RisingEdge(dut.clk_i)

    dut.pulso_teclas_pi.value = 1
    dut.dato_codificador_i.value = dato_codificador
    await FallingEdge(dut.data_available_o)
    assert dut.dato_codificado_o.value == valor_codificado
    dut.pulso_teclas_pi.value = 0


@cocotb.test()
async def Prueba_tecla_C(dut):
    await cocotb.start(generar_reloj_10MHz(dut))
    await reiniciar_modulo(dut)
    await RisingEdge(dut.clk_i)

    dato_codificador = 1
    valor_contador = 2

    valor_concatenado = (valor_contador << 2) | dato_codificador
    valor_binario = f'{valor_concatenado:04b}'
    valor_codificado = mapeo_key_encoding(valor_binario)

    while dut.cuenta_dos_bits_o.value != 3:
        await RisingEdge(dut.clk_i)

    dut.pulso_teclas_pi.value = 1
    dut.dato_codificador_i.value = dato_codificador
    await FallingEdge(dut.data_available_o)
    assert dut.dato_codificado_o.value == valor_codificado
    dut.pulso_teclas_pi.value = 0


@cocotb.test()
async def Prueba_tecla_D(dut):
    await cocotb.start(generar_reloj_10MHz(dut))
    await reiniciar_modulo(dut)
    await RisingEdge(dut.clk_i)

    dato_codificador = 1
    valor_contador = 3

    valor_concatenado = (valor_contador << 2) | dato_codificador
    valor_binario = f'{valor_concatenado:04b}'
    valor_codificado = mapeo_key_encoding(valor_binario)

    while dut.cuenta_dos_bits_o.value != 0:
        await RisingEdge(dut.clk_i)

    dut.pulso_teclas_pi.value = 1
    dut.dato_codificador_i.value = dato_codificador
    await FallingEdge(dut.data_available_o)
    assert dut.dato_codificado_o.value == valor_codificado
    dut.pulso_teclas_pi.value = 0


@cocotb.test()
async def Prueba_tecla_E(dut):
    await cocotb.start(generar_reloj_10MHz(dut))
    await reiniciar_modulo(dut)
    await RisingEdge(dut.clk_i)

    dato_codificador = 2
    valor_contador = 3

    valor_concatenado = (valor_contador << 2) | dato_codificador
    valor_binario = f'{valor_concatenado:04b}'
    valor_codificado = mapeo_key_encoding(valor_binario)

    while dut.cuenta_dos_bits_o.value != 0:
        await RisingEdge(dut.clk_i)

    dut.pulso_teclas_pi.value = 1
    dut.dato_codificador_i.value = dato_codificador
    await FallingEdge(dut.data_available_o)
    assert dut.dato_codificado_o.value == valor_codificado
    dut.pulso_teclas_pi.value = 0


@cocotb.test()
async def Prueba_tecla_F(dut):
    await cocotb.start(generar_reloj_10MHz(dut))
    await reiniciar_modulo(dut)
    await RisingEdge(dut.clk_i)

    dato_codificador = 0
    valor_contador = 3

    valor_concatenado = (valor_contador << 2) | dato_codificador
    valor_binario = f'{valor_concatenado:04b}'
    valor_codificado = mapeo_key_encoding(valor_binario)

    while dut.cuenta_dos_bits_o.value != 0:
        await RisingEdge(dut.clk_i)

    dut.pulso_teclas_pi.value = 1
    dut.dato_codificador_i.value = dato_codificador
    await FallingEdge(dut.data_available_o)
    assert dut.dato_codificado_o.value == valor_codificado
    dut.pulso_teclas_pi.value = 0
 #######################################################################################3 012301230123






