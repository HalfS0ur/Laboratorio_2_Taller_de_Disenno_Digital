import cocotb
from cocotb.triggers import Timer, FallingEdge, RisingEdge

import random

async def generar_reloj_10MHz(dut):
    while True:
        dut.clk_i.value = 0
        await Timer (100, units = 'ns')
        dut.clk_i.value = 1
        await Timer (100, units = 'ns')

async def reiniciar_modulo(dut):
    dut.reset_i.value = 1
    dut.we_i.value = 0
    dut.data_in.value = 0
    dut.addr_rd.value = 0
    dut.addr_rs1.value = 0
    dut.addr_rs2.value = 0
    await Timer (400, units = 'ns')
    dut.reset_i.value = 0


@cocotb.test()
async def prueba_escritura_secuencial(dut):
    await (reiniciar_modulo(dut))

    NUMERO_REGISTROS = 2**5
    
    for escritura in range (NUMERO_REGISTROS):
        await cocotb.start(generar_reloj_10MHz(dut))

        dut.we_i.value = 1
        dut.data_in.value = escritura
        dut.addr_rd.value = escritura

        await FallingEdge(dut.clk_i)

    for dato in range (NUMERO_REGISTROS):
        dut.we_i.value = 0
        dut.addr_rs1.value = dato
        dut.addr_rs2.value = dato

        await FallingEdge(dut.clk_i)

        assert dut.rs1.value == dato, f"El valor de rs1 esperado es {dato}, se recibió {dut.rs1.value}"
        assert dut.rs2.value == dato, f"El valor de rs1 esperado es {dato}, se recibió {dut.rs2.value}"

@cocotb.test()
async def prueba_escritura_aleatoria(dut):
    await cocotb.start(generar_reloj_10MHz(dut))
    await (reiniciar_modulo(dut))
    await FallingEdge(dut.clk_i)

    NUMERO_REGISTROS = 2**5
    ANCHO_REGISTROS = 2**32

    lista_valores = []
    lista_direcciones = []

    while True:
        dut.we_i.value = 1

        direccion = random.randint(0, (NUMERO_REGISTROS-1))
        dato = random.randint(0, (ANCHO_REGISTROS-1))

        if direccion not in lista_direcciones:
            lista_direcciones.append(direccion)
            lista_valores.append(dato)
            dut.data_in.value = dato
            dut.addr_rd.value = direccion
            await FallingEdge(dut.clk_i)

        if len(lista_direcciones) == NUMERO_REGISTROS:
            break

    for lectura in range (NUMERO_REGISTROS):
        dut.we_i.value = 0
        dut.addr_rd.value = 0
        dut.data_in.value = 0

        dut.addr_rs1.value = lista_direcciones[lectura]
        dut.addr_rs2.value = lista_direcciones[lectura]

        await FallingEdge(dut.clk_i)

        if lista_direcciones[lectura] == 0:
            assert dut.rs1.value == 0, f"El valor de rs1 esperado en el registro 0 es {lista_valores[lectura]}, se recibió {dut.rs1.value}"
            assert dut.rs2.value == 0, f"El valor de rs1 esperado en el registro 0 es {lista_valores[lectura]}, se recibió {dut.rs2.value}"

        else:
            assert dut.rs1.value == lista_valores[lectura], f"El valor de rs1 esperado es {lista_valores[lectura]}, se recibió {dut.rs1.value}"
            assert dut.rs2.value == lista_valores[lectura], f"El valor de rs1 esperado es {lista_valores[lectura]}, se recibió {dut.rs2.value}"

