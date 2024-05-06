`timescale 1ns / 1ps

module fsm_control(
    input logic            clk_i,
    input logic            rst_i,
    input logic [3:0]      teclado_i,
    input logic            key_detect_i,
    input logic            sw_i,
    
    output logic           mux_o,
    output logic [4:0]     addr_rs1_o,
    output logic [4:0]     addr_rs2_o,
    output logic [4:0]     addr_rd_o,
    output logic           we_o,
    output logic [3:0]     alucont_o,
    output logic           flag_in,
    output logic [15:0]    led_o, 
    output logic           we_7seg_o
        
    );
    
    logic [4:0] dir_1 = 5'b00000;
    logic [4:0] dir_2 = 5'b00000;
    logic [3:0] opr   = 4'b0000;       
    
    typedef enum 
        {
            inicio,
            sel_modo,
            esp_dato_1,
            leer_regfile,
            rec_dato_1,
            dato_1_inv,
            grd_dato_1,
            leer_dato_1,
            most_dato_1,
            esp_opr,
            rec_opr,
            most_opr,
            opr_inv,
            esp_dato_2,
            rec_dato_2,
            grd_dato_2,
            dato_2_inv,
            leer_dato_2,
            most_dato_2,
            esp_ent,
            rec_ent,
            ent_inv,
            leer_datos,
            opera_datos,
            grd_res,
            leer_res,
            most_res,
            esp_modo,
            most_regfile   
        } state_t;
        
    state_t state_reg, state_next;
    
    always_ff @ (posedge clk_i , posedge rst_i)
        if (rst_i)
            state_reg <= inicio;
        else
            state_reg <= state_next;
            
    always_comb begin
        state_next = state_reg;
        
        unique case (state_reg)
            inicio: begin
                mux_o       =  1'b0;
                dir_1       =  5'b00001;
                dir_2       =  5'b00000;
                opr         =  4'b0000;
                addr_rs1_o  =  5'b00000;
                addr_rs2_o  =  5'b00000;
                addr_rd_o   =  5'b00000;
                we_o        =  1'b0;
                alucont_o   =  4'b0000;
                flag_in     =  1'b0;
                led_o       =  16'b1111100000000000;
                we_7seg_o   =  1'b0;
 
                state_next = sel_modo; 
                
            end
            
            sel_modo: begin
                mux_o       =  1'b0;
                dir_1       =  dir_1 + 5'b00011;
                dir_2       =  dir_2;
                opr         =  4'b0000;
                addr_rs1_o  =  dir_2;
                addr_rs2_o  =  dir_1;
                addr_rd_o   =  5'b00000;
                we_o        =  1'b0;
                alucont_o   =  4'b0000;
                flag_in     =  1'b0;
                led_o       =  16'b1111100000000000;
                we_7seg_o   =  1'b1;
                
                if (sw_i == 1'b0) begin
                    state_next = esp_dato_1;
                end
                
                else if (sw_i == 1'b1) begin
                    state_next = leer_regfile;
                end 
                       
            end
            
            
            
            
            esp_dato_1: begin
                mux_o       =  1'b0;
                dir_1       =  dir_1;
                dir_2       =  dir_2;
                opr         =  4'b0000;
                addr_rs1_o  =  5'b00000;
                addr_rs2_o  =  5'b00000;
                addr_rd_o   =  5'b00000;
                we_o        =  1'b0;
                alucont_o   =  4'b0000;
                flag_in     =  1'b0;
                led_o       =  16'b1110100000000000;
                we_7seg_o   =  1'b0;
            
            
                if (key_detect_i) begin
                    state_next = rec_dato_1;
                end
                
                else begin
                    state_next = esp_dato_1;
                end
            end
            
            rec_dato_1: begin
                mux_o       =  1'b0;
                dir_1       =  dir_1;
                dir_2       =  dir_2;
                opr         =  4'b0000;
                addr_rs1_o  =  5'b00000;
                addr_rs2_o  =  5'b00000;
                addr_rd_o   =  5'b00000;
                we_o        =  1'b0;
                alucont_o   =  4'b0000;
                flag_in     =  1'b0;
                led_o       =  16'b1110100000000000;
                we_7seg_o   =  1'b0;
                 
                if (teclado_i < 4'b1010) begin
                    state_next = grd_dato_1;
                end
                
                else begin
                    state_next = dato_1_inv;
                end
            end
            
            dato_1_inv: begin
                mux_o       =  1'b0;
                dir_1       =  dir_1;
                dir_2       =  dir_2;
                opr         =  4'b0000;
                addr_rs1_o  =  5'b00000;
                addr_rs2_o  =  5'b00000;
                addr_rd_o   =  5'b00000;
                we_o        =  1'b0;
                alucont_o   =  4'b0000;
                flag_in     =  1'b0;
                led_o       =  16'b1110100000000001;
                we_7seg_o   =  1'b0;
            
                state_next = esp_dato_1;
            end
            
            grd_dato_1:  begin
                mux_o       =  1'b0;
                dir_1       =  dir_1;
                dir_2       =  dir_2;
                opr         =  4'b0000;
                addr_rs1_o  =  5'b00000;
                addr_rs2_o  =  5'b00000;
                addr_rd_o   =  dir_1;
                we_o        =  1'b1;
                alucont_o   =  4'b0000;
                flag_in     =  1'b0;
                led_o       =  16'b1110100000000000;
                we_7seg_o   =  1'b0;
            
                state_next = leer_dato_1;
            end
            
            leer_dato_1: begin
                mux_o       =  1'b0;
                dir_1       =  dir_1;
                dir_2       =  dir_2;
                opr         =  4'b0000;
                addr_rs1_o  =  dir_1;
                addr_rs2_o  =  5'b00000;
                addr_rd_o   =  dir_1;
                we_o        =  1'b0;
                alucont_o   =  4'b0000;
                flag_in     =  1'b0;
                led_o       =  16'b1110100000000000;
                we_7seg_o   =  1'b0;
            
                state_next = most_dato_1;
            end
            
            most_dato_1: begin
                mux_o       =  1'b0;
                dir_1       =  dir_1;
                dir_2       =  dir_2;
                opr         =  4'b0000;
                addr_rs1_o  =  dir_1;
                addr_rs2_o  =  5'b00000;
                addr_rd_o   =  dir_1;
                we_o        =  1'b0;
                alucont_o   =  4'b0000;
                flag_in     =  1'b0;
                led_o       =  16'b1110100000000000;
                we_7seg_o   =  1'b1;
            
                state_next = esp_opr;
            end
            
            esp_opr: begin
                mux_o       =  1'b0;
                dir_1       =  dir_1;
                dir_2       =  dir_2;
                opr         =  4'b0000;
                addr_rs1_o  =  dir_1;
                addr_rs2_o  =  5'b00000;
                addr_rd_o   =  dir_1;
                we_o        =  1'b0;
                alucont_o   =  4'b0000;
                flag_in     =  1'b0;
                led_o       =  16'b1101100000000000;
                we_7seg_o   =  1'b0;
            
                if (key_detect_i) begin
                    state_next = rec_opr;
                end
                
                else begin
                    state_next = esp_opr;
                end
            end
            
            rec_opr: begin
                mux_o       =  1'b0;
                dir_1       =  dir_1;
                dir_2       =  dir_2;
                opr         =  teclado_i;
                addr_rs1_o  =  dir_1;
                addr_rs2_o  =  5'b00000;
                addr_rd_o   =  dir_1;
                we_o        =  1'b0;
                alucont_o   =  opr;
                flag_in     =  1'b0;
                led_o[10:0] =  {alucont_o,7'b0000000};
                we_7seg_o   =  1'b0;
            
                if (teclado_i > 4'b1001) begin
                    if (teclado_i < 4'b1111) begin
                        state_next = most_opr;
                    end
                    
                    else begin
                        state_next = opr_inv;
                    end
                end
                
                else begin
                    state_next = opr_inv;    
                end
            end
            
            opr_inv: begin
                mux_o       =  1'b0;
                dir_1       =  dir_1;
                dir_2       =  dir_2;
                opr         =  teclado_i;
                addr_rs1_o  =  dir_1;
                addr_rs2_o  =  5'b00000;
                addr_rd_o   =  dir_1;
                we_o        =  1'b0;
                alucont_o   =  opr;
                flag_in     =  1'b0;
                led_o[10:0] =  {alucont_o,7'b0000001};
                we_7seg_o   =  1'b0;
            
                state_next = esp_opr;
            end
            
            most_opr: begin 
                mux_o       =  1'b0;
                dir_1       =  dir_1;
                dir_2       =  dir_2;
                opr         =  teclado_i;
                addr_rs1_o  =  dir_1;
                addr_rs2_o  =  5'b00000;
                addr_rd_o   =  dir_1;
                we_o        =  1'b0;
                alucont_o   =  opr;
                flag_in     =  1'b0;
                led_o[10:0] =  {alucont_o,7'b0000000};
                we_7seg_o   =  1'b0;
             
                state_next = esp_dato_2;
            end
            
            esp_dato_2: begin
                mux_o       =  1'b0;
                dir_1       =  dir_1;
                dir_2       =  dir_2;
                opr         =  opr;
                addr_rs1_o  =  dir_1;
                addr_rs2_o  =  5'b00000;
                addr_rd_o   =  dir_1;
                we_o        =  1'b0;
                alucont_o   =  opr;
                flag_in     =  1'b0;
                led_o       =  {5'b10111,alucont_o,7'b0000000};
                we_7seg_o   =  1'b0;
            
                if (key_detect_i) begin
                    state_next = rec_dato_2;
                end
                
                else begin
                    state_next = esp_dato_2;
                end
                
            end
            
            rec_dato_2: begin
                mux_o       =  1'b0;
                dir_1       =  dir_1;
                dir_2       =  dir_2;
                opr         =  opr;
                addr_rs1_o  =  dir_1;
                addr_rs2_o  =  5'b00000;
                addr_rd_o   =  dir_1;
                we_o        =  1'b0;
                alucont_o   =  opr;
                flag_in     =  1'b0;
                led_o       =  {5'b10111,alucont_o,7'b0000000};
                we_7seg_o   =  1'b0;
            
                if (teclado_i < 4'b1010) begin
                    state_next = grd_dato_2;
                end
                
                else begin
                    state_next = dato_2_inv;
                end   
            end
            
            dato_2_inv: begin
                mux_o       =  1'b0;
                dir_1       =  dir_1;
                dir_2       =  dir_2;
                opr         =  opr;
                addr_rs1_o  =  dir_1;
                addr_rs2_o  =  5'b00000;
                addr_rd_o   =  dir_1;
                we_o        =  1'b0;
                alucont_o   =  4'b0000;
                flag_in     =  1'b0;
                led_o       =  {5'b10111,alucont_o,7'b0000001};
                we_7seg_o   =  1'b0;
            
                state_next = esp_dato_2;      
            end
            
            grd_dato_2: begin
                mux_o       =  1'b0;
                dir_1       =  dir_1;
                dir_2       =  dir_2;
                opr         =  opr;
                addr_rs1_o  =  dir_1;
                addr_rs2_o  =  5'b00000;
                addr_rd_o   =  dir_1 + 5'b00001;
                we_o        =  1'b1;
                alucont_o   =  opr;
                flag_in     =  1'b0;
                led_o       =  {5'b10111,alucont_o,7'b0000000};
                we_7seg_o   =  1'b0;
            
                state_next = leer_dato_2;
            end
            
            leer_dato_2: begin
                mux_o       =  1'b0;
                dir_1       =  dir_1;
                dir_2       =  dir_2;
                opr         =  opr;
                addr_rs1_o  =  dir_1 + 5'b00001;
                addr_rs2_o  =  5'b00000;
                addr_rd_o   =  dir_1 + 5'b00001;
                we_o        =  1'b0;
                alucont_o   =  opr;
                flag_in     =  1'b0;
                led_o       =  {5'b10111,alucont_o,7'b0000000};
                we_7seg_o   =  1'b0;
            
                state_next = most_dato_2;
            end
            
            most_dato_2: begin
                mux_o       =  1'b0;
                dir_1       =  dir_1;
                dir_2       =  dir_2;
                opr         =  opr;
                addr_rs1_o  =  dir_1 + 5'b00001;
                addr_rs2_o  =  5'b00000;
                addr_rd_o   =  dir_1 + 5'b00001;
                we_o        =  1'b0;
                alucont_o   =  opr;
                flag_in     =  1'b0;
                led_o       =  {5'b10111,alucont_o,7'b0000000};
                we_7seg_o   =  1'b1;
            
                state_next = esp_ent;
            end
            
            esp_ent: begin
                mux_o       =  1'b0;
                dir_1       =  dir_1;
                dir_2       =  dir_2;
                opr         =  opr;
                addr_rs1_o  =  dir_1 + 5'b00001;
                addr_rs2_o  =  5'b00000;
                addr_rd_o   =  dir_1 + 5'b00001;
                we_o        =  1'b0;
                alucont_o   =  opr;
                flag_in     =  1'b0;
                led_o       =  {5'b10001,alucont_o,7'b0000000};
                we_7seg_o   =  1'b0;
            
                if (key_detect_i) begin
                    state_next = rec_ent;
                end
                
                else begin
                    state_next = esp_ent;
                end    
            end
            
            rec_ent: begin
                mux_o       =  1'b0;
                dir_1       =  dir_1;
                dir_2       =  dir_2;
                opr         =  opr;
                addr_rs1_o  =  dir_1 + 5'b00001;
                addr_rs2_o  =  5'b00000;
                addr_rd_o   =  dir_1 + 5'b00001;
                we_o        =  1'b0;
                alucont_o   =  opr;
                flag_in     =  1'b0;
                led_o       =  {5'b10001,alucont_o,7'b0000000};
                we_7seg_o   =  1'b0;
            
                if (teclado_i == 4'b1111) begin
                    state_next = leer_datos;
                end
                
                else begin
                    state_next = ent_inv;
                end    
            end
            
            ent_inv: begin
                mux_o       =  1'b0;
                dir_1       =  dir_1;
                dir_2       =  dir_2;
                opr         =  opr;
                addr_rs1_o  =  dir_1 + 5'b00001;
                addr_rs2_o  =  5'b00000;
                addr_rd_o   =  dir_1 + 5'b00001;
                we_o        =  1'b0;
                alucont_o   =  opr;
                flag_in     =  1'b0;
                led_o       =  {5'b10001,alucont_o,7'b0000001};
                we_7seg_o   =  1'b0;
            
                state_next = esp_ent;     
            end
            
            leer_datos: begin
                mux_o       =  1'b0;
                dir_1       =  dir_1;
                dir_2       =  dir_2;
                opr         =  opr;
                addr_rs1_o  =  dir_1;
                addr_rs2_o  =  dir_1 + 5'b00001;
                addr_rd_o   =  dir_1 + 5'b00001;
                we_o        =  1'b0;
                alucont_o   =  opr;
                flag_in     =  1'b0;
                led_o       =  {5'b10001,alucont_o,7'b0000001};
                we_7seg_o   =  1'b0;
            
                state_next = opera_datos;
                
            end
            
            opera_datos: begin
                mux_o       =  1'b1;
                dir_1       =  dir_1;
                dir_2       =  dir_2;
                opr         =  opr;
                addr_rs1_o  =  dir_1;
                addr_rs2_o  =  dir_1 + 5'b00001;
                addr_rd_o   =  dir_1 + 5'b00001;
                we_o        =  1'b0;
                alucont_o   =  opr;
                flag_in     =  1'b0;
                led_o       =  {5'b10001,alucont_o,7'b0000001};
                we_7seg_o   =  1'b0;
            
                state_next = grd_res;    
            end
            
            grd_res: begin
                mux_o       =  1'b1;
                dir_1       =  dir_1;
                dir_2       =  dir_2;
                opr         =  opr;
                addr_rs1_o  =  dir_1;
                addr_rs2_o  =  dir_1 + 5'b00001;
                addr_rd_o   =  dir_1 + 5'b00010;
                we_o        =  1'b1;
                alucont_o   =  opr;
                flag_in     =  1'b0;
                led_o       =  {5'b10001,alucont_o,7'b0000001};
                we_7seg_o   =  1'b0;
            
                state_next = leer_res;
            end
            
            leer_res: begin
                mux_o       =  1'b1;
                dir_1       =  dir_1;
                dir_2       =  dir_2;
                opr         =  5'b00000;
                addr_rs1_o  =  dir_1 + 5'b00010;
                addr_rs2_o  =  dir_1 + 5'b00001;
                addr_rd_o   =  dir_1 + 5'b00010;
                we_o        =  1'b0;
                alucont_o   =  opr;
                flag_in     =  1'b0;
                led_o       =  {5'b10001,alucont_o,7'b0000001};
                we_7seg_o   =  1'b0;
            
                state_next = most_res;
            end
            
            most_res: begin
                mux_o       =  1'b1;
                dir_1       =  dir_1;
                dir_2       =  dir_2;
                opr         =  opr;
                addr_rs1_o  =  dir_1 + 5'b00010;
                addr_rs2_o  =  dir_1 + 5'b00001;
                addr_rd_o   =  dir_1 + 5'b00010;
                we_o        =  1'b0;
                alucont_o   =  opr;
                flag_in     =  1'b0;
                led_o       =  {5'b10001,alucont_o,7'b0000001};
                we_7seg_o   =  1'b1;

                state_next = sel_modo;
    
            end
            
           
            
            
            
            leer_regfile: begin
                mux_o       =  1'b1;
                dir_1       =  dir_1 + 5'b00011;
                dir_2       =  dir_2;
                opr         =  opr;
                addr_rs1_o  =  dir_2;
                addr_rs2_o  =  dir_1 + 5'b00001;
                addr_rd_o   =  dir_1 + 5'b00010;
                we_o        =  1'b0;
                alucont_o   =  opr;
                flag_in     =  1'b0;
                led_o       =  {5'b10001,alucont_o,7'b0000001};
                we_7seg_o   =  1'b0;
            
                if (teclado_i == 4'b0000) begin
                    state_next = most_regfile;
                end
                
                else begin
                    state_next = leer_regfile;
                end 
            end
            
            most_regfile: begin
                mux_o       =  1'b1;
                dir_1       =  dir_1 + 5'b00011;
                dir_2       =  dir_2 + 1'b1;
                opr         =  opr;
                addr_rs1_o  =  dir_2;
                addr_rs2_o  =  dir_1 + 5'b00001;
                addr_rd_o   =  dir_1 + 5'b00010;
                we_o        =  1'b0;
                alucont_o   =  opr;
                flag_in     =  1'b0;
                led_o       =  {5'b10001,alucont_o,7'b0000001};
                we_7seg_o   =  1'b1;

                state_next = sel_modo;
            end
             
        endcase
    end
    
endmodule
