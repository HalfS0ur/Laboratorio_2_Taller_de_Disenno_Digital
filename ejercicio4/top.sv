`timescale 1ns / 1ps

module top #(parameter ANCHO = 16)(
    input   logic             clk_i,
    input   logic [1:0]       pc_op_i,
    input   logic [ANCHO-1:0] pc_i,
    output  logic [ANCHO-1:0] pc_o,
    output  logic [ANCHO-1:0] pcinc_o

);

program_counter #(.ANCHO(ANCHO)) program_counter(
    .clk_i(clk_i),
    .pc_op_i(pc_op_i),
    .pc_i(pc_i),
    .pc_o(pc_o),
    .pcinc_o(pcinc_o)
);

endmodule