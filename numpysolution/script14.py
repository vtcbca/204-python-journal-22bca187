#Write a NumPy program to get the values and indices of the elements that are bigger than 10 in a given array.
import numpy as np
a = np.array([[0, 10, 20], [30, 40, 50]])
print("Original array: ")
print(a)
print("Values is bigger than 10 =", a[a>10])
