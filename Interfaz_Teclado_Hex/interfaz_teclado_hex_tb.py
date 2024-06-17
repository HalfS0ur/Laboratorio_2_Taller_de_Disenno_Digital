import cocotb
from cocotb.triggers import Timer, FallingEdge, RisingEdge
from cocotb.clock import Clock

async def iniciar_reloj(dut, periodo = 100, unidad = 'ns'):
    clock = Clock(dut.clk_i, periodo, unidad)
    await cocotb.start(clock.start())

async def reiniciar_modulo(dut):
    dut.reset_i.value = 1
    dut.pulso_teclas_pi.value = 0
    dut.dato_codificador_i.value = 0
    await Timer (200, units = 'ns')
    dut.reset_i.value = 0
    await RisingEdge(dut.clk_i)

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
async def prueba_tecla_0(dut):
    await iniciar_reloj(dut)
    await reiniciar_modulo(dut)

    valor_codificador = 3
    valor_contador = 3

    valor_concatenado = (valor_contador << 2) | valor_codificador
    valor_binario = f'{valor_concatenado:04b}'
    valor_codificado = mapeo_key_encoding(valor_binario)

    hmm = getattr(dut.clock_divider, 'clk_o')
    while dut.cuenta_dos_bits_o.value != valor_contador:
        await FallingEdge(hmm)

    dut.pulso_teclas_pi.value = 1
    dut.dato_codificador_i.value = valor_codificador
    await FallingEdge(dut.data_available_o)
    assert dut.dato_codificado_o.value == valor_codificado

@cocotb.test()
async def prueba_tecla_1(dut):
    await iniciar_reloj(dut)
    await reiniciar_modulo(dut)

    valor_codificador = 0
    valor_contador = 2

    valor_concatenado = (valor_contador << 2) | valor_codificador
    valor_binario = f'{valor_concatenado:04b}'
    valor_codificado = mapeo_key_encoding(valor_binario)

    hmm = getattr(dut.clock_divider, 'clk_o')
    while dut.cuenta_dos_bits_o.value != valor_contador:
        await FallingEdge(hmm)

    dut.pulso_teclas_pi.value = 1
    dut.dato_codificador_i.value = valor_codificador
    await FallingEdge(dut.data_available_o)
    assert dut.dato_codificado_o.value == valor_codificado

@cocotb.test()
async def prueba_tecla_2(dut):
    await iniciar_reloj(dut)
    await reiniciar_modulo(dut)

    valor_codificador = 3
    valor_contador = 2

    valor_concatenado = (valor_contador << 2) | valor_codificador
    valor_binario = f'{valor_concatenado:04b}'
    valor_codificado = mapeo_key_encoding(valor_binario)

    hmm = getattr(dut.clock_divider, 'clk_o')
    while dut.cuenta_dos_bits_o.value != valor_contador:
        await FallingEdge(hmm)

    dut.pulso_teclas_pi.value = 1
    dut.dato_codificador_i.value = valor_codificador
    await FallingEdge(dut.data_available_o)
    assert dut.dato_codificado_o.value == valor_codificado

@cocotb.test()
async def prueba_tecla_3(dut):
    await iniciar_reloj(dut)
    await reiniciar_modulo(dut)

    valor_codificador = 2
    valor_contador = 2

    valor_concatenado = (valor_contador << 2) | valor_codificador
    valor_binario = f'{valor_concatenado:04b}'
    valor_codificado = mapeo_key_encoding(valor_binario)

    hmm = getattr(dut.clock_divider, 'clk_o')
    while dut.cuenta_dos_bits_o.value != valor_contador:
        await FallingEdge(hmm)

    dut.pulso_teclas_pi.value = 1
    dut.dato_codificador_i.value = valor_codificador
    await FallingEdge(dut.data_available_o)
    assert dut.dato_codificado_o.value == valor_codificado

@cocotb.test()
async def prueba_tecla_4(dut):
    await iniciar_reloj(dut)
    await reiniciar_modulo(dut)

    valor_codificador = 0
    valor_contador = 1

    valor_concatenado = (valor_contador << 2) | valor_codificador
    valor_binario = f'{valor_concatenado:04b}'
    valor_codificado = mapeo_key_encoding(valor_binario)

    hmm = getattr(dut.clock_divider, 'clk_o')
    while dut.cuenta_dos_bits_o.value != valor_contador:
        await FallingEdge(hmm)

    dut.pulso_teclas_pi.value = 1
    dut.dato_codificador_i.value = valor_codificador
    await FallingEdge(dut.data_available_o)
    assert dut.dato_codificado_o.value == valor_codificado

