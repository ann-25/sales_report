import pandas as pd
import numpy as np
#visualization tools for python
import matplotlib.pyplot as plt
import seaborn as sns

#load dataset
filepath = "SampleSuperstore.csv"
# Read the CSV file
df = pd.read_csv(r"C:\Users\Thomas\Desktop\analytical projects\SPARK\Retal-beginner-EDA\SampleSuperstore.csv") #add r to remove unicode
# print(df.head(10))
# # Print the dataframe#
# # print(df)

# #data cleaning and preparation
# print(df.info())  # To check for missing values and data types
# df.drop_duplicates(inplace=True)  # Remove duplicates

# #data exploration
print(df.describe())

#distribution plot
#histogram
plt.figure(figsize=(10, 6))
sns.histplot(df['Sales'], bins=30, kde=True)
plt.title('Sales Distribution')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()

# #boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Category', y='Sales', data=df)
plt.title('Sales Distribution by Category')
plt.xlabel('Category')
plt.ylabel('Sales')
plt.show()

#relationship plot
#scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Sales', y='Profit', hue='Category', data=df)
plt.title('Sales vs Profit')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.show()

#pair plot
sns.pairplot(df[['Sales', 'Profit', 'Quantity', 'Discount']])
plt.show()

#Ctegorical plot
#Bar plot
plt.figure(figsize=(12, 6))
sns.barplot(x='Region', y='Sales', data=df)
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.show()

#count plot
plt.figure(figsize=(12, 6))
sns.countplot(x='Ship Mode', data=df)
plt.title('Count of Ship Mode')
plt.xlabel('Ship Mode')
plt.ylabel('Count')
plt.show()

#correlation heatmap
plt.figure(figsize=(12, 8))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()






