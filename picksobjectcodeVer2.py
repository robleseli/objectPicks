#!/usr/bin/env python3
import sys
from array import *
import numpy as np

pickpath='./syst_linux_py/radutils'
#print(sys.path)

#from pickutils.py import Picks
#Picks()

sys.path.insert(1,pickpath)

print(sys.path)

from pickutils import Picks

np_array1 = np.array([[]])
np_array2 = np.array([[]])
np_array3 = np.array([[]])

picks = Picks(np_array1, np_array2, np_array3, "IRE/CCx/X01a",
"der",1,
"bed", "IRE-CCx-X01a.bed")
print(picks)
#print(picks.get_sweeps());  # Errors out because there is no data.
picks.load()
print(picks.get_sweeps());

#1
picks.add_pick(1,1,True)  #positional arg.

#2
picks.delete_pick(1,1,True)

#3
picks.add_pair(1,1,1)

#4
picks.close_pick(1,1)

#5
picks.delete_picks(1,1,1)

#6
picks.get_sweeps()

#7
picks.calc_missing_vmax()

#8
picks.autopick()

#9
picks.display_name()

#10
picks.is_complete()

