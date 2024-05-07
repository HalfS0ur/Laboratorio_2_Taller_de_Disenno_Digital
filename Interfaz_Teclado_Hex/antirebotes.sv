`timescale 1ns / 1ps

module antirebotes (
    input logic clk_i,
    input logic reset_i,
    input logic boton0_pi,
    input logic boton1_pi,
    input logic boton2_pi,
    input logic boton3_pi,
    output logic boton_debounce_o
);

    parameter CUENTA_DB = 5; 

    logic [CUENTA_DB-1:0] cuenta = 0;
    logic [3:0] boton_pasado = 4'b0000;
    logic [3:0] boton_debounceado = 4'b0000; 

    always @(posedge clk_i or posedge reset_i) begin
        if (reset_i) begin
            cuenta <= 0;
            boton_pasado <= 4'b0000;
            boton_debounceado <= 4'b0000;
        end 
        
        else begin
            if (boton0_pi != boton_pasado[0] || boton1_pi != boton_pasado[1] || boton2_pi != boton_pasado[2] || boton3_pi != boton_pasado[3]) begin
                cuenta <= cuenta + 1;
                if (cuenta == (2*CUENTA_DB) - 1) begin
                    boton_pasado <= boton_debounceado;
                    boton_debounceado <= {boton0_pi, boton1_pi, boton2_pi, boton3_pi};
                end
            end else begin
                cuenta <= 0;
                boton_debounceado <= 4'b1111; 
            end
        end
    end

    assign boton_debounce_o = (boton_debounceado != 4'b1111);

endmodule
