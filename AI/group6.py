import pandas as pd
import networkx as nx
import numpy as np
from itertools import combinations
from sklearn.cluster import SpectralClustering

# Load Data from CSV
file_path = "responses.csv"  # Change this to your actual file
df = pd.read_csv(file_path)

# Ensure correct column name for names
name_column = "Name "  # Change this if necessary
if name_column not in df.columns:
    print("Error: 'Name' column not found! Check your CSV headers.")
    exit()

# Define weights for each question
weights = [2, 2, 1.5, 2, 1, 1.5, 2, 1, 1, 0.5, 0.5, 0.5, 10]  # Adjust as needed

# Create a Graph
G = nx.Graph()

# Calculate Matching Scores for all pairs
for student_A, student_B in combinations(df.index, 2):
    score = 0
    for i, weight in enumerate(weights[:-1]):  # Exclude "Preferred Partner"
        if df.iloc[student_A, i + 1] == df.iloc[student_B, i + 1]:
            score += weight

    # Extract Names
    name_A = df.iloc[student_A][name_column]
    name_B = df.iloc[student_B][name_column]

    # Check Mutual Preference
    preferred_A = df.iloc[student_A, -1]
    preferred_B = df.iloc[student_B, -1]
    if preferred_A == name_B and preferred_B == name_A:
        score += weights[-1]  # Bonus points for mutual choice

    # Add Edge to Graph
    if score > 0:
        G.add_edge(name_A, name_B, weight=score)

# Convert Graph to Adjacency Matrix
adj_matrix = nx.to_numpy_array(G, nodelist=df[name_column])

# Apply Spectral Clustering with 6 groups
num_groups = 6
clustering = SpectralClustering(n_clusters=num_groups, affinity="precomputed", assign_labels="discretize", random_state=42)
labels = clustering.fit_predict(adj_matrix)

# Organize students into groups
groups = {i: [] for i in range(num_groups)}
for student, group in zip(df[name_column], labels):
    groups[group].append(student)

# Balance Groups to ensure 4,4,4,4,5,5 distribution
sorted_groups = sorted(groups.values(), key=len, reverse=True)

# If a group has more than 5, redistribute members
while any(len(group) > 5 for group in sorted_groups):
    for i, group in enumerate(sorted_groups):
        if len(group) > 5:
            # Move extra member to a smaller group
            for j, smaller_group in enumerate(sorted_groups):
                if len(smaller_group) < 4:
                    smaller_group.append(group.pop())
                    break

# Print Final Groups
print("\nFinal Groups:")
for i, group in enumerate(sorted_groups):
    print(f"Group {i + 1}: {', '.join(group)}")
