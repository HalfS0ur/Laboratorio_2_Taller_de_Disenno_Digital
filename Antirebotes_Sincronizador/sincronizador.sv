`timescale 1ns / 1ps

module sincronizador(
    input logic clk,
    input logic boton_i, 
    output logic boton_o 
);

    logic boton_prev; 

    always_ff @(posedge clk) begin
        boton_prev <= boton_i;
    end

    always_comb begin
        if (boton_prev == 0 && boton_i == 1) begin
            boton_o = 1; 
        end 
        
        else begin
            boton_o = 0;
        end
    end

endmodule
