#!/usr/bin/env python3
import sys

pickpath='./syst_linux_py/radutils'
#print(sys.path)

#from pickutils.py import Picks
#Picks()

sys.path.insert(1,pickpath)

print(sys.path)

from pickutils import Picks
print_picks = Picks([],[],[], "pst", "product",1, "label", "filepath") #setting the last one as None returns a typeError.
print(print_picks)

try:
    print_picks.load()
except TypeError as e:
    print(e)
    raise e

print("end")



VarMethod = Picks.nameOfMethodToTest(1,1,1)  #positional arg. data types will vary but for the most part they are ints.
print(VarMathod)