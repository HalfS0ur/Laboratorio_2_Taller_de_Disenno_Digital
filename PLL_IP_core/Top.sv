`timescale 1ns / 1ps

module Top(
    input logic CLK_100MHZ,
    output logic led_po
    );

    logic clk_10MHz;
    
    clk_wiz_0 reloj(
    .clk_10MHz(clk_10MHz),
    .clk_100MHz(CLK_100MHZ)
    );  
    
    reloj_10MHz prueba(
    .clk_i(clk_10MHz),
    .LED_po(led_po)
    );   
    
endmodule
