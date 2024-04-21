import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Choose a different style instead of 'seaborn'
plt.style.use('ggplot')

# Load the data
df = pd.read_csv('all-data.csv', encoding="ISO-8859-1")
print(df.head())
df.isna().sum()