@cocotb.test()
async def prueba_tecla_5(dut):
    await iniciar_reloj(dut)
    await reiniciar_modulo(dut)

    valor_codificador = 3
    valor_contador = 1

    valor_concatenado = (valor_contador << 2) | valor_codificador
    valor_binario = f'{valor_concatenado:04b}'
    valor_codificado = mapeo_key_encoding(valor_binario)

    hmm = getattr(dut.clock_divider, 'clk_o')
    while dut.cuenta_dos_bits_o.value != valor_contador:
        await FallingEdge(hmm)

    dut.pulso_teclas_pi.value = 1
    dut.dato_codificador_i.value = valor_codificador
    await FallingEdge(dut.data_available_o)
    assert dut.dato_codificado_o.value == valor_codificado

@cocotb.test()
async def prueba_tecla_6(dut):
    await iniciar_reloj(dut)
    await reiniciar_modulo(dut)

    valor_codificador = 2
    valor_contador = 1

    valor_concatenado = (valor_contador << 2) | valor_codificador
    valor_binario = f'{valor_concatenado:04b}'
    valor_codificado = mapeo_key_encoding(valor_binario)

    hmm = getattr(dut.clock_divider, 'clk_o')
    while dut.cuenta_dos_bits_o.value != valor_contador:
        await FallingEdge(hmm)

    dut.pulso_teclas_pi.value = 1
    dut.dato_codificador_i.value = valor_codificador
    await FallingEdge(dut.data_available_o)
    assert dut.dato_codificado_o.value == valor_codificado

@cocotb.test()
async def prueba_tecla_7(dut):
    await iniciar_reloj(dut)
    await reiniciar_modulo(dut)

    valor_codificador = 0
    valor_contador = 0

    valor_concatenado = (valor_contador << 2) | valor_codificador
    valor_binario = f'{valor_concatenado:04b}'
    valor_codificado = mapeo_key_encoding(valor_binario)

    hmm = getattr(dut.clock_divider, 'clk_o')
    while dut.cuenta_dos_bits_o.value != valor_contador:
        await FallingEdge(hmm)

    dut.pulso_teclas_pi.value = 1
    dut.dato_codificador_i.value = valor_codificador
    await FallingEdge(dut.data_available_o)
    assert dut.dato_codificado_o.value == valor_codificado

@cocotb.test()
async def prueba_tecla_8(dut):
    await iniciar_reloj(dut)
    await reiniciar_modulo(dut)

    valor_codificador = 3
    valor_contador = 0

    valor_concatenado = (valor_contador << 2) | valor_codificador
    valor_binario = f'{valor_concatenado:04b}'
    valor_codificado = mapeo_key_encoding(valor_binario)

    hmm = getattr(dut.clock_divider, 'clk_o')
    while dut.cuenta_dos_bits_o.value != valor_contador:
        await FallingEdge(hmm)

    dut.pulso_teclas_pi.value = 1
    dut.dato_codificador_i.value = valor_codificador
    await FallingEdge(dut.data_available_o)
    assert dut.dato_codificado_o.value == valor_codificado

@cocotb.test()
async def prueba_tecla_9(dut):
    await iniciar_reloj(dut)
    await reiniciar_modulo(dut)

    valor_codificador = 2
    valor_contador = 0

    valor_concatenado = (valor_contador << 2) | valor_codificador
    valor_binario = f'{valor_concatenado:04b}'
    valor_codificado = mapeo_key_encoding(valor_binario)

    hmm = getattr(dut.clock_divider, 'clk_o')
    while dut.cuenta_dos_bits_o.value != valor_contador:
        await FallingEdge(hmm)

    dut.pulso_teclas_pi.value = 1
    dut.dato_codificador_i.value = valor_codificador
    await FallingEdge(dut.data_available_o)
    assert dut.dato_codificado_o.value == valor_codificado

