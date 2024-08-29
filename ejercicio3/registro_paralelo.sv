`timescale 1ns / 1ps

module registro_paralelo(
    input logic          clk_i,
    input logic          we_i,
    input logic          reset_i,
    input logic  [15:0]  data_i,
    
    output logic [15:0]  data_o
    );
    
    logic [15:0] data = 0;
    
    always_ff @(posedge clk_i or posedge reset_i) begin
        if (reset_i) begin
            data <= 0;
        end
        
        else if (we_i) begin
            data <= data_i;
        end
    end
    
    assign data_o = data;
endmodule //
