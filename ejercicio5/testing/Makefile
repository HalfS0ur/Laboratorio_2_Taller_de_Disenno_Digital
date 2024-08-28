# Makefile
export PYTHONPATH := $(PWD):$(PYTHONPATH)

TOPLEVEL_LANG = verilog
VERILOG_SOURCES += $(PWD)/../*.sv
TOPLEVEL = top
MODULE = regfile_tb
WAVES = 1

include $(shell cocotb-config --makefiles)/Makefile.sim