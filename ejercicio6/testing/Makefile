# Makefile
export PYTHONPATH := $(PWD):$(PYTHONPATH)

TOPLEVEL_LANG = verilog

VERILOG_SOURCES = $(PWD)/alu.sv \
				  $(PWD)/banco_de_registros.sv \
				  $(PWD)/FSM_Control.sv \
				  $(PWD)/display_7_segmentos.sv \
				  $(PWD)/mux_2_1.sv \
				  $(PWD)/registro_paralelo.sv \
				  $(PWD)/top.sv

TOPLEVEL = top

MODULE = unidad_calculo_tb

WAVES = 1

include $(shell cocotb-config --makefiles)/Makefile.sim