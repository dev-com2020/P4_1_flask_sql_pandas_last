import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

data = np.genfromtxt('data/example_data.csv', delimiter=';', names=True, dtype=None, encoding='UTF')
# print(data[0][0])
# print(data)
# print(data.dtype)
# print(data.shape)

array_dict = {col: np.array([row[i] for row in data])for i, col in enumerate(data.dtype.names)}

# array_dict = {}
# for i, col in enumerate(data.dtype.names):
#     column_data = []
#     for row in data:
#         column_data.append(row[i])
#     array_dict[col] = np.array(column_data)

# print(array_dict)
# print(array_dict['mag'].max())
# print(array_dict['mag'].min())
# print(array_dict['mag'].mean())
#
# print(np.array([value[array_dict['mag'].argmax()] for key, value in array_dict.items()]))

place = pd.Series(array_dict['place'], name='place')
mag = pd.Series(array_dict['mag'], name='mag')
print(place)
place_index = place.index
print(place_index)
print(place_index.values)
mag.plot()
plt.show()
