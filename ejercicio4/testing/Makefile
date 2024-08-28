# Makefile
export PYTHONPATH := $(PWD):$(PYTHONPATH)

TOPLEVEL_LANG = verilog
VERILOG_SOURCES += $(PWD)/../*.sv
TOPLEVEL = top
MODULE = program_counter_tb
WAVES = 1

include $(shell cocotb-config --makefiles)/Makefile.sim