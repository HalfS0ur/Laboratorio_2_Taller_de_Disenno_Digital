`timescale 1ns / 1ps

module deteccion_tecla(
    input logic clk_i,
    input logic reset_i,
    input logic [3:0] pulso_teclas_i,
    
    output logic inhibit_o,
    output logic data_available_o
    );
    
    logic boton_db;
    logic boton_sc;    
    logic deteccion = 0;
    
    antirebotes antirebotes(
        .clk_i(clk_i),
        .reset_i(reset_i),
        .boton0_pi(pulso_teclas_i[0]),
        .boton1_pi(pulso_teclas_i[1]),
        .boton2_pi(pulso_teclas_i[2]),
        .boton3_pi(pulso_teclas_i[3]),
        .boton_debounce_o(boton_db)
    );
    
    sincronizador sincronizacion(
        .clk_i(clk_i),
        .boton_i(boton_db),
        .boton_o(boton_sc)
    );
       
    always_comb begin
        if (boton_db == 1 & boton_sc == 1) begin
            deteccion = 1;
        end
        
        else if (deteccion == 1 & boton_db == 1) begin
            deteccion = deteccion;
        end
        
        else if (boton_db == 0 & boton_sc == 0) begin
            deteccion = 0;
        end
    end
       
    assign inhibit_o = deteccion;
    assign data_available_o = boton_sc;
    
endmodule
