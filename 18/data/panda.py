import pandas as pd

# series = pd.Series([5, 6, 7], index=['a', 'b', 'c'])
# print(series)
# print(series.values)
# print(series['a'])
# print(series[['a', 'c']])

# print(series[series <= 6])

slovar = {'a': 3, 'b': 4, 'c': 10}

series = pd.Series(slovar)
print(series)
