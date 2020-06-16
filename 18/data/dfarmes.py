import pandas as pd

df = pd.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
    'population': [18, 137.5, 9, 40],
    'square': [2724902, 17125191, 207600, 603628]
}, index=['Kz', 'Ru', 'By', 'Ua'])

df.to_csv('file.csv')