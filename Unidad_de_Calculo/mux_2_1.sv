`timescale 1ns / 1ps

module mux_2_1 #(
    parameter int ANCHO = 16
)(
    input  logic             seleccion_i,
    input  logic [ANCHO-1:0] entrada0_i,
    input  logic [ANCHO-1:0] entrada1_i,  
    output logic [ANCHO-1:0] salida_o
    );
    
    always_comb begin 
        case (seleccion_i)
            0: salida_o = entrada0_i;
            1: salida_o = entrada1_i;
        endcase
    end
endmodule
