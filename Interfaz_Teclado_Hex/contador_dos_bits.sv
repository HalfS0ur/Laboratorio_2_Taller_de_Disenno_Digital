`timescale 1ns / 1ps

module contador_dos_bits(
    input  logic       clk_i,
    input  logic       reset_i,
    input  logic       inhibit_i,
    
    output logic [1:0] cuenta_o
    );
    
    logic [1:0] cuenta;
    
    always_ff @(posedge clk_i or posedge reset_i) begin
        if (reset_i) begin
            cuenta <= 0;
        end
        
        else if (inhibit_i) begin
            cuenta <= cuenta;
        end
        
        else begin
            cuenta <= cuenta + 1;
        end
        
        if (cuenta == 4) begin
            cuenta <= 0;
        end
    end
    
    assign cuenta_o = cuenta;
    
endmodule
