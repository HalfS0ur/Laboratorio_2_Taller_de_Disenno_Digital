`timescale 1ns / 1ps

module sincronizador(
    input logic clk,
    input logic button_i, 
    output logic button_o 
);

    logic button_prev; 

    always_ff @(posedge clk) begin
        button_prev <= button_i;
    end

    always_comb begin
        if (button_prev == 1'b0 && button_i == 1'b1) begin
            button_o = 1'b1; 
        end else begin
            button_o = 1'b0;
        end
    end

endmodule
