`timescale 1ns / 1ps

module top(
    input logic clk_i,
    input logic boton_pi,
    input logic reset_pi,
    output logic [7:0]conta_o
    );
    
    logic boton_debounce;
    logic boton_sync;
    
    debouncer debounce(
    .clk(clk_i),
    .boton_pi(boton_pi),
    .boton_debounce_o(boton_debounce));
    
    sincronizador sync(
    .clk(clk_i),
    .boton_i(boton_debounce),
    .boton_o(boton_sync));
    
    contador cuenta(
    .clk(clk_i),
    .reset_i(reset_pi),
    .boton_i(boton_sync),
    .conta_o(conta_o)); 

endmodule
