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
            assert dut.rs1.value == 0, f"El valor de rs1 esperado en el registro 0 es 0, se recibió {dut.rs1.value}"
            assert dut.rs2.value == 0, f"El valor de rs1 esperado en el registro 0 es 0, se recibió {dut.rs2.value}"

        else:
            assert dut.rs1.value == lista_valores[lectura], f"El valor de rs1 esperado es {lista_valores[lectura]}, se recibió {dut.rs1.value}"
            assert dut.rs2.value == lista_valores[lectura], f"El valor de rs1 esperado es {lista_valores[lectura]}, se recibió {dut.rs2.value}"


@cocotb.test()
async def prueba_escritura_intermitente(dut):
    await cocotb.start(generar_reloj_10MHz(dut))
    await (reiniciar_modulo(dut))
    await FallingEdge(dut.clk_i)

    NUMERO_REGISTROS = 2**5
    ANCHO_REGISTROS = 2**32

    estado_we = []
    lista_datos = []
    lista_direcciones = []

    while True:
        we = random.randint(0,1)
        direccion = random.randint(0, (NUMERO_REGISTROS-1))
        dato = random.randint(0, (ANCHO_REGISTROS-1))

        if direccion not in lista_direcciones:
            lista_direcciones.append(direccion)
            lista_datos.append(dato)
            estado_we.append(we)
            dut.data_in.value = dato
            dut.addr_rd.value = direccion
            dut.we_i.value = we
            await FallingEdge(dut.clk_i)

        if len(lista_direcciones) == NUMERO_REGISTROS:
            break
    
    cuenta_rs2 = (len(lista_direcciones) - 1)
    print(estado_we)
    print (cuenta_rs2)

    for verificacion in range (NUMERO_REGISTROS):
        dut.we_i.value = 0
        dut.addr_rs1 = lista_direcciones[verificacion]
        dut.addr_rs2 = lista_direcciones[cuenta_rs2]

        await FallingEdge (dut.clk_i)

        if (estado_we[verificacion] == 0):
            assert dut.rs1.value == 0, f"Error en la iteración {verificacion} No se han escrito datos en este registro, el valor de rs1 esperado es 0, se recibió {dut.rs1.value}"
            
        elif (estado_we[cuenta_rs2] == 0):
            assert dut.rs2.value == 0, f"Error en la iteración {verificacion} No se han escrito datos en este registro, el valor de rs2 esperado es 0, se recibió {dut.rs2.value}"

        elif (lista_direcciones[verificacion] == 0):
            assert dut.rs1.value == 0, f"El valor de rs1 esperado en el registro 0 es 0, se recibió {dut.rs1.value}"
            assert dut.rs2.value == 0, f"El valor de rs1 esperado en el registro 0 es 0, se recibió {dut.rs2.value}"

        else:
            assert dut.rs1.value == lista_datos[verificacion], f"El valor de rs1 esperado es {lista_datos[verificacion]}, se recibió {dut.rs1.value}"
            assert dut.rs2.value == lista_datos[cuenta_rs2], f"El valor de rs2 esperado es {lista_datos[verificacion]}, se recibió {dut.rs2.value}"

        cuenta_rs2 = cuenta_rs2 - 1

@cocotb.test()
async def prueba_reset(dut):
    await cocotb.start(generar_reloj_10MHz(dut))
    await (reiniciar_modulo(dut))
    await FallingEdge(dut.clk_i)

    NUMERO_REGISTROS = 2**5

    for prueba in range (NUMERO_REGISTROS):
        dut.addr_rs1.value = prueba
        dut.addr_rs2.value = prueba

        await FallingEdge(dut.clk_i)

        assert dut.rs1.value == 0, f"El valor de rs1 esperado después de un reinicio es 0, se recibió {dut.rs1.value}"
        assert dut.rs2.value == 0, f"El valor de rs2 esperado después de un reinicio es 0, se recibió {dut.rs2.value}"