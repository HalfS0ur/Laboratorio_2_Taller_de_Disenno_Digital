`timescale 1ns / 1ps

module top(
    input logic clk_i, //Reloj de 10MHz
    input logic boton_pi,
    input logic reset_pi,
    output logic [7:0]conta_o,
    output logic boton_o
    );
    
    logic boton_debounce_o;
    
    debouncer debounce(
    .clk(clk_i),
    .boton_pi(boton_pi),
    .boton_debounce_o(boton_debounce_o));
    
    sincronizador sync(
    .clk(clk_i),
    .button_i(boton_debounce_o),
    .button_o(boton_o));
    
    contador cuenta(
    .clk(clk_i),
    .reset_i(reset_pi),
    .boton_i(boton_o),
    .conta_o(conta_o)); 

endmodule
