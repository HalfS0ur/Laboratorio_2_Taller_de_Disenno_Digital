`timescale 1ns / 1ps

module reloj_10MHz(
    input logic clk_i,
    output logic LED_po
);

logic [23:0] cuenta; // declare a counter to keep track of time

always @(posedge clk_i) 
    begin
        if (cuenta == 100) //10000000
            begin
                LED_po <= ~LED_po; // toggle the LED
                cuenta <= 0; // reset the counter
            end
        else 
            begin
                cuenta <= cuenta + 1; // increment the counter
            end
    end
endmodule
