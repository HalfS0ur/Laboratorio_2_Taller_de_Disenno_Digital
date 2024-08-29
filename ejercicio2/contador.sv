`timescale 1ns / 1ps

module contador (
    input logic clk, // clock signal
    input logic reset_i, // synchronous reset input
    input logic boton_i, // previous module output
    output logic [7:0] conta_o // 8-bit count output.
);

    // define internal signals
    logic [7:0] count_reg = 0; // register to hold the count value

    // reset the count value to 0 when the reset input is high.
    always_ff @(posedge clk) begin
        if (reset_i == 1'b1) begin
            count_reg <= 8'b0;
        end else begin
            // increment the count value on every clock cycle when the reset input is low
            count_reg <= boton_i ? count_reg + 1 : count_reg;
        end
    end

    // assign the count value to the output
    assign conta_o = count_reg;

endmodule
