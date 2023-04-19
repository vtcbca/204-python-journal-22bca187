#scrip12....Write a NumPy program to convert a list of numeric value into a one-dimensional NumPy array. Print original list and array with its dimension , size and byte occupied in memory
import numpy as np
l1 = [50, 100, 200, 332]
print("Original List:",l1)
v = np.array(l1)
print("One-dimensional NumPy array: ",v)
