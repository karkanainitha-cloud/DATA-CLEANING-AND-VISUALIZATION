# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set_style("whitegrid")

# Load Dataset
df = pd.read_csv("Salary_Dataset.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset Information
print("\nDataset Info:")
print(df.info())

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove Duplicate Rows
df.drop_duplicates(inplace=True)

# Fill Missing Values (if any)
df["Experience_Years"] = df["Experience_Years"].fillna(df["Experience_Years"].median())
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])
df["Salary"] = df["Salary"].fillna(df["Salary"].median())

# Convert Data Types
df["Experience_Years"] = df["Experience_Years"].astype(int)
df["Age"] = df["Age"].astype(int)
df["Salary"] = df["Salary"].astype(float)

# Check Cleaned Dataset
print("\nCleaned Dataset:")
print(df.head())

# -----------------------------
# DATA VISUALIZATION
# -----------------------------

# 1. Salary Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["Salary"], bins=10, kde=True)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Count")
plt.show()

# 2. Gender Count
plt.figure(figsize=(6,5))
sns.countplot(x="Gender", data=df)
plt.title("Gender Distribution")
plt.show()

# 3. Experience vs Salary
plt.figure(figsize=(8,5))
sns.scatterplot(x="Experience_Years", y="Salary", hue="Gender", data=df)
plt.title("Experience vs Salary")
plt.show()

# 4. Age vs Salary
plt.figure(figsize=(8,5))
sns.scatterplot(x="Age", y="Salary", hue="Gender", data=df)
plt.title("Age vs Salary")
plt.show()

# 5. Salary by Gender
plt.figure(figsize=(6,5))
sns.boxplot(x="Gender", y="Salary", data=df)
plt.title("Salary by Gender")
plt.show()

# 6. Correlation Heatmap
plt.figure(figsize=(6,4))
numeric_df = df[["Experience_Years", "Age", "Salary"]]
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

print("\nData Cleaning and Visualization Completed Successfully!")
