# pip3 install seaborn

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset from the CSV file
df = pd.read_csv('iris.csv')

# Create a Violin Plot for petal.length and variety
plt.figure(figsize=(10, 6))
sns.violinplot(x='variety', y='petal.length', data=df, palette='viridis')
plt.title('Violin Plot of Petal Length by Variety')
plt.xlabel('Variety')
plt.ylabel('Petal Length')

# Save the plot to a file
plt.savefig('violinPlot_petalLength.png')

# Show the plot
plt.show()
