import cocotb
from cocotb.triggers import Timer, FallingEdge, RisingEdge

async def generar_reloj_10MHz(dut):
    while True:
        dut.clk_i.value = 1
        await Timer (100, units = 'ns')
        dut.clk_i.value = 0
        await Timer (100, units = 'ns')

async def reiniciar_modulo(dut):
    dut.reset_i.value = 1
    dut.sw_i.value = 0
    dut.key_detect_i.value = 0
    dut.teclado_i.value = 0
    await Timer (200, units = 'ns')
    dut.reset_i.value = 0

ciclo_reloj = 200  

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

@cocotb.test()
async def prueba_funcion_and(dut):
    #estado = int(dut.control.estado_o)
    await cocotb.start(generar_reloj_10MHz(dut))
    await (reiniciar_modulo(dut))
    await RisingEdge(dut.clk_i)

    for operando_a in range(10):
        for operando_b in range(10):
            dut.sw_i.value = 0
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
            #print(int(dut.control.estado_o))

@cocotb.test()
async def prueba_funcion_or(dut):
    #estado = int(dut.control.estado_o)
    await cocotb.start(generar_reloj_10MHz(dut))
    await (reiniciar_modulo(dut))
    await RisingEdge(dut.clk_i)

    for operando_a in range(10):
        for operando_b in range(10):
            dut.sw_i.value = 0
            await Timer (ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 1
            await Timer (2*ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 0
            dut.teclado_i.value = operando_a #meter al loop
            await Timer (4*ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 1
            await Timer (ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 0
            dut.teclado_i.value = 13
            await Timer (2*ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 1
            await Timer (ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 0
            dut.teclado_i.value = operando_b #meter al loop
            resultado = (operando_a | operando_b) & 0xFFFF
            #print(resultado)
            await Timer (4*ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 1
            await Timer (ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 0
            dut.teclado_i.value = 15
            await Timer (5*ciclo_reloj, units = 'ns') #tal vez sea 4
            assert dut.banco_de_registros.rs2.value == resultado
            await Timer (2*ciclo_reloj, units = 'ns')
            #print(int(dut.control.estado_o))

@cocotb.test()
async def prueba_funcion_suma(dut):
    #estado = int(dut.control.estado_o)
    await cocotb.start(generar_reloj_10MHz(dut))
    await (reiniciar_modulo(dut))
    await RisingEdge(dut.clk_i)

    for operando_a in range(10):
        for operando_b in range(10):
            dut.sw_i.value = 0
            await Timer (ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 1
            await Timer (2*ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 0
            dut.teclado_i.value = operando_a #meter al loop
            await Timer (4*ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 1
            await Timer (ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 0
            dut.teclado_i.value = 10
            await Timer (2*ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 1
            await Timer (ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 0
            dut.teclado_i.value = operando_b #meter al loop
            resultado = (operando_a + operando_b) & 0xFFFF
            #print(resultado)
            await Timer (4*ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 1
            await Timer (ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 0
            dut.teclado_i.value = 15
            await Timer (5*ciclo_reloj, units = 'ns') #tal vez sea 4
            assert dut.banco_de_registros.rs2.value == resultado
            await Timer (2*ciclo_reloj, units = 'ns')
            #print(int(dut.control.estado_o))

@cocotb.test()
async def prueba_funcion_resta(dut):
    #estado = int(dut.control.estado_o)
    await cocotb.start(generar_reloj_10MHz(dut))
    await (reiniciar_modulo(dut))
    await RisingEdge(dut.clk_i)

    for operando_a in range(10):
        for operando_b in range(10):
            dut.sw_i.value = 0
            await Timer (ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 1
            await Timer (2*ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 0
            dut.teclado_i.value = operando_a #meter al loop
            await Timer (4*ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 1
            await Timer (ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 0
            dut.teclado_i.value = 11
            await Timer (2*ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 1
            await Timer (ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 0
            dut.teclado_i.value = operando_b #meter al loop
            resultado = (operando_a - operando_b) & 0xFFFF
            #print(resultado)
            await Timer (4*ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 1
            await Timer (ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 0
            dut.teclado_i.value = 15
            await Timer (5*ciclo_reloj, units = 'ns') #tal vez sea 4
            assert dut.banco_de_registros.rs2.value == resultado
            await Timer (2*ciclo_reloj, units = 'ns')
            #print(int(dut.control.estado_o))

@cocotb.test()
async def prueba_funcion_corrimiento(dut):
    #estado = int(dut.control.estado_o)
    await cocotb.start(generar_reloj_10MHz(dut))
    await (reiniciar_modulo(dut))
    await RisingEdge(dut.clk_i)

    for operando_a in range(10):
        for operando_b in range(10):
            dut.sw_i.value = 0
            await Timer (ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 1
            await Timer (2*ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 0
            dut.teclado_i.value = operando_a #meter al loop
            await Timer (4*ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 1
            await Timer (ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 0
            dut.teclado_i.value = 14
            await Timer (2*ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 1
            await Timer (ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 0
            dut.teclado_i.value = operando_b #meter al loop
            resultado = (operando_a << operando_b) & 0xFFFF
            #print(resultado)
            await Timer (4*ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 1
            await Timer (ciclo_reloj, units = 'ns')
            dut.key_detect_i.value = 0
            dut.teclado_i.value = 15
            await Timer (5*ciclo_reloj, units = 'ns') #tal vez sea 4
            assert dut.banco_de_registros.rs2.value == resultado
            await Timer (2*ciclo_reloj, units = 'ns')
            #print(int(dut.control.estado_o))