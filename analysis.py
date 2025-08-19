# Marimo Notebook: Interactive Data Analysis
# Author email: 21f2000670@ds.study.iitm.ac.in

# Cell 1: Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mo  # Marimo interactive module

# Cell 2: Create sample dataset
# This cell generates random data for analysis
np.random.seed(42)
data_size = 100
x = np.random.rand(data_size) * 10
y = 2 * x + np.random.normal(0, 2, data_size)
df = pd.DataFrame({'x': x, 'y': y})

# Display the first 5 rows
df.head()

# Cell 3: Interactive slider to filter data
# Slider for selecting max x value
max_x = mo.ui.slider(1, 10, value=10, label="Max X Value")

# Cell 4: Filter data based on slider
# This cell depends on 'max_x' and 'df' from previous cells
filtered_df = df[df['x'] <= max_x]

# Cell 5: Dynamic Markdown
# Shows number of points in filtered dataset
mo.md(f"### Number of points with x ≤ {max_x}: {len(filtered_df)}")

# Cell 6: Plot filtered data
plt.figure(figsize=(6,4))
plt.scatter(filtered_df['x'], filtered_df['y'], color='teal')
plt.title(f"Scatter plot of y vs x (x ≤ {max_x})")
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

