# -*- coding: utf-8 -*-
"""New Year and the Treasure Geolocation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qSSqvuQeTZbte9BT_pEuSKibscxJvptg
"""

n = int(input())
T = 2*n
sum1 = 0
sum2 = 0
for i in range(T):
  x,y=map(int,input(). split())
  sum1 = sum1+x
  sum2 = sum2+y
print(int(sum1/n)," ",int(sum2/n))