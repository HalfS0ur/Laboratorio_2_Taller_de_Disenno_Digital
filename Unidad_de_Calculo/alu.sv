`timescale 1ns / 1ps

module alu #(
    parameter ANCHO = 16
)(
    input  logic signed [ANCHO-1:0] ALUa_i,
    input  logic signed [ANCHO-1:0] ALUb_i,
    input  logic                    ALUflagin_i,
    input  logic        [3:0]       ALUcontrol_i,
    
    output logic        [ANCHO-1:0] ALUresult_o
);

    always_comb begin
        case(ALUcontrol_i)
             4'b1100: begin //AND bitwise ....
                    ALUresult_o = ALUa_i & ALUb_i;
                  end
                  
             4'b1101: begin //OR bitwise
                    ALUresult_o = ALUa_i | ALUb_i;
                  end
                  
             4'b1010: begin //Suma
                    ALUresult_o = ALUa_i + ALUb_i + ALUflagin_i;
                  end
        
              4'b1011: begin //Resta
                      ALUresult_o = ALUa_i - ALUb_i - ALUflagin_i;
                  end
                 
              4'b1110: begin //Corrimiento a la izquierda            
                      ALUresult_o = ALUa_i << ALUb_i;                    
                  end
        endcase
        
    end
    
endmodule
