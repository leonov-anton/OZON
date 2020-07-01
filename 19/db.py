import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data.csv', encoding='unicode_escape')

# print(df.shape) размер таблицы

print(df.head(5))