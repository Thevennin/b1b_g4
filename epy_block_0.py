"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr

class mean_meter (gr. sync_block ):
	""" Descripcion del bloque """
	def __init__ ( self ):
		gr. sync_block . __init__ (self ,
			name =" e_mean_meter_ff ",
			in_sig =[ np. float32 ],
			out_sig =[ np. float32 ])
		# variables externas
		self . contador = 0
		self . acum =0
	def work (self , input_items , output_items ):
		# traduccion a algo que podemos manejar mejor
		in0 = input_items [0]
		out0 = output_items [0]
		# Logica principal
		self . contador += len ( in0 )
		self . acum += np. sum ( in0 )
		out0 [:] = self . acum / self . contador
		return len ( output_items [0])
