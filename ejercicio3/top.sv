`timescale 1ns / 1ps

module top(
    input  logic        clk_i,
    input  logic        reset_i,
    input  logic        we_i,
    input  logic [15:0] data_i, 
    
    output logic [3:0]  an_o,
    output logic [6:0]  seg_o
    );
    
    logic [15:0] data_o;
    
    registro_paralelo registro_paralelo(
    .clk_i(clk_i),  
    .we_i(we_i),    
    .reset_i(reset_i),  
    .data_i(data_i),   
    .data_o(data_o)   
);

    display_7_segmentos display_7_segmentos(
    .clk_i(clk_i),   
    .reset_i(reset_i), 
    .dato_i(data_o),  
    .an_o(an_o),    
    .seg_o(seg_o)   
);

endmodule
