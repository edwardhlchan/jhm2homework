import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('sales.csv') # Read the data from the csv file
plot = plt.bar(df['Month'], df['Sales'], width=0.5, color = '#008000') # bar chart with green, width 0.5
# Lables and title
plt.xlabel('Month')
plt.ylabel('Sales (in thousand dollars)')
plt.title('Bar Chart of Ice-cream Sales')
# Show the plot
plt.show()