@cocotb.test()
async def prueba_tecla_A(dut):
    await iniciar_reloj(dut)
    await reiniciar_modulo(dut)

    valor_codificador = 1
    valor_contador = 0

    valor_concatenado = (valor_contador << 2) | valor_codificador
    valor_binario = f'{valor_concatenado:04b}'
    valor_codificado = mapeo_key_encoding(valor_binario)

    hmm = getattr(dut.clock_divider, 'clk_o')
    while dut.cuenta_dos_bits_o.value != valor_contador:
        await FallingEdge(hmm)

    dut.pulso_teclas_pi.value = 1
    dut.dato_codificador_i.value = valor_codificador
    await FallingEdge(dut.data_available_o)
    assert dut.dato_codificado_o.value == valor_codificado

@cocotb.test()
async def prueba_tecla_B(dut):
    await iniciar_reloj(dut)
    await reiniciar_modulo(dut)

    valor_codificador = 1
    valor_contador = 1

    valor_concatenado = (valor_contador << 2) | valor_codificador
    valor_binario = f'{valor_concatenado:04b}'
    valor_codificado = mapeo_key_encoding(valor_binario)

    hmm = getattr(dut.clock_divider, 'clk_o')
    while dut.cuenta_dos_bits_o.value != valor_contador:
        await FallingEdge(hmm)

    dut.pulso_teclas_pi.value = 1
    dut.dato_codificador_i.value = valor_codificador
    await FallingEdge(dut.data_available_o)
    assert dut.dato_codificado_o.value == valor_codificado

@cocotb.test()
async def prueba_tecla_C(dut):
    await iniciar_reloj(dut)
    await reiniciar_modulo(dut)

    valor_codificador = 1
    valor_contador = 2

    valor_concatenado = (valor_contador << 2) | valor_codificador
    valor_binario = f'{valor_concatenado:04b}'
    valor_codificado = mapeo_key_encoding(valor_binario)

    hmm = getattr(dut.clock_divider, 'clk_o')
    while dut.cuenta_dos_bits_o.value != valor_contador:
        await FallingEdge(hmm)

    dut.pulso_teclas_pi.value = 1
    dut.dato_codificador_i.value = valor_codificador
    await FallingEdge(dut.data_available_o)
    assert dut.dato_codificado_o.value == valor_codificado

@cocotb.test()
async def prueba_tecla_D(dut):
    await iniciar_reloj(dut)
    await reiniciar_modulo(dut)

    valor_codificador = 1
    valor_contador = 3

    valor_concatenado = (valor_contador << 2) | valor_codificador
    valor_binario = f'{valor_concatenado:04b}'
    valor_codificado = mapeo_key_encoding(valor_binario)

    hmm = getattr(dut.clock_divider, 'clk_o')
    while dut.cuenta_dos_bits_o.value != valor_contador:
        await FallingEdge(hmm)

    dut.pulso_teclas_pi.value = 1
    dut.dato_codificador_i.value = valor_codificador
    await FallingEdge(dut.data_available_o)
    assert dut.dato_codificado_o.value == valor_codificado

@cocotb.test()
async def prueba_tecla_E(dut):
    await iniciar_reloj(dut)
    await reiniciar_modulo(dut)

    valor_codificador = 2
    valor_contador = 3

    valor_concatenado = (valor_contador << 2) | valor_codificador
    valor_binario = f'{valor_concatenado:04b}'
    valor_codificado = mapeo_key_encoding(valor_binario)

    hmm = getattr(dut.clock_divider, 'clk_o')
    while dut.cuenta_dos_bits_o.value != valor_contador:
        await FallingEdge(hmm)

    dut.pulso_teclas_pi.value = 1
    dut.dato_codificador_i.value = valor_codificador
    await FallingEdge(dut.data_available_o)
    assert dut.dato_codificado_o.value == valor_codificado

@cocotb.test()
async def prueba_tecla_F(dut):
    await iniciar_reloj(dut)
    await reiniciar_modulo(dut)

    valor_codificador = 0
    valor_contador = 3

    valor_concatenado = (valor_contador << 2) | valor_codificador
    valor_binario = f'{valor_concatenado:04b}'
    valor_codificado = mapeo_key_encoding(valor_binario)

    hmm = getattr(dut.clock_divider, 'clk_o')
    while dut.cuenta_dos_bits_o.value != valor_contador:
        await FallingEdge(hmm)

    dut.pulso_teclas_pi.value = 1
    dut.dato_codificador_i.value = valor_codificador
    await FallingEdge(dut.data_available_o)
    assert dut.dato_codificado_o.value == valor_codificado






