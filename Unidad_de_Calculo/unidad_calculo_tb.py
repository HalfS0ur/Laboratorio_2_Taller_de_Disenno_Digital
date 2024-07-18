import cocotb
from cocotb.triggers import Timer, RisingEdge
from cocotb.clock import Clock
import random

ciclo_reloj = 100 

@cocotb.coroutine
async def iniciar_reloj(dut, periodo = 100, unidad = 'ns'):
    clock = Clock(dut.clk_i, periodo, unidad)
    await cocotb.start(clock.start())


@cocotb.coroutine
async def reiniciar_modulo(dut):
    dut.reset_i.value = 1
    dut.sw_i.value = 0
    dut.key_detect_i.value = 0
    dut.teclado_i.value = 0
    await Timer (200, units = 'ns')
    dut.reset_i.value = 0


@cocotb.coroutine
async def pulsar_tecla(dut, ciclo1, ciclo2, valor):
    dut.key_detect_i.value = 1
    await Timer(ciclo1*ciclo_reloj, units='ns')
    dut.key_detect_i.value = 0
    dut.teclado_i.value = valor
    await Timer(ciclo2 * ciclo_reloj, units='ns')


@cocotb.test()
async def prueba_funcion_and(dut):
    await iniciar_reloj(dut)
    await (reiniciar_modulo(dut))
    await RisingEdge(dut.clk_i)

    dut.sw_i.value = 0

    for operando_a in range(10):
        for operando_b in range(10):
            await Timer(ciclo_reloj, units='ns')
            await pulsar_tecla(dut, 2, 4, operando_a)
            await pulsar_tecla(dut, 1, 2, 12)
            await pulsar_tecla(dut, 1, 4, operando_b)
            resultado = (operando_a & operando_b) & 0xFFFF
            await pulsar_tecla(dut, 1, 5, 15)
            assert dut.banco_de_registros.rs2.value == resultado, f"Operación AND falló para {operando_a} & {operando_b}, se obtuvo {int(dut.banco_de_registros.rs2.value)}, esperaba {resultado}"
            await Timer(2 * ciclo_reloj, units='ns')


@cocotb.test()
async def prueba_funcion_or(dut):
    await iniciar_reloj(dut)
    await (reiniciar_modulo(dut))
    await RisingEdge(dut.clk_i)

    dut.sw_i.value = 0

    for operando_a in range(10):
        for operando_b in range(10):
            await Timer(ciclo_reloj, units='ns')
            await pulsar_tecla(dut, 2, 4, operando_a)
            await pulsar_tecla(dut, 1, 2, 13)
            await pulsar_tecla(dut, 1, 4, operando_b)
            resultado = (operando_a | operando_b) & 0xFFFF
            await pulsar_tecla(dut, 1, 5, 15)
            assert dut.banco_de_registros.rs2.value == resultado, f"Operación OR falló para {operando_a} | {operando_b}, se obtuvo {int(dut.banco_de_registros.rs2.value)}, esperaba {resultado}"
            await Timer(2 * ciclo_reloj, units='ns')


@cocotb.test()
async def prueba_funcion_suma(dut):
    await iniciar_reloj(dut)
    await (reiniciar_modulo(dut))
    await RisingEdge(dut.clk_i)

    dut.sw_i.value = 0

    for operando_a in range(10):
        for operando_b in range(10):
            await Timer(ciclo_reloj, units='ns')
            await pulsar_tecla(dut, 2, 4, operando_a)
            await pulsar_tecla(dut, 1, 2, 10)
            await pulsar_tecla(dut, 1, 4, operando_b)
            resultado = (operando_a + operando_b) & 0xFFFF
            await pulsar_tecla(dut, 1, 5, 15)
            assert dut.banco_de_registros.rs2.value == resultado, f"Operación suma falló para {operando_a} + {operando_b}, se obtuvo {int(dut.banco_de_registros.rs2.value)}, esperaba {resultado}"
            await Timer(2 * ciclo_reloj, units='ns')


