`timescale 1ns / 1ps

module top(
    input  logic clk_pi,
    output logic led_po
);

clock_divider clock_divider(
    .clk_i(clk_pi),
    .led_o(led_po)
);

endmodule