import numpy as np

arr = np.array([2,6,1,9,10,3,27])

filtered_arr = []

for element in arr:
  if element >= 5 and element <= 10:
    filtered_arr.append(True)
  else:
    filtered_arr.append(False)

print(arr[filtered_arr])