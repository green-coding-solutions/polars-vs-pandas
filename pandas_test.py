import pandas as pd

df = pd.read_csv('bigfile.log', names=['time', 'value'], dtype={'time': int, 'value': int}, sep=' ',)

df['difference'] = df.time.diff()

df['difference'] = df['difference'].fillna(1)

print('Any different?', (df['difference'] > 0).any())

print('Mean:', df['difference'].mean())
