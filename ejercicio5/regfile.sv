`timescale 1ns / 1ps

module regfile
    #(parameter ANCHO = 32, 
                PROFUNDIDAD = 5
    )(
    input  logic             clk_i,
    input  logic             reset_i,
    input  logic             we_i,
    input  logic [ANCHO-1:0] data_in,
    input  logic [PROFUNDIDAD-1:0] addr_rd,
    input  logic [PROFUNDIDAD-1:0] addr_rs1,
    input  logic [PROFUNDIDAD-1:0] addr_rs2,
    
    output logic [ANCHO-1:0] rs1,
    output logic [ANCHO-1:0] rs2
    );
    
    logic [31:0] rf [31:0];
    
    always_ff @(negedge clk_i or posedge reset_i) begin
        if (reset_i) begin
            for (int i = 0; i<32; i++) begin
                rf[i] <= 0; //..
            end
        end
        
        else if(we_i) begin
            rf [addr_rd] <= data_in;
        end
    end
    
    assign rs1 = (addr_rs1 != 0) ? rf[addr_rs1] : 0;
    assign rs2 = (addr_rs2 != 0) ? rf[addr_rs2] : 0;
    
endmodule
