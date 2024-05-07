`timescale 1ns / 1ps

module top(
    input logic clk_i,
    input logic reset_i,
    input logic [3:0] pulso_teclas_pi,
    input logic [1:0] dato_codificador_i,
    
    output logic data_available_o,
    output logic [1:0] cuenta_dos_bits_o,
    output logic [3:0] dato_codificado_o
);
   
   logic inhibit_contador;
   logic data_available;
   logic [3:0] dato_teclado;
   
   contador_dos_bits contador(
       .clk_i(clk_i),
       .reset_i(reset_i),
       .inhibit_i(data_available),
       .cuenta_o(cuenta_dos_bits_o)
   );
   
   deteccion_tecla deteccion_tecla(
       .clk_i(clk_i),
       .pulso_teclas_i(pulso_teclas_pi),
       .inhibit_o(inhibit_contador),
       .data_available_o(data_available)
   ); 
   
   registro_paralelo registro_datos(
       .clk_i(clk_i),
       .reset_i(reset_i),
       .we_i(data_available),
       .cuenta_i(cuenta_dos_bits_o),
       .dato_codificador_i(dato_codificador_i),
       .dato_teclado_o(dato_teclado)
   );
   
   key_encoding codificador_datos(
       .dato_i(dato_teclado),
       .dato_o(dato_codificado_o)
   );
   
   registro_available registro_data_available(
       .clk_i(clk_i),
       .reset_i(reset_i),
       .data_available_i(data_available),
       .data_available_o(data_available_o)
   );
endmodule
