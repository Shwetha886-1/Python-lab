# Import libraries
import numpy as np
import pandas as pd

# Create a NumPy array
arr = np.array([10, 20, 30, 40, 50])
print("NumPy Array:", arr)

# Perform operations
print("Mean:", np.mean(arr))
print("Sum:", np.sum(arr))

# Create a Pandas DataFrame
data = {
    "Name": ["Asha", "Riya", "Kiran"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

print("\nPandas DataFrame:")
print(df)


# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Create data
data = {
    "Team": ["RCB", "CSK", "MI", "KKR"],
    "Score": [180, 200, 175, 190]
}

# Create DataFrame
df = pd.DataFrame(data)

print("DataFrame:")
print(df)

# Plot graph
plt.bar(df["Team"], df["Score"])
plt.title("Team Scores")
plt.xlabel("Teams")
plt.ylabel("Scores")

# Show plot
plt.show()