`timescale 1ns / 1ps

module registro_available(
    input logic  clk_i,
    input logic  reset_i,
    input logic  data_available_i,
    
    output logic data_available_o
    );
    
    logic data_available = 0;
    
    always_ff @(posedge clk_i or posedge reset_i) begin
        if (reset_i) begin
            data_available <= 0;
        end
        
        else begin
            data_available <= data_available_i;
        end
    end
    
    assign data_available_o = data_available;
    
endmodule
