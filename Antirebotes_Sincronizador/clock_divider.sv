
`timescale 1ns / 1ps

module clock_divider(
    input logic clk,
    output logic enable_o
    );
    
    logic [15:0] cuenta = 0;
    logic estado = 0;
    
    always_ff @(posedge clk) begin
        cuenta <= cuenta + 1;
        if (cuenta == 10) 
            begin
                estado <= ~estado;
                cuenta <= 0;
            end
    end
    
    assign enable_o = estado;
endmodule
