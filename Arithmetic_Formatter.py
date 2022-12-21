# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 18:51:45 2022

@author: cayoj
"""
 
import numpy as np
import time

a = np.array(["32", "3801", "45", "123"])

c = np.array(["+", "-"])

v = np.array(["698", "2", "43", "49"])



print("  ", a[0], "    ", a[1], "    ", a[2], "  ", a[3])
print(c[0], v[0], "  ", c[1],"", v[0], "  ", c[0], v[2], " ", c[0], v[3])
print("-----    -------    ----  -----")

print("")

p = np.array(["32", "1", "9999", "523"])

i = np.array(["8", "3801", "9999", "49"])

b = np.array([32 + 8, 1 - 3801, 9999 + 9999, 523 - 49, True])

if b[4] == True:

    print("", p[0], "         ", p[1], "    ", p[2], "   ", p[3])
    print(c[0], i[0], "   ", c[1],"   ", i[0], "  ", c[0], i[2], " ", c[0], "", i[3])
    print("-----     -------   -------  ------")
    print(" ", b[0], "     ", b[1], "  ", b[2], "   ", b[3])

time.sleep(4)