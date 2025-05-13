import numpy as np;

# Create a 4x4 array with integers from 1 to 16
array_4x4_int = np.arange(1, 17).reshape((4, 4))

print(array_4x4_int)

# Create a 5x5 array with integers from 1 to 25
array_5x5_int = np.arange(1, 21).reshape((4, 5))
print(array_5x5_int)

# Create a 4x1 array with integers from 1 to 4
array_4x1_int = np.arange(1, 5).reshape((4, 1))
print(array_4x1_int)

array1D_uint8 = np.array([[255,256,257]],dtype=np.uint8)

# Challenge 2 - Concatenate 1x4 array to 4x4 array in the middle row

array_1x4_int = np.array([[2, 0, 1, 4]]);
array_4x4_int = np.insert(array_4x4_int, 2, array_1x4_int, axis=0)

print(array_4x4_int)

# Exercise 3 - Create a 200x200 array filled with the value of 100.

array_200x200_int = np.full((200, 200), 100)
print(array_200x200_int)

# Challenge 3 - Create a 7x7 array where it increments from 1 for every cell, but every alternating column is 0, and every even-indexed row is 0s. All 0s are not counted in the increment.

array_7x7_int = np.zeros((7, 7), dtype=int)
for i in range(7):
    for j in range(7):
        if i % 2 == 1:
            array_7x7_int[i, j] = 0
        elif i % 2 == 0 and j % 2 == 0:
            array_7x7_int[i, j] = (i // 2) * 4 + (j // 2) + 1
print(array_7x7_int)