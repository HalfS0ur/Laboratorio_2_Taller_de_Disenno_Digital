`timescale 1ns / 1ps

module registro_paralelo(
    input logic        clk_i,
    input logic        reset_i,
    input logic        we_i,
    input logic  [1:0] cuenta_i,
    input logic  [1:0] dato_codificador_i,
    
    output logic [3:0] dato_teclado_o
    );
    
    logic [3:0] dato_teclado = 0;
    
    always_ff @(posedge clk_i or posedge reset_i) begin
        if (reset_i) begin
            dato_teclado <= 0;
        end
        
        else if (we_i) begin
            dato_teclado <= {cuenta_i, dato_codificador_i};
        end
    end
    
    assign dato_teclado_o = dato_teclado;
    
endmodule
