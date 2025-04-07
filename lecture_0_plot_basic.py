# %% [markdown]
# # Data Visualization with Pandas and Matplotlib
# 
# ## Introduction
# Pandas and Matplotlib provide a powerful combination for creating informative and visually appealing plots. In this lecture, we will explore basic plotting techniques using a business dataset. We'll cover line plots, bar plots, and pie charts to gain insights from the data.
# 
# ## Dataset
# We'll use a dataset containing sales data for a company. The dataset includes information about the year, product category, and sales amount.

# %%
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Year': [2018, 2019, 2020, 2021, 2018, 2019, 2020, 2021, 2018, 2019, 2020, 2021],
    'Category': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C'],
    'Sales': [1000, 1200, 1400, 1600, 800, 900, 1000, 1100, 1200, 1400, 1600, 1800]
}

df = pd.DataFrame(data)
df
# %% [markdown]
# ## Sales Trend Analysis
# Let's analyze the sales trend over time using a line plot.

# %%
fig, ax = plt.subplots(figsize=(8, 6))
df.groupby(['Year', 'Category'])['Sales'].sum().unstack().plot(ax=ax)
ax.set_xlabel('Year')
ax.set_ylabel('Sales')
ax.set_title('Sales Trend by Category')
ax.legend(title='Category')

# %% [markdown]
# ## Sales Comparison by Category
# We can create a bar plot to compare the total sales for each category.

# %%
fig, ax = plt.subplots(figsize=(8, 6))
df.groupby('Category')['Sales'].sum().plot(kind='bar', ax=ax)
ax.set_xlabel('Category')
ax.set_ylabel('Total Sales')
ax.set_title('Total Sales by Category')

# %% [markdown]
# ## Sales Proportion by Category
# Let's create a pie chart to visualize the proportion of sales for each category.

# %%
fig, ax = plt.subplots(figsize=(8, 8))
df.groupby('Category')['Sales'].sum().plot(kind='pie', autopct='%1.1f%%', ax=ax)
ax.set_title('Sales Proportion by Category')

# %% [markdown]
# ## Conclusion
# Pandas and Matplotlib provide a straightforward way to create informative visualizations for business data. By using basic plotting techniques like line plots, bar plots, and pie charts, we can gain valuable insights into sales trends, comparisons, and proportions.
# 
# Remember to refer to the Pandas and Matplotlib documentation for more plotting options and customization techniques. Happy data visualization!