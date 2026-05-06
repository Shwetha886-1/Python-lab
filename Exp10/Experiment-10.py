# Import library
import pandas as pd

# Step 1: Load data (example CSV file)
df = pd.read_csv("data.csv")

# Step 2: Display first 5 rows
print("First 5 rows:")
print(df.head())

# Step 3: Explore data
print("\nData Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nShape of data:")
print(df.shape)

# Step 4: Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Step 5: Clean data
# Fill missing values with mean (for numeric columns)
df.fillna(df.mean(numeric_only=True), inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Step 6: Final cleaned data
print("\nCleaned Data:")
print(df.head())




# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Create dataset
data = {
    'Name': ['A', 'B', 'C', 'D'],
    'Marks': [85, 90, 78, 92]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display data
print("Dataset:")
print(df)

# Line Graph
plt.plot(df['Name'], df['Marks'])
plt.title("Line Graph - Marks")
plt.xlabel("Name")
plt.ylabel("Marks")
plt.show()

# Bar Chart
plt.bar(df['Name'], df['Marks'])
plt.title("Bar Chart - Marks")
plt.xlabel("Name")
plt.ylabel("Marks")
plt.show()

# Pie Chart
plt.pie(df['Marks'], labels=df['Name'], autopct='%1.1f%%')
plt.title("Pie Chart - Marks Distribution")
plt.show()

# Histogram
plt.hist(df['Marks'])
plt.title("Histogram - Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()