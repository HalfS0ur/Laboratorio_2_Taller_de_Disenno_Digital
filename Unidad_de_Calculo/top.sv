`timescale 1ns / 1ps

module top(
    input logic clk_i,
    input logic reset_i,
    input logic sw_i,
    
    output logic [15:0] led_o
    );
    
    logic seleccion_mux;
    logic we_regfile;
    logic alu_flag;
    logic [3:0] alu_control;
    logic [4:0] addr_rd;
    logic [4:0] addr_rs1;
    logic [4:0] addr_rs2;
    logic [15:0] data_in;
    logic [15:0] rs1;
    logic [15:0] rs2;
    logic [15:0] alu_result;
    
    fsm_control control(
        .clk_i(clk_i),         
        .rst_i(reset_i),         
        .teclado_i(),      
        .key_detect_i(),   
        .sw_i(sw_i),                                
        .mux_o(seleccion_mux),          
        .addr_rs1_o(addr_rs1),     
        .addr_rs2_o(addr_rs2),     
        .addr_rd_o(addr_rd),      
        .we_o(we_regfile),           
        .alucont_o(alu_control),      
        .flag_in(alu_flag),        
        .led_o(led_o),          
        .we_7seg_o()      
    );
    
    mux_2_1 mux_2_1(
        .seleccion_i(seleccion_mux),
        .entrada0_i(), 
        .entrada1_i(alu_result), 
        .salida_o(data_in)    
    );
    
    banco_de_registros banco_de_registros(
        .clk_i(clk_i),     
        .reset_i(reset_i),   
        .we_i(we_regfile),      
        .data_in(data_in),   
        .addr_rd(addr_rd),   
        .addr_rs1(addr_rs1),  
        .addr_rs2(addr_rs2),                     
        .rs1(rs1),       
        .rs2(rs2)        
    );
    
    alu alu(
        .ALUa_i(rs1),       
        .ALUb_i(rs2),       
        .ALUflagin_i(alu_flag),  
        .ALUcontrol_i(alu_control),                     
        .ALUresult_o(alu_result)   
    );
    
endmodule
