`timescale 1ns / 1ps

module control(
    input logic            clk_i,
    input logic            reset_i,
    input logic [3:0]      teclado_i,
    input logic            key_detect_i,
    input logic            sw_i,
    
    output logic           mux_o,
    output logic [4:0]     addr_rs1_o,
    output logic [4:0]     addr_rs2_o,
    output logic [4:0]     addr_rd_o,
    output logic           we_regfile_o,
    output logic [3:0]     alucont_o,
    output logic           alu_flag_in_o,
    output logic [15:0]    led_o, 
    output logic           we_7seg_o
    );
    
    logic [4:0] rs1 = 1;
    logic [4:0] reg_rs1 = 1;
    logic [4:0] rs2 = 2;
    logic [4:0] reg_rs2 = 2;
    logic [4:0] rd = 1;
    logic [3:0] aluop = 0;
    logic [3:0] reg_op = 0;
    
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
            esp_op,
            rec_op,
            most_op,
            op_inv,
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
            prep_sig_op,
            esp_modo,
            most_regfile   
        } state_t;
        
    state_t state_reg, state_next;
    
    always_ff @(posedge clk_i, posedge reset_i) begin
        if (reset_i) begin
            state_reg <= inicio;
        end
        
        else begin
            state_reg <= state_next;
        end
    end
    
    always_ff @(posedge clk_i) begin
        state_next <= state_reg;
        
        case(state_reg)
            inicio: begin
                mux_o <= 0;
                rs1 <= reg_rs1;
                rs2 <= reg_rs2;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= 0;
                we_7seg_o <= 0;
                reg_op <= 0;
                state_next <= sel_modo;
            end
            
            sel_modo: begin
                mux_o <= 0;
                rs1 <= reg_rs1;
                rs2 <= reg_rs2;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b00001,11'b0};
                we_7seg_o <= 0;
                reg_op <= 0;
                
                if (sw_i == 0) begin
                    state_next <= esp_dato_1;
                end
                
                else begin
                    state_next <= leer_regfile;
                end
            end
            
            esp_dato_1: begin
                mux_o <= 0;
                rs1 <= reg_rs1;
                rs2 <= reg_rs2;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b00010,11'b0};
                we_7seg_o <= 0;
                reg_op <= 0;
                
                if (key_detect_i) begin
                    state_next <= rec_dato_1;
                end
                
                else begin
                    state_next <= esp_dato_1;
                end
            end
            
            rec_dato_1: begin
                mux_o <= 0;
                rs1 <= reg_rs1;
                rs2 <= reg_rs2;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b00011,11'b0};
                we_7seg_o <= 0;
                reg_op <= 0;
                
                if (teclado_i < 4'b1010) begin
                    state_next <= grd_dato_1;
                end
                
                else begin
                    state_next <= dato_1_inv;
                end
            end
            
            dato_1_inv: begin
                mux_o <= 0;
                rs1 <= reg_rs1;
                rs2 <= reg_rs2;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b00100,10'b0, 1'b1};
                we_7seg_o <= 0;
                reg_op <= 0;
                state_next <= esp_dato_1;
            end
            
            grd_dato_1: begin
                mux_o <= 0;
                rs1 <= reg_rs1;
                rs2 <= reg_rs2;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 1;
                led_o <= {5'b00101,11'b0};
                we_7seg_o <= 0;
                reg_op <= 0;
                state_next <= leer_dato_1;
            end
            
            leer_dato_1: begin
                mux_o <= 0;
                rs1 <= reg_rs1;
                rs2 <= rd;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b00110,11'b0};
                we_7seg_o <= 0;
                reg_op <= 0;
                state_next <= most_dato_1;
            end
            
            most_dato_1: begin
                mux_o <= 0;
                rs1 <= reg_rs1;
                rs2 <= rd;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b00111,11'b0};
                we_7seg_o <= 1;
                reg_op <= 0;
                state_next <= esp_op;
            end
            
            esp_op: begin
                mux_o <= 0;
                rs1 <= reg_rs1;
                rs2 <= reg_rs2;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b01000,11'b0};
                we_7seg_o <= 0;
                reg_op <= 0;
                
                if (key_detect_i) begin
                    state_next <= rec_op;
                end
                
                else begin
                    state_next <= esp_op;
                end
            end
            
            rec_op: begin
                mux_o <= 0;
                rs1 <= reg_rs1;
                rs2 <= reg_rs2;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b01001,11'b0};
                we_7seg_o <= 0;
                //reg_op = 0;
                
                if (teclado_i > 4'b1001 && teclado_i < 4'b1111) begin
                    reg_op <= teclado_i;
                    state_next <= most_op;
                end
                
                else begin
                    reg_op <= 0;
                    state_next <= op_inv;
                end
            end
            
            op_inv: begin
                mux_o <= 0;
                rs1 <= reg_rs1;
                rs2 <= reg_rs2;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b01010,10'b0, 1'b1};
                we_7seg_o <= 0;
                reg_op <= 0;
                state_next <= esp_op;
            end
            
            most_op: begin
                mux_o <= 0;
                rs1 <= reg_rs1;
                rs2 <= reg_rs2;
                aluop <= aluop;
                rd <= rd + 1;
                we_regfile_o <= 0;
                led_o <= {5'b01011, 1'b0, reg_op, 6'b0};
                we_7seg_o <= 0;
                //reg_op = 0;
                state_next <= esp_dato_2;
            end
            
            esp_dato_2: begin
                mux_o <= 0;
                rs1 <= reg_rs1;
                rs2 <= reg_rs2;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b01100, 1'b0, reg_op, 6'b0};
                we_7seg_o <= 0;
                //reg_op = 0;
                
                if (key_detect_i) begin
                    state_next <= rec_dato_2;
                end
                
                else begin
                    state_next <= esp_dato_2;
                end
            end
            
            rec_dato_2: begin
                mux_o <= 0;
                rs1 <= reg_rs1;
                rs2 <= reg_rs2;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b01101, 1'b0, reg_op, 6'b0};
                we_7seg_o <= 0;
                //reg_op = 0;
                
                if (teclado_i < 4'b1010) begin
                    state_next <= grd_dato_2;
                end
                
                else begin
                    state_next <= dato_2_inv;
                end
            end
            
            dato_2_inv: begin
                mux_o <= 0;
                rs1 <= reg_rs1;
                rs2 <= reg_rs2;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b01110, 1'b0, reg_op, 6'b1};
                we_7seg_o <= 0;
                //reg_op = 0;
                state_next <= esp_dato_2;
            end
            
            grd_dato_2: begin
                mux_o <= 0;
                rs1 <= reg_rs1;
                rs2 <= reg_rs2;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 1;
                led_o <= {5'b01111, 1'b0, reg_op, 6'b0};
                we_7seg_o <= 0;
                //reg_op = 0;
                state_next <= leer_dato_2;
            end
            
            leer_dato_2: begin
                mux_o <= 0;
                rs1 <= reg_rs1;
                rs2 <= rd;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b10000, 1'b0, reg_op, 6'b0};
                we_7seg_o <= 0;
                //reg_op = 0;
                state_next <= most_dato_2;
            end
            
            most_dato_2: begin
                mux_o <= 0;
                rs1 <= reg_rs1;
                rs2 <= rd;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b10001, 1'b0, reg_op, 6'b0};
                we_7seg_o <= 1;
                //reg_op = 0;
                state_next <= esp_ent;
            end
            
            esp_ent: begin
                mux_o <= 0;
                rs1 <= reg_rs1;
                rs2 <= reg_rs2;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b10010, 1'b0, reg_op, 6'b0};
                we_7seg_o <= 0;
                //reg_op = 0;
                
                if (key_detect_i) begin
                    state_next <= rec_ent;
                end
                
                else begin
                    state_next <= esp_ent;
                end
            end
            
            rec_ent: begin
                mux_o <= 0;
                rs1 <= reg_rs1;
                rs2 <= reg_rs2;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b10011, 1'b0, reg_op, 6'b0};
                we_7seg_o <= 0;
                //reg_op = 0;
                
                if (teclado_i == 4'b1111) begin
                    state_next <= leer_datos;
                end
                
                else begin
                    state_next <= ent_inv;
                end
            end
            
            ent_inv: begin
                mux_o <= 0;
                rs1 <= reg_rs1;
                rs2 <= reg_rs2;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b10100, 1'b0, reg_op, 5'b0, 1'b1};
                we_7seg_o <= 0;
                //reg_op = 0;
                state_next <= esp_ent;
            end
            
            leer_datos: begin
                mux_o <= 0;
                rs1 <= reg_rs1;
                rs2 <= reg_rs2;
                aluop <= reg_op;
                rd <= rd + 1;
                we_regfile_o <= 0;
                led_o <= {5'b10101, 1'b0, reg_op, 6'b0};
                we_7seg_o <= 0;
                //reg_op = 0;
                state_next <= opera_datos;
            end
            
            opera_datos: begin
                mux_o <= 1;
                rs1 <= reg_rs1;
                rs2 <= reg_rs2;
                aluop <= reg_op;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b10110, 1'b0, reg_op, 6'b0};
                we_7seg_o <= 0;
                //reg_op = 0;
                state_next <= grd_res;
            end
            
            grd_res: begin
                mux_o <= 1;
                rs1 <= reg_rs1;
                rs2 <= reg_rs2;
                aluop <= reg_op;
                rd <= rd;
                we_regfile_o <= 1;
                led_o <= {5'b10111, 1'b0, reg_op, 6'b0};
                we_7seg_o <= 0;
                //reg_op = 0;
                state_next <= leer_res;
            end
            
            leer_res: begin
                mux_o <= 1;
                rs1 <= reg_rs1;
                rs2 <= rd;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b11000, 1'b0, reg_op, 6'b0};
                we_7seg_o <= 0;
                //reg_op = 0;
                state_next <= most_res;
            end
            
            most_res: begin
                mux_o <= 1;
                rs1 <= reg_rs1;
                rs2 <= rd;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b11001, 1'b0, reg_op, 6'b0};
                we_7seg_o <= 1;
                //reg_op = 0;
                state_next <= prep_sig_op;
            end
            
            prep_sig_op: begin
                if (rd == 30) begin
                    reg_rs1 <= 1;
                    reg_rs2 <= 2;
                    rd <= 1;
                end
                
                else begin
                    reg_rs1 <= reg_rs1 + 3;
                    reg_rs2 <= reg_rs2 + 3;
                    rd <= rd + 1;
                end
                
                mux_o <= 0;
                rs1 <= reg_rs1;
                rs2 <= reg_rs2;
                aluop <= 0;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= 16'hFFFF;
                we_7seg_o <= 0;
                reg_op <= 0;
                state_next <= sel_modo;     
            end
        endcase
    end
    
    
    assign addr_rs1_o = rs1;
    assign addr_rs2_o = rs2;
    assign addr_rd_o = rd;
    assign alucont_o = aluop;
    assign alu_flag_in_o = 0;
    
endmodule
