import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

filtered_arr = []

for element in arr:
  if element % 2 == 0:
    filtered_arr.append(False)
  else:
    filtered_arr.append(True)

print(arr[filtered_arr])