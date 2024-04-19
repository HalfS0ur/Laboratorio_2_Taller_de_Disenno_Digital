`timescale 1ns / 1ps

module top(
    input logic clk_in1,
    input logic boton_pi,
    input logic reset_pi,
    output logic [7:0]conta_o,
    output logic boton_o
    );
    
    logic clk_10MHz;
    logic clk_1kHz;
    logic boton_debounce_o;
    logic boton_sync_o;
    
    clk_wiz_0 reloj(
    .clk_10MHz(clk_10MHz),     
    .clk_in1(clk_in1)); 
    
    clock_divider divisor(
    .clk(clk_10MHz),
    .enable_o(clk_1kHz));
    
    debouncer debounce(
    .clk(clk_1kHz),
    .boton_pi(boton_pi),
    .boton_debounce_o(boton_debounce_o));
    
    sincronizador sync(
    .clk(clk_1kHz),
    .button_i(boton_debounce_o),
    .button_o(boton_o));
    
    contador cuenta(
    .clk(clk_1kHz),
    .reset_i(reset_pi),
    .boton_i(boton_o),
    .conta_o(conta_o)); 
endmodule
