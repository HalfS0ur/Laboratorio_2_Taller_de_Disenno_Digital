# Makefile
export PYTHONPATH := $(PWD):$(PYTHONPATH)

TOPLEVEL_LANG = verilog

VERILOG_SOURCES = $(PWD)/antirebotes.sv \
				  $(PWD)/contador_dos_bits.sv \
				  $(PWD)/deteccion_tecla.sv \
				  $(PWD)/key_encoding.sv \
				  $(PWD)/registro_paralelo.sv \
				  $(PWD)/registro_available.sv \
				  $(PWD)/sincronizador.sv \
				  $(PWD)/top.sv

TOPLEVEL = top

MODULE = interfaz_teclado_hex_tb

WAVES = 1

include $(shell cocotb-config --makefiles)/Makefile.sim