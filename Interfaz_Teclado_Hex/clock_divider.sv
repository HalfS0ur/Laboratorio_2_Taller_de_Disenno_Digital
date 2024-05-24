module clock_divider (
    input logic clk_i,     // 10 MHz clock input
    input logic reset_i,      // Active high synchronous reset
    output logic clk_o    // 10 kHz clock output
);

    // Calculate the divide factor
    localparam int DIVIDE_FACTOR = 1000;
    localparam int COUNTER_WIDTH = $clog2(DIVIDE_FACTOR);

    // Counter to keep track of clock cycles
    logic [COUNTER_WIDTH-1:0] counter;

    // Output clock toggle register
    logic clk_out_reg;

    // Combinational logic for clock output
    assign clk_o = clk_out_reg;

    // Sequential logic for counter and output clock
    always_ff @(posedge clk_i or posedge reset_i) begin
        if (reset_i) begin
            counter <= 0;
            clk_out_reg <= 0;
        end else begin
            if (counter == DIVIDE_FACTOR-1) begin
                counter <= 0;
                clk_out_reg <= ~clk_out_reg;
            end else begin
                counter <= counter + 1;
            end
        end
    end

endmodule