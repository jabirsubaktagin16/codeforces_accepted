# -*- coding: utf-8 -*-
"""In Search of an Easy Problem.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1izQimESIJu2YTP10UjQfNYnzTZdmvCT7
"""

n = int(input())
a = list(map(int,input().split()))

if sum(a):
  print('HARD')
else:
  print('EASY')