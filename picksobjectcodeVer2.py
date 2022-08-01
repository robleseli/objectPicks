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

np_array1 = np.array([[2, 3],[2,4]])

printpicks = Picks(np_array1, [],[], "pst",
"product",1,
"label", "filepath") #setting the last one as None returns a typeError.
print(printpicks)
try:
    printpicks.load()
except TypeError as e:
    print(e)
    raise e

print("end")


#1
add_pick = printpicks.add_pick(1,1,True)  #positional arg.
print(add_pick) #no errorss

#2
delete_picks = printpicks.delete_picks(1,1,True)
print(delete_picks)

#3
add_pair = printpicks.add_pair(1,1,1)
print(add_pair)

#4
close_pick = printpicks.close_pick(1,1)
print(close_pick)
#array concat. errors

#5
delete_pick = printpicks.delete_pick(1,1,1,1)
print(delete_pick)
#having array concat.errors

#6
get_sweeps = printpicks.get_sweeps()
print(get_sweeps)

#7
calc_missing_vmax = printpicks.calc_missing_vmax()
print(calc_missing_vmax)
print("OKAY7")

#8
autopick = printpicks.autopick()
print(autopick)
print("OKAY8")

#9
display_name = printpicks.display_name()
print(display_name)

#10
is_complete = printpicks.is_complete()
print(is_complete)



