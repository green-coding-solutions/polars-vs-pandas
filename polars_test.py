import polars as pl

# Read the file using Polars
df = pl.read_csv('bigfile.log', has_header=False, new_columns=['time', 'value'], separator=' ')

df = df.with_columns((pl.col("time") - pl.col("time").shift(1)).alias("difference"))

print('Any different?', (df['difference'] <= 0).any())

print('Mean:', df['difference'].mean())
