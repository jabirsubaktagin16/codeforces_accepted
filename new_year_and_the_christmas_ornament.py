# -*- coding: utf-8 -*-
"""New Year and the Christmas Ornament.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GfNB7dM7Wo582kArTte-MNMTMu5lZh7-
"""

y,b,r = map(int,input(). split())
a = min(b-1, r-2)
result = int(3*(min(y,a)+1))
print(result)