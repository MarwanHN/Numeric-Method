# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wzN-MmI04-FlRDeD_VsBY3EiA3VG15tX
"""

import numpy
f = lambda x: 4*x*x*x-15*x*x+17*x-6
tf = lambda x: 12*x*x-30*x+17

n=0
x = 3.0
itemax = 100
eps = 0.0005
a = (f(x)/tf(x))

print("|it|       x   |   fx    |     tfx   | f(x1)/f'(x1)   |")
print("-------------------------------------------------------")
print('|{:2}|{:=9.5f}|{:=9.5f}|{:=9.5f}|{:=9.5f}           |'.format(n, x, f(x),tf(x),a))
for n in range(1,itemax):
  if abs(f(x)) >= eps:    
    x = x - (f(x)/tf(x))
    xi = x
    a = (f(x)/tf(x))
    print('|{:2}|{:=9.5f}|{:=9.5f}|{:=9.5f}|{:=9.5f}           |'.format(n, x, f(x),tf(x),a))
print('Akar ditemukan pada x = {:=9.5f}'.format (x))