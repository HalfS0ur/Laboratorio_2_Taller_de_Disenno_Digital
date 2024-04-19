# Makefile
export PYTHONPATH := $(PWD):$(PYTHONPATH)

TOPLEVEL_LANG = verilog
VERILOG_SOURCES = $(PWD)/reloj_10MHz.sv
TOPLEVEL = reloj_10MHz
MODULE = reloj_10MHz_tb
WAVES = 1

include $(shell cocotb-config --makefiles)/Makefile.sim