# -*- coding: utf-8 -*-
"""Hulk.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ti_EWZO3c6BAQLmp-f5cIJB6XcmDHhRZ
"""

n = int(input())
ans = ""
for i in range(1, n):
  if i%2==1:
    ans+="I hate that "
  else:
    ans+="I love that "

if n%2==1:
  print (ans+"I hate it")
else:
  print (ans+"I love it")