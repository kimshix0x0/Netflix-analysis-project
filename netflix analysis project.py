# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
df = pd.read_csv("mymoviedb.csv", lineterminator = '\n')

# %%
df.head()

# %%
df.info()

# %%
df['Genre'].head()

# %%
#to check duplicate

df.duplicated()

# %%
df.describe()

# %%
#changing the formate of Release_Date
df['Release_Date'] =  pd.to_datetime(df['Release_Date'])
print(df['Release_Date'].dtypes)

# %%
df['Release_Date'] = df['Release_Date'].dt.year
df['Release_Date'].dtypes

# %%
df.head()

# %%
#dlting unuseful column

col = ['Overview', 'Original_Language','Poster_Url']
df.drop(col, axis=1, inplace= True)
df.columns

# %% [markdown]
# categorizing Vote_Average column
# we would cut the Vote_Average values and make 4 categories : popular, average, below_avg and not popular to describe it more using categorize_col() function provided above

# %%
def categorize_col(df, col, label):
    edges = [df[col].describe()['min'],
            df[col].describe()['25%'],
            df[col].describe()['50%'],
            df[col].describe()['75%'],
            df[col].describe()['max']]
            
    df[col] = pd.cut(df[col], edges, labels = labels, duplicates = 'drop')
    return df

# %%
labels = ['popular', 'average', 'below avg', 'not popular']

categorize_col(df, 'Vote_Average', labels)
df['Vote_Average'].unique()

# %%
df.head()

# %%
df['Vote_Average'].value_counts()

# %%
#drop null values
df.dropna(inplace = True)

#confirming
df.isna().sum()

# %% [markdown]
# #separating all the genre
# we'd split genre into a list and then explore our dataframe to have only one genre per row for ezch movie
# 

# %%
#split the strings into lists
df['Genre'] = df['Genre'].str.split(', ')

#explode the lists
df = df.explode('Genre').reset_index(drop = True)
df.head()

# %%
#casting column into category

df['Genre'] = df['Genre'].astype('category')
df['Genre'].dtypes

# %%
df['Genre'].cat.categories

# %%
df['Genre'].unique()

# %%
df.info()

# %%
df.nunique()

# %% [markdown]
# now, our data is completely resolved and processed

# %% [markdown]
# Data Visulisation

# %%
sns.set_style('whitegrid')

# %% [markdown]
# Q1. What is the most frequent genre of movies released on Netflix?

# %%
df['Genre'].describe()

# %%
sns.catplot(y = 'Genre', data = df, kind = 'count',
order = df['Genre'].value_counts().index)

plt.title('Genre column distribution')
plt.show()

# %% [markdown]
# Q2. Which has highest votes avg column?

# %%
df.head()

# %%
sns.catplot(y = 'Vote_Average', data = df, kind = 'count',
order = df['Vote_Average'].value_counts().index)

plt.title('Vote Average column distribution')
plt.show()

# %% [markdown]
# Q3. What movie got the highest popularity what's its genre

# %%
df[df['Popularity'] == df['Popularity'].max()]

# %% [markdown]
# Q4. What movie got the lowest popularity what's its genre

# %%
df[df['Popularity'] == df['Popularity'].min()]

# %% [markdown]
# Q5. which year has the most filmmed movies?

# %%
df['Release_Date'].hist()
plt.title("Release Date column distributed")
plt.show()

# %% [markdown]
# #SUMMARY
# 
# Q1: What is the most frequent genre in the dataset?
# 
# Drama genre is the most frequent genre in our dataset and has appeared more than 14% of the times among 19 other genres.
# 
# Q2: What genres has highest votes?
# 
# We have 25.5% of our dataset with popular vote (6520 rows). Drama again gets the highest popularity among fans by having more than 18.5% of movies popularities.
# 
# Q3: What movie got the highest popularity? What's its genre?
# 
# Spider-Man: No Way Home has the highest popularity rate in our dataset and it has genres of Action, Adventure, and Science Fiction.
# 
# Q4: Which year has the most filmed movies?
# 
# Year 2020 has the highest filming rate in our dataset.

# %%



