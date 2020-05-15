
from pandas.io.parsers import read_csv
data = read_csv(r"D:\assignment 2\14100224.csv")
filtered_data = data.dropna(axis='columns', how='all')
filtered_data.to_csv(r"D:\assignment 2\empty-columns-removed.csv")

filtered_data
