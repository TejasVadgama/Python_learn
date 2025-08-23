import pandas as pan

# Define two series
A1 = pan.Series([10, 20, 30, 40, 50])
A2 = pan.Series([1, 2, 3, 4, 5])

print("Series 1:")
print(A1)
print("Series 2:")
print(A2)

# Arithmetic operations
print("\nAddition:")
print(A1 + A2)

print("\nSubtraction:")
print(A1 - A2)

print("\nMultiplication:")
print(A1 * A2)

print("\nDivision:")
print(A1 / A2)