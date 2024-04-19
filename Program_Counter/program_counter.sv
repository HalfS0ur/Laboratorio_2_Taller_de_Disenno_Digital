`timescale 1ns / 1ps

module program_counter #(parameter ANCHO = 16)(
    input   logic             clk_i,
    input   logic [1:0]       pc_op_i,
    input   logic [ANCHO-1:0] pc_i,
    output  logic [ANCHO-1:0] pc_o,
    output  logic [ANCHO-1:0] pcinc_o
    );
    
    logic [ANCHO-1:0] pc_actual = 0;
    logic [ANCHO-1:0] pc_siguiente = 0;
    
    always @(posedge clk_i) begin
        case(pc_op_i)
            'b00: begin
                pc_actual = 0;
                pc_siguiente = 0;
            end
            
            'b01: begin
                pc_actual = pc_actual;
                pc_siguiente = 0;
            end
            
            'b10: begin
                pc_actual = pc_actual + 4;
                pc_siguiente = 0;
            end
            
            'b11: begin
                pc_siguiente = pc_actual + 4;
                pc_actual = pc_i;
            end
        endcase
    end
    
    assign pc_o = pc_actual;
    assign pcinc_o = pc_siguiente;
    
endmodule
