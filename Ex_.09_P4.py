import pandas as pd

s1 = pd.Series([1, 2, 3], name='A')
s2 = pd.Series([4, 5, 6], name='B')

# Vertically (stacked)
ver_stack = pd.concat([s1, s2], axis=0)
print("\nVertical Stack:")
print(ver_stack)

# Horizontally (as columns in a DataFrame)
hori_stack = pd.concat([s1, s2], axis=1)
print("\nHorizontal Stack:")
print(hori_stack)