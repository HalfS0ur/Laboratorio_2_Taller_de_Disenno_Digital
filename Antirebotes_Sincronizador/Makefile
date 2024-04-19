# Makefile
export PYTHONPATH := $(PWD):$(PYTHONPATH)

TOPLEVEL_LANG = verilog
VERILOG_SOURCES = $(PWD)/top.sv \
				 $(PWD)/sincronizador.sv \
				 $(PWD)/debouncer.sv \
				 $(PWD)/contador.sv 
TOPLEVEL = top
MODULE = antirebotes_sincronizador_tb
WAVES = 1

include $(shell cocotb-config --makefiles)/Makefile.sim