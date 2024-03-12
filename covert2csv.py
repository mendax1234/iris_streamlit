# Convert iris.data to iris.csv for further processing
import pandas as pd
data = pd.read_csv("raw_dataset/iris.data", header=0)
data.to_csv("data/iris.csv", index=False)