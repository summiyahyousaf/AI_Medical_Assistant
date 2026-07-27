import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from data_loader import load_data
train_df,test_df=load_data()


print(train_df.head())
print("\nDataset Shape: ")
print(train_df.shape)

print("Information : ")
train_df.info()

print("\nColumns: ")
print(train_df.columns)

print("\nStatistical Summary:")
print(train_df.describe())

#check for missing values
print("\nMissing Values:")
print(train_df.isnull().sum())

#check for duplicated values
print("\nDuplicated Rows : ")
print(train_df.duplicated().sum())

#Display Disease Distribution
print("Disease Distribution: ", train_df["prognosis"].value_counts())

#Count unique diseases
print("Unique Diseases : ", train_df["prognosis"].nunique())

#Display list of diseases
print("List of all Diseases: ", train_df["prognosis"].unique())



# DATA VISUALIZATION

disease_count=train_df["prognosis"].value_counts()
plt.figure(figsize=(15,8))
disease_count.plot(kind="bar")
plt.title("Disease Distribution")
plt.xlabel("Disease")
plt.ylabel("Number of Patients")
plt.xticks(rotation=90)
plt.grid(axis="y" , linestyle="--", alpha=0.7)
plt.tight_layout()

plt.savefig("images/disease_distribution.png")
plt.show()



#visualization of missing values

missing_values= train_df.isnull().sum()
missing_values = missing_values[missing_values > 0]
plt.figure(figsize=(15,8))
missing_values.plot(kind="bar")
plt.title("Missing Values")
plt.xlabel("Columns")
plt.ylabel("Number of Missing values")
plt.xticks(rotation=90)
plt.grid(axis="y" , linestyle="--" , alpha=0.7)
plt.tight_layout()

plt.savefig("images/missing_values.png")
plt.show()



print("Unnamed 133 Columns:")
print(train_df["Unnamed: 133"].unique())

train_df = train_df.drop(columns=["Unnamed: 133"])

print("\nShape After Removing Unnamed Column:")
print(train_df.shape)
