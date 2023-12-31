# Loading in required libraries

# for data manipulation
import pandas as pd

# for data visualization
import seaborn as sns

# for working with arrays and numerical values
import numpy as np

# for efficient data cleaning
import klib as kb
 
# for plotting
import matplotlib.pyplot as plt                     

 # for plotting percent
from matplotlib.ticker import PercentFormatter  

# Reading in the Nobel Prize data
nobel = pd.read_csv(NobelWinner.csv)

# Returns the dimensions (rows and columns) of our dataset
nobel.shape

# Display concise information about the dataframe
nobel.info()

# Cleaning Datasets in case of Duplicate Values
clean_col_names = kb.data_cleaning(nobel)
clean_col_names.info()

# Let's check for null values in our dataset
nobel.isnull().sum()

# Load the dataset
nobel = pd.read_csv(NobelWinner.csv)

# Impute missing values in 'motivation', 'birth_city', 'birth_country', and 'sex'
nobel["motivation"].fillna("No motivation provided", inplace=True)
nobel["birth_city"].fillna("Unknown", inplace=True)
nobel["birth_country"].fillna("Unknown", inplace=True)
nobel["sex"].fillna("Unknown", inplace=True)

# Convert 'birth_date' to datetime type
nobel["birth_date"] = pd.to_datetime(nobel["birth_date"])

# Calculate the median birth year
median_birth_year = nobel["birth_date"].dropna().dt.year.median()

# Impute missing birth dates based on the median year
nobel["birth_date"] = nobel["birth_date"].fillna(
    pd.to_datetime(str(int(median_birth_year)) + "-01-01")
)

# Drop irrelevant columns
nobel.drop(
    [
        "death_date",
        "death_city",
        "death_country",
        "organization_name",
        "organization_city",
        "organization_country",
    ],
    axis=1,
    inplace=True,
)

nobel.isnull().sum()

# Our Analysis

# Taking a look at the first several winners
nobel.head(8)

# Display the number of (possibly shared) Nobel Prizes handed out between 1901 and 2016
print(nobel["prize_share"].value_counts())

# Display the number of prizes won by male and female recipients.
print(nobel["sex"].value_counts())

# Display the number of prizes won by the top 10 nationalities.
nobel["birth_country"].value_counts().head(10)

Gender of a Nobel Prize winner
# Calculating the proportion of female laureates per decade
nobel['female_winner'] = nobel['sex'] == 'Female'
prop_female_winners = nobel.groupby(['decade', 'category'], as_index=False)[
    'female_winner'].mean()

# Plotting USA born winners with % winners on the y-axis

ax = sns.lineplot(x='decade', y='female_winner',
                  hue='category', data=prop_female_winners)

ax.yaxis.set_major_formatter(PercentFormatter(1.0))

First Woman To Win The Nobel Prize

# # Picking out the first woman to win a Nobel Prize
# # To get the year from a datetime column you need to use access the dt.year value.
# # Here is an example:
# # a_data_frame['a_datatime_column'].dt.year

# # nobel['Female']

# nobel.nsmallest(1, "year")

# Filter and sort the DataFrame to include only female winners and reset the index
first_female_winner = (
    nobel[nobel["sex"] == "Female"].sort_values(
        "year").reset_index(drop=True).iloc[0]
)

# Display the information of the first female winner
first_female_winner

# Repeat laureates
# Selecting the laureates that have received 2 or more prizes.
nobel.groupby("full_name").filter(lambda group: len(group) >= 2)

Average Age Of A Nobel Prize Winner.
# Converting birth_date from String to datetime
nobel['birth_date'] = pd.to_datetime(nobel['birth_date'])

# Calculating the age of Nobel Prize winners
nobel['age'] = nobel['year'] - nobel['birth_date'].dt.year

# Plotting the age of Nobel Prize winners
sns.lmplot(x='year', y='age', data=nobel, lowess=True,
           aspect=2, line_kws={'color': 'red'})

# Same plot as above, but separate plots for each type of Nobel Prize
sns.lmplot(x='year', y='age', data=nobel, row='category',
           lowess=True, aspect=2, line_kws={'color': 'red'})

# The oldest winner of a Nobel Prize as of 2016
display(nobel.nlargest(1, "age"))

# The youngest winner of a Nobel Prize as of 2016
display(nobel.nsmallest(1, "age"))
