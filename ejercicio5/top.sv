`timescale 1ns / 1ps

module top
    #(parameter ANCHO = 32,
                PROFUNDIDAD = 5
    )(
    input  logic                   clk_i,
    input  logic                   reset_i,
    input  logic                   we_i,
    input  logic [ANCHO-1:0]       data_in,
    input  logic [PROFUNDIDAD-1:0] addr_rd,
    input  logic [PROFUNDIDAD-1:0] addr_rs1,
    input  logic [PROFUNDIDAD-1:0] addr_rs2,
    output logic [ANCHO-1:0]       rs1,
    output logic [ANCHO-1:0]       rs2
    );

    regfile #(.ANCHO(ANCHO), .PROFUNDIDAD(PROFUNDIDAD)) regfile(
        .clk_i(clk_i),
        .reset_i(reset_i),
        .we_i(we_i),
        .data_in(data_in),
        .addr_rd(addr_rd),
        .addr_rs1(addr_rs1),
        .addr_rs2(addr_rs2),
        .rs1(rs1),
        .rs2(rs2)
    );

endmodule