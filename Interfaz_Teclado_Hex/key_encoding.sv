`timescale 1ns / 1ps


module key_encoding(
    input logic  [3:0] dato_i,
    output logic [3:0] dato_o
    );
    
    always_comb begin
        begin
            case(dato_i)
                4'b0000: dato_o = 4'b0111; //7  
                4'b0001: dato_o = 4'b1010; //A
                4'b0010: dato_o = 4'b1001; //9
                4'b0011: dato_o = 4'b1000; //8    
                4'b0100: dato_o = 4'b0100; //4    
                4'b0101: dato_o = 4'b1011; //B
                4'b0110: dato_o = 4'b0110; //6 
                4'b0111: dato_o = 4'b0101; //5
                4'b1000: dato_o = 4'b0001; //1
                4'b1001: dato_o = 4'b1100; //C
                4'b1010: dato_o = 4'b0011; //3
                4'b1011: dato_o = 4'b0010; //2
                4'b1100: dato_o = 4'b1111; //F
                4'b1101: dato_o = 4'b1101; //D
                4'b1110: dato_o = 4'b1110; //E
                4'b1111: dato_o = 4'b0000; //0
                default: dato_o = 4'b0000; //0
            endcase
        end
    end    
    
endmodule
