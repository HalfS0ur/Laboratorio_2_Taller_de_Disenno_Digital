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
        '0000': int('0001', 2),  # 1
        '0001': int('0010', 2),  # 2
        '0010': int('0011', 2),  # 3
        '0011': int('1010', 2),  # A
        '0100': int('0100', 2),  # 4
        '0101': int('0101', 2),  # 5
        '0110': int('0110', 2),  # 6
        '0111': int('1011', 2),  # B
        '1000': int('0111', 2),  # 7
        '1001': int('1000', 2),  # 8
        '1010': int('1001', 2),  # 9
        '1011': int('1100', 2),  # C
        '1100': int('1111', 2),  # F
        '1101': int('0000', 2),  # 0
        '1110': int('1110', 2),  # E
        '1111': int('1101', 2)   # D
    }
        return mapeo.get(valor_teclado, int('1111', 2))


@cocotb.test()
async def prueba_16_teclas(dut):
    await iniciar_reloj(dut)
    await reiniciar_modulo(dut)

    for test in range(8):
        for codificador in range(4):
            for contador in range(4):
                valor_tecla = f'{((contador << 2)|codificador):04b}'
                valor_codificado = mapeo_key_encoding(valor_tecla)

                while dut.cuenta_dos_bits_o.value != contador:
                    await FallingEdge(dut.clk_i)

                dut.pulso_teclas_pi.value = 1
                dut.dato_codificador_i.value = codificador

                await FallingEdge(dut.data_available_o)
                assert dut.dato_codificado_o.value == valor_codificado, f"La tecla presionada es {valor_codificado}, se recibió {dut.dato_codificado_o.value}"
                
                dut.pulso_teclas_pi.value = 0