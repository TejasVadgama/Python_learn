import numpy as np
import pandas as pd

List = [5, 10, 15, 20]
Array = np.array([25, 30, 35, 40])
Dict1 = {'A': 1, 'B': 2, 'C': 3}

S_List = pd.Series(List)
S_array = pd.Series(Array)
S_dict1 = pd.Series(Dict1)

print("\nSeries from List:")
print(S_List)

print("\nSeries from NumPy Array:")
print(S_array)

print("\nSeries from Dictionary:")
print(S_dict1)