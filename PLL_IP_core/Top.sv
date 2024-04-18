`timescale 1ns / 1ps

module Top(
    input logic CLK_100MHZ,
    output logic led_po
    );
    logic clk_100MHz;
    logic clk_10MHz;
    logic led;
    
  clk_wiz_0 reloj
   (
    // Clock out ports
    .clk_10MHz(clk_10MHz),     // output clk_10MHz
   // Clock in ports
    .clk_100MHz(CLK_100MHZ));      // input clk_100MHz
    
    reloj_10MHz prueba(
    .clk_i(clk_10MHz),
    .LED_po(led_po)
    );   
    
endmodule
