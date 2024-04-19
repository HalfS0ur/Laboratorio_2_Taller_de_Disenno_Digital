`timescale 1ns / 1ps

module sincronizador(
    input logic clk, // clock signal
    input logic button_i, // synchronized input from previous module
    output logic button_o // synchronized output pulse
);

    // define internal signals
    logic button_prev; // previous synchronized button state

    // synchronize button input to clock
    always_ff @(posedge clk) begin
        button_prev <= button_i;
    end

    // detect button rising edges and generate one-clock-cycle pulse
    always_comb begin
        if (button_prev == 1'b0 && button_i == 1'b1) begin
            button_o = 1'b1; // generate one-clock-cycle pulse on rising edge
        end else begin
            button_o = 1'b0; // output low otherwise
        end
    end

endmodule
