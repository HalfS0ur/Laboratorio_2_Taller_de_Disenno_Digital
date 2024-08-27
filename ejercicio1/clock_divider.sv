`timescale 1ns / 1ps

module clock_divider (
    input  logic clk_i,
    output logic led_o
);

logic [23:0] cuenta = 0; // declare a counter to keep track of time..
logic estado_LED = 0;

always @(posedge clk_i) begin
    if (cuenta == 99) begin //10000000
        estado_LED <= ~estado_LED; // toggle the LED
        cuenta <= 0; // reset the counter
    end
    
    else begin 
        cuenta <= cuenta + 1; // increment the counter
    end
end
  
assign led_o = estado_LED;
    
endmodule