@cocotb.test()
async def prueba_funcion_resta(dut):
    await iniciar_reloj(dut)
    await (reiniciar_modulo(dut))
    await RisingEdge(dut.clk_i)

    dut.sw_i.value = 0

    for operando_a in range(10):
        for operando_b in range(10):
            await Timer(ciclo_reloj, units='ns')
            await pulsar_tecla(dut, 2, 4, operando_a)
            await pulsar_tecla(dut, 1, 2, 11)
            await pulsar_tecla(dut, 1, 4, operando_b)
            resultado = (operando_a - operando_b) & 0xFFFF
            await pulsar_tecla(dut, 1, 5, 15)
            assert dut.banco_de_registros.rs2.value == resultado, f"Operación resta falló para {operando_a} - {operando_b}, se obtuvo {int(dut.banco_de_registros.rs2.value)}, esperaba {resultado}"
            await Timer(2 * ciclo_reloj, units='ns')


@cocotb.test()
async def prueba_funcion_corrimiento(dut):
    await iniciar_reloj(dut)
    await (reiniciar_modulo(dut))
    await RisingEdge(dut.clk_i)

    dut.sw_i.value = 0

    for operando_a in range(10):
        for operando_b in range(10):
            await Timer(ciclo_reloj, units='ns')
            await pulsar_tecla(dut, 2, 4, operando_a)
            await pulsar_tecla(dut, 1, 2, 14)
            await pulsar_tecla(dut, 1, 4, operando_b)
            resultado = (operando_a << operando_b) & 0xFFFF
            await pulsar_tecla(dut, 1, 5, 15)
            assert dut.banco_de_registros.rs2.value == resultado, f"Operación corrimiento falló para {operando_a} << {operando_b}, se obtuvo {int(dut.banco_de_registros.rs2.value)}, esperaba {resultado}"
            await Timer(2 * ciclo_reloj, units='ns')

        
@cocotb.test()
async def prueba_lectura_regfile(dut):
    await iniciar_reloj(dut)
    await (reiniciar_modulo(dut))
    await RisingEdge(dut.clk_i)

    dut.sw_i.value = 0

    regfile = []

    for operacion in range (10):
        operando_a = random.randint(1, 9)
        operando_b = random.randint(1, 9)

        await Timer(ciclo_reloj, units='ns')
        await pulsar_tecla(dut, 2, 4, operando_a)
        await pulsar_tecla(dut, 1, 2, 12)
        await pulsar_tecla(dut, 1, 4, operando_b)
        resultado = (operando_a & operando_b) & 0xFFFF
        regfile.extend([operando_a, operando_b, resultado])
        await pulsar_tecla(dut, 1, 5, 15)
        await Timer(2 * ciclo_reloj, units='ns')

    await Timer(ciclo_reloj, units='ns')

    dut.sw_i.value = 1

    for registro in range(30):
        await Timer(2*ciclo_reloj, units='ns')
        assert dut.banco_de_registros.rs2.value == regfile[registro], f"Operación lectura falló en el registro {registro}, se obtuvo {int(dut.banco_de_registros.rs2.value)}, esperaba {regfile[registro]}"



#estados de interes: 1,4,9,10,13,14,19,20,26


'''@cocotb.test()
async def let_it_run_baby(dut):
    await cocotb.start(generar_reloj_10MHz(dut))
    await (reiniciar_modulo(dut))
    await RisingEdge(dut.clk_i)
    for run in range (32):
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
        dut.teclado_i.value = 11
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
        #print(int(dut.control.estado_o))
        await Timer (200, units = 'ns')
        await Timer (200, units = 'ns')
        await Timer (200, units = 'ns')'''


'''@cocotb.test()
async def prueba_funcion_and(dut):
    await iniciar_reloj(dut)
    await (reiniciar_modulo(dut))
    await RisingEdge(dut.clk_i)

    dut.sw_i.value = 0

    estado = int(dut.control.estado_o)
    print(estado)

    for operando_a in range(10):
        for operando_b in range(10):
            await Timer (ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 1
            await Timer (2*ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 0
            dut.teclado_i.value = operando_a #meter al loop
            await Timer (4*ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 1
            await Timer (ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 0
            dut.teclado_i.value = 12
            await Timer (2*ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 1
            await Timer (ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 0
            dut.teclado_i.value = operando_b #meter al loop
            resultado = (operando_a & operando_b) & 0xFFFF
            #print(resultado)
            await Timer (4*ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 1
            await Timer (ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 0
            dut.teclado_i.value = 15
            await Timer (5*ciclo_reloj, units = 'ns') #tal vez sea 4
            assert dut.banco_de_registros.rs2.value == resultado
            await Timer (2*ciclo_reloj, units = 'ns')
            #print(estados_de_interes)'''