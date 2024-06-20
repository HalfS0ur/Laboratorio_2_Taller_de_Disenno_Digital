`timescale 1ns / 1ps

module FSM_control(
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
    output logic [5:0]     estado_o,
    output logic           we_7seg_o
    );
    
    logic [4:0] rs1 = 1;
    logic [4:0] reg_rs1 = 1;
    logic [4:0] rs2 = 2;
    logic [4:0] reg_rs2 = 2;
    logic [4:0] rd = 1;
    logic [4:0] leer_rf = 1;
    logic [3:0] aluop = 0;
    logic [3:0] reg_op = 0;
    logic [5:0] state;
    
    localparam [5:0]
        INICIO = 5'b00000,
        SEL_MODO = 5'b00001,
        ESP_DATO_1 = 5'b00010,
        LEER_REGFILE = 5'b00011,
        REC_DATO_1 = 5'b00100,
        DATO_1_INV = 5'b00101,
        GRD_DATO_1 = 5'b00110,
        LEER_DATO_1 = 5'b00111,
        MOST_DATO_1 = 5'b01000,
        ESP_OP = 5'b01001,
        REC_OP = 5'b01010,
        MOST_OP = 5'b01011,
        OP_INV = 5'b01100,
        ESP_DATO_2 = 5'b01101,
        REC_DATO_2 = 5'b01110,
        GRD_DATO_2 = 5'b01111,
        DATO_2_INV = 5'b10000,
        LEER_DATO_2 = 5'b10001,
        MOST_DATO_2 = 5'b10010,
        ESP_ENT = 5'b10011,
        REC_ENT = 5'b10100,
        ENT_INV = 5'b10101,
        LEER_DATOS = 5'b10110,
        OPERA_DATOS = 5'b10111,
        GRD_RES = 5'b11000,
        LEER_RES = 5'b11001,
        MOST_RES = 5'b11010,
        PREP_SIG_OP = 5'b11011,
        ESP_MODO = 5'b11100,
        MOST_REGFILE = 5'b11101,
        PREP_SIG_RD = 5'b11110;
        
    always_ff @(posedge clk_i, posedge reset_i) begin
        if (reset_i) begin
            state <= INICIO;
            mux_o <= 0;
            reg_rs1 <= 1;
            reg_rs2 <= 2;
            addr_rs1_o <= 1;
            addr_rs2_o <= 2;
            aluop <= 0;
            rd <= 1;
            we_regfile_o <= 0;
            led_o <= 0;
            we_7seg_o <= 0;
            reg_op <= 0;
            addr_rd_o <= 1;
            alucont_o <= 0;
            leer_rf <= 1;
        end
        
        else begin
            case(state)
                INICIO: begin
                mux_o <= 0;
                addr_rs1_o <= reg_rs1;
                addr_rs2_o <= reg_rs2;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= 0;
                we_7seg_o <= 0;
                reg_op <= 0;
                addr_rd_o <= rd;
                alucont_o <= aluop;
                leer_rf <= leer_rf;
                state <= SEL_MODO;
            end
            
            SEL_MODO: begin
                mux_o <= 0;
                addr_rs1_o <= reg_rs1;
                addr_rs2_o <= reg_rs2;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b00001,11'b0};
                we_7seg_o <= 0;
                reg_op <= 0;
                addr_rd_o <= rd;
                leer_rf <= leer_rf;
                alucont_o <= aluop;
                
                if (sw_i == 0) begin
                    state <= ESP_DATO_1;
                end
                
                else begin
                    state <= LEER_REGFILE;
                end
            end
            
            ESP_DATO_1: begin
                mux_o <= 0;
                addr_rs1_o <= reg_rs1;
                addr_rs2_o <= reg_rs2;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b00010,11'b0};
                we_7seg_o <= 0;
                reg_op <= 0;
                addr_rd_o <= rd;
                leer_rf <= 1;
                alucont_o <= aluop;
                
                if (key_detect_i) begin
                    state <= REC_DATO_1;
                end
                
                else begin
                    state <= ESP_DATO_1;
                end
            end
            
            REC_DATO_1: begin
                mux_o <= 0;
                addr_rs1_o <= reg_rs1;
                addr_rs2_o <= reg_rs2;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b00011,11'b0};
                we_7seg_o <= 0;
                reg_op <= 0;
                addr_rd_o <= rd;
                leer_rf <= 1;
                alucont_o <= aluop;
                
                if (teclado_i < 4'b1010) begin
                    state <= GRD_DATO_1;
                end
                
                else begin
                    state <= DATO_1_INV;
                end
            end
            
            DATO_1_INV: begin
                mux_o <= 0;
                addr_rs1_o <= reg_rs1;
                addr_rs2_o <= reg_rs2;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b00100,10'b0, 1'b1};
                we_7seg_o <= 0;
                reg_op <= 0;
                addr_rd_o <= rd;
                alucont_o <= aluop;
                leer_rf <= 1;
                state <= ESP_DATO_1;
            end
            
            GRD_DATO_1: begin
                mux_o <= 0;
                addr_rs1_o <= reg_rs1;
                addr_rs2_o <= reg_rs2;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 1;
                led_o <= {5'b00101,11'b0};
                we_7seg_o <= 0;
                reg_op <= 0;
                addr_rd_o <= rd;
                alucont_o <= aluop;
                leer_rf <= 1;
                state <= LEER_DATO_1;
            end
            
            LEER_DATO_1: begin
                mux_o <= 0;
                addr_rs1_o <= reg_rs1;
                addr_rs2_o <= rd;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b00110,11'b0};
                we_7seg_o <= 0;
                reg_op <= 0;
                addr_rd_o <= rd;
                alucont_o <= aluop;
                leer_rf <= 1;
                state <= MOST_DATO_1;
            end
            
            MOST_DATO_1: begin
                mux_o <= 0;
                addr_rs1_o <= reg_rs1;
                addr_rs2_o <= rd;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b00111,11'b0};
                we_7seg_o <= 1;
                reg_op <= 0;
                addr_rd_o <= rd;
                alucont_o <= aluop;
                leer_rf <= 1;
                state <= ESP_OP;
            end
            
            ESP_OP: begin
                mux_o <= 0;
                addr_rs1_o <= reg_rs1;
                addr_rs2_o <= reg_rs2;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b01000,11'b0};
                we_7seg_o <= 0;
                reg_op <= 0;
                alucont_o <= aluop;
                leer_rf <= 1;
                addr_rd_o <= rd;
                
                if (key_detect_i) begin
                    state <= REC_OP;
                end
                
                else begin
                    state <= ESP_OP;
                end
            end
            
            REC_OP: begin
                mux_o <= 0;
                addr_rs1_o <= reg_rs1;
                addr_rs2_o <= reg_rs2;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b01001,11'b0};
                we_7seg_o <= 0;
                //reg_op = 0;
                addr_rd_o <= rd;
                leer_rf <= 1;
                alucont_o <= aluop;
                
                if (teclado_i > 4'b1001 && teclado_i < 4'b1111) begin
                    reg_op <= teclado_i;
                    state <= MOST_OP;
                end
                
                else begin
                    reg_op <= 0;
                    state <= OP_INV;
                end
            end
            
            OP_INV: begin
                mux_o <= 0;
                addr_rs1_o <= reg_rs1;
                addr_rs2_o <= reg_rs2;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b01010,10'b0, 1'b1};
                we_7seg_o <= 0;
                reg_op <= 0;
                addr_rd_o <= rd;
                leer_rf <= 1;
                alucont_o <= aluop;
                state <= ESP_OP;
            end
            
            MOST_OP: begin
                mux_o <= 0;
                addr_rs1_o <= reg_rs1;
                addr_rs2_o <= reg_rs2;
                aluop <= aluop;
                rd <= rd + 1;
                we_regfile_o <= 0;
                led_o <= {5'b01011, 1'b0, reg_op, 6'b0};
                we_7seg_o <= 0;
                //reg_op = 0;
                addr_rd_o <= rd;
                leer_rf <= 1;
                alucont_o <= aluop;
                state <= ESP_DATO_2;
            end
            
            ESP_DATO_2: begin
                mux_o <= 0;
                addr_rs1_o <= reg_rs1;
                addr_rs2_o <= reg_rs2;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b01100, 1'b0, reg_op, 6'b0};
                we_7seg_o <= 0;
                //reg_op = 0;
                leer_rf <= 1;
                alucont_o <= aluop;
                addr_rd_o <= rd;
                
                if (key_detect_i) begin
                    state <= REC_DATO_2;
                end
                
                else begin
                    state <= ESP_DATO_2;
                end
            end
            
            REC_DATO_2: begin
                mux_o <= 0;
                addr_rs1_o <= reg_rs1;
                addr_rs2_o <= reg_rs2;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b01101, 1'b0, reg_op, 6'b0};
                we_7seg_o <= 0;
                //reg_op = 0;
                leer_rf <= 1;
                alucont_o <= aluop;
                addr_rd_o <= rd;
                
                if (teclado_i < 4'b1010) begin
                    state <= GRD_DATO_2;
                end
                
                else begin
                    state <= DATO_2_INV;
                end
            end
            
            DATO_2_INV: begin
                mux_o <= 0;
                addr_rs1_o <= reg_rs1;
                addr_rs2_o <= reg_rs2;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b01110, 1'b0, reg_op, 6'b1};
                we_7seg_o <= 0;
                //reg_op = 0;
                leer_rf <= 1;
                addr_rd_o <= rd;
                alucont_o <= aluop;
                state <= ESP_DATO_2;
            end
            
            GRD_DATO_2: begin
                mux_o <= 0;
                addr_rs1_o <= reg_rs1;
                addr_rs2_o <= reg_rs2;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 1;
                led_o <= {5'b01111, 1'b0, reg_op, 6'b0};
                we_7seg_o <= 0;
                //reg_op = 0;
                leer_rf <= 1;
                addr_rd_o <= rd;
                alucont_o <= aluop;
                state <= LEER_DATO_2;
            end
            
            LEER_DATO_2: begin
                mux_o <= 0;
                addr_rs1_o <= reg_rs1;
                addr_rs2_o <= rd;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b10000, 1'b0, reg_op, 6'b0};
                we_7seg_o <= 0;
                //reg_op = 0;
                leer_rf <= 1;
                addr_rd_o <= rd;
                alucont_o <= aluop;
                state <= MOST_DATO_2;
            end
            
            MOST_DATO_2: begin
                mux_o <= 0;
                addr_rs1_o <= reg_rs1;
                addr_rs2_o <= rd;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b10001, 1'b0, reg_op, 6'b0};
                we_7seg_o <= 1;
                //reg_op = 0;
                leer_rf <= 1;
                addr_rd_o <= rd;
                alucont_o <= aluop;
                state <= ESP_ENT;
            end
            
            ESP_ENT: begin
                mux_o <= 0;
                addr_rs1_o <= reg_rs1;
                addr_rs2_o <= reg_rs2;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b10010, 1'b0, reg_op, 6'b0};
                we_7seg_o <= 0;
                //reg_op = 0;
                leer_rf <= 1;
                alucont_o <= aluop;
                addr_rd_o <= rd;
                
                if (key_detect_i) begin
                    state <= REC_ENT;
                end
                
                else begin
                    state <= ESP_ENT;
                end
            end
            
            REC_ENT: begin
                mux_o <= 0;
                addr_rs1_o <= reg_rs1;
                addr_rs2_o <= reg_rs2;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b10011, 1'b0, reg_op, 6'b0};
                we_7seg_o <= 0;
                //reg_op = 0;
                leer_rf <= 1;
                addr_rd_o <= rd;
                alucont_o <= aluop;
                
                if (teclado_i == 4'b1111) begin
                    state <= LEER_DATOS;
                end
                
                else begin
                    state <= ENT_INV;
                end
            end
            
            ENT_INV: begin
                mux_o <= 0;
                addr_rs1_o <= reg_rs1;
                addr_rs2_o <= reg_rs2;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b10100, 1'b0, reg_op, 5'b0, 1'b1};
                we_7seg_o <= 0;
                //reg_op = 0;
                leer_rf <= 1;
                addr_rd_o <= rd;
                alucont_o <= aluop;
                state <= ESP_ENT;
            end
            
            LEER_DATOS: begin
                mux_o <= 0;
                addr_rs1_o <= reg_rs1;
                addr_rs2_o <= reg_rs2;
                aluop <= reg_op;
                rd <= rd + 1;
                we_regfile_o <= 0;
                led_o <= {5'b10101, 1'b0, reg_op, 6'b0};
                we_7seg_o <= 0;
                //reg_op = 0;
                leer_rf <= 1;
                addr_rd_o <= rd;
                alucont_o <= aluop;
                state <= OPERA_DATOS;
            end
            
            OPERA_DATOS: begin
                mux_o <= 1;
                addr_rs1_o <= reg_rs1;
                addr_rs2_o <= reg_rs2;
                aluop <= reg_op;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b10110, 1'b0, reg_op, 6'b0};
                we_7seg_o <= 0;
                //reg_op = 0;
                leer_rf <= 1;
                addr_rd_o <= rd;
                alucont_o <= aluop;
                state <= GRD_RES;
            end
            
            GRD_RES: begin
                mux_o <= 1;
                addr_rs1_o <= reg_rs1;
                addr_rs2_o <= reg_rs2;
                aluop <= reg_op;
                rd <= rd;
                we_regfile_o <= 1;
                led_o <= {5'b10111, 1'b0, reg_op, 6'b0};
                we_7seg_o <= 0;
                //reg_op = 0;
                leer_rf <= 1;
                addr_rd_o <= rd;
                alucont_o <= aluop;
                state <= LEER_RES;
            end
            
            LEER_RES: begin
                mux_o <= 1;
                addr_rs1_o <= reg_rs1;
                addr_rs2_o <= rd;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b11000, 1'b0, reg_op, 6'b0};
                we_7seg_o <= 0;
                //reg_op = 0;
                leer_rf <= 1;
                addr_rd_o <= rd;
                alucont_o <= aluop;
                state <= MOST_RES;
            end
            
            MOST_RES: begin
                mux_o <= 1;
                addr_rs1_o <= reg_rs1;
                addr_rs2_o <= rd;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b11001, 1'b0, reg_op, 6'b0};
                we_7seg_o <= 1;
                //reg_op = 0;
                leer_rf <= 1;
                addr_rd_o <= rd;
                alucont_o <= aluop;
                state <= PREP_SIG_OP;
            end
            
            PREP_SIG_OP: begin
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
                addr_rs1_o <= reg_rs1;
                addr_rs2_o <= reg_rs2;
                aluop <= 0;
                //rd <= rd;
                we_regfile_o <= 0;
                led_o <= 16'hFFFF;
                we_7seg_o <= 0;
                reg_op <= 0;
                addr_rd_o <= rd;
                alucont_o <= aluop;
                leer_rf <= 1;
                state <= INICIO;     
            end
            
            LEER_REGFILE: begin
                mux_o <= 1;
                addr_rs1_o <= reg_rs1;
                addr_rs2_o <= leer_rf;
                aluop <= aluop;
                rd <= rd;
                we_regfile_o <= 0;
                led_o <= {5'b00011, 1'b0, reg_op, 6'b0};
                we_7seg_o <= 1;
                //leer_rf <= 1;
                addr_rd_o <= rd;
                alucont_o <= aluop;
                state <= PREP_SIG_RD;
            end
            
            PREP_SIG_RD: begin
                if (leer_rf == 30) begin
                    leer_rf <= 1;
                end
                
                else begin
                    leer_rf <= leer_rf + 1;
                end
                
                mux_o <= 0;
                addr_rs1_o <= reg_rs1;
                addr_rs2_o <= leer_rf;
                aluop <= 0;
                //rd <= rd;
                we_regfile_o <= 0;
                led_o <= 16'hFFFF;
                we_7seg_o <= 0;
                reg_op <= 0;
                addr_rd_o <= rd;
                alucont_o <= aluop;
                //leer_rf <= 1;
                state <= INICIO;
            end
            endcase
        end
        
    //assign addr_rs1_o = rs1;
    //assign addr_rs2_o = rs2;
    //assign addr_rd_o = rd;
    //assign alucont_o = aluop;
    
    
    end
    assign alu_flag_in_o = 0;
    assign estado_o = state;
endmodule
