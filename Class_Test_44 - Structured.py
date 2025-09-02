import numpy as np

#Tejas Vadgama -EK3 -92510133044.

# Que.1: Extract first two rows
A = np.arange(1, 17).reshape(4,4)
print("Que.1 Output:")
print(A[0:2,0:4])
print(A)  # Full matrix

# Que.2: Extract middle 3x3 from 5x5 matrix
B = np.arange(1,26).reshape(5,5)
print("\nQue.2 Output:")
print(B)
print(B[1:4,1:4])

# Que.3: Extract all even elements
C = B[B % 2 == 0]
print("\nQue.3 Output:")
print(C)
print("Boolean array for even elements:")
print(B % 2 == 0)  # Boolean array (if needed)

# Que.4: Extract "Python" from string
D = "pythonprogramming"
print("\nQue.4 Output:")
print(D[0:6])

# Que.5: Append two NumPy arrays
E = np.array([1,2,3,4,5])
F = np.array([6,7,8,9,10])
G = np.concatenate((E,F))
print("\nQue.5 Output:")
print(G)

# Que.6: Sort array
H = np.array([10,5,8,3])
print("\nQue.6 Output:")
print(np.sort(H))

# Que.7: Extract border elements in row-wise order
I = np.concatenate([
    A[0, :],                  # First row
    A[1:3, [0, 3]].flatten(), # First and last of middle rows
    A[3, :]                   # Last row
])
print("\nQue.7 Output:")
print(I)

# Que.8: Replace every 5th element with 0
J = np.arange(1,101)
J[4::5] = 0  # Every 5th element
print("\nQue.8 Output:")
print(J)

# Que.9: Replace all even numbers with 0
J[J % 2 == 0] = 0
print("\nQue.9 Output:")
print(J)

# Extra List-Based Que: Add specific elements from two lists
l1 = [1,2,3]
l2 = [4,5,6]
result = l1[0] + l2[0] + l1[2] + l2[2]
print("\nExtra List Que Output:")
print(result)
