# Makefile
export PYTHONPATH := $(PWD):$(PYTHONPATH)

TOPLEVEL_LANG = verilog

VERILOG_SOURCES = $(PWD)/regfile.sv

TOPLEVEL = regfile

MODULE = regfile_tb

WAVES = 1

include $(shell cocotb-config --makefiles)/Makefile.sim