# import pandas as pd
# from itertools import combinations
# import networkx as nx

# # Load Google Form responses
# df = pd.read_csv("poll.csv")  # Change the file name if needed

# # Extract names and answers
# names = df.iloc[:, 1].values  # First column is 'Name'
# answers = df.iloc[:, 2:].values  # All other columns are responses

# # Define weights for each question (adjust based on importance)
# weights = [2, 2, 1.5, 2, 1, 1.5, 2, 1, 1, 0.5, 0.5, 0.5]  # Adjust based on your form

# # Function to calculate weighted compatibility
# def calculate_compatibility(person1, person2):
#     return sum(weight for (a, b, weight) in zip(person1, person2, weights) if a == b)

# # Create a graph for optimal matching
# G = nx.Graph()

# # Generate all possible pairs and their scores
# for i, j in combinations(range(len(names)), 2):
#     score = calculate_compatibility(answers[i], answers[j])
#     G.add_edge(names[i], names[j], weight=score)

# # Find the best pairing using Maximum Matching
# best_matching = nx.max_weight_matching(G, maxcardinality=True)

# # Print the final pairs
# print("\nFinal Group Pairs:")
# for a, b in best_matching:
#     print(f"{a} is paired with {b} (Score: {G[a][b]['weight']})")

# # Optional: Save the pairs to a CSV file
# output_df = pd.DataFrame(best_matching, columns=["Student 1", "Student 2"])
# output_df.to_csv("final_pairs.csv", index=False)


# import pandas as pd
# import networkx as nx
# from itertools import combinations

# #  Load Data from CSV (Google Form responses)
# file_path = "responses.csv"  # Change to your CSV file path
# df = pd.read_csv(file_path)

# # 🚨 FIX: Make sure we're using the correct "Name" column
# name_column = "Name "  # Change this if the column has a different name in your CSV
# if name_column not in df.columns:
#     print("Error: 'Name' column not found! Check your CSV headers.")
#     exit()

# #  Define weights for each question
# weights = [2, 2, 1.5, 2, 1, 1.5, 2, 1, 1, 0.5, 0.5, 0.5, 10]  # Adjust as needed

# #  Create a Graph for Matching
# G = nx.Graph()

# # 4️⃣ Pairwise Comparison: Calculate Matching Scores
# for student_A, student_B in combinations(df.index, 2):  # Compare every pair
#     score = 0
#     for i, weight in enumerate(weights[:-1]):  # Exclude "Preferred Partner" for now
#         if df.iloc[student_A, i + 1] == df.iloc[student_B, i + 1]:  # Same answer
#             score += weight

#     # 🚨 FIX: Extract names correctly
#     name_A = df.iloc[student_A][name_column]
#     name_B = df.iloc[student_B][name_column]

#     # 5️⃣ Check Mutual Preference
#     preferred_partner_A = df.iloc[student_A, -1]  # Last column = Preferred Partner
#     preferred_partner_B = df.iloc[student_B, -1]

#     if preferred_partner_A == name_B and preferred_partner_B == name_A:
#         score += weights[-1]  # Extra points for mutual choice

#     # 6️⃣ Add to Graph
#     if score > 0:
#         G.add_edge(name_A, name_B, weight=score)

# # 7️⃣ Compute Maximum Weight Matching
# matched_pairs = nx.max_weight_matching(G, maxcardinality=True)

# # 8️⃣ Print Final Pairs with Names
# print("\nFinal Group Pairs:")
# for pair in matched_pairs:
#     name_A, name_B = pair
#     score = G[name_A][name_B]["weight"]
#     print(f"{name_A} is paired with {name_B} (Score: {score})")

#fix
import pandas as pd
import networkx as nx
from itertools import combinations

# Load Data from CSV
file_path = "responses.csv"  # Change to your CSV file path
df = pd.read_csv(file_path)

# Fix: Ensure correct column name for student names
name_column = "Name "  # Adjust based on your CSV file
if name_column not in df.columns:
    print("Error: 'Name' column not found! Check your CSV headers.")
    exit()

# Define weights for each question
weights = [2, 2, 1.5, 2, 1, 1.5, 2, 1, 1, 0.5, 0.5, 0.5, 10]  # Adjust as needed

# Create a Graph for Matching
G = nx.Graph()

# Pairwise Comparison: Calculate Matching Scores
pair_scores = {}  # Store scores for reference

for student_A, student_B in combinations(df.index, 2):  # Compare every pair
    score = 0
    score_breakdown = []  # Track individual score calculations

    name_A = df.iloc[student_A][name_column]
    name_B = df.iloc[student_B][name_column]

    # Compare answers and calculate score
    for i, weight in enumerate(weights[:-1]):  # Exclude "Preferred Partner"
        answer_A = df.iloc[student_A, i + 1]
        answer_B = df.iloc[student_B, i + 1]

        if answer_A == answer_B:  # If answers match, add the weighted score
            score += weight
            score_breakdown.append(f"Q{i+1}: {answer_A} = {answer_B} → +{weight}")

    # Check mutual preference bonus
    preferred_partner_A = df.iloc[student_A, -1]  # Last column = Preferred Partner
    preferred_partner_B = df.iloc[student_B, -1]

    if preferred_partner_A == name_B and preferred_partner_B == name_A:
        score += weights[-1]  # Extra points for mutual choice
        score_breakdown.append(f"🎯 Mutual Choice Bonus → +{weights[-1]}")

    # Store score details for debugging
    pair_scores[(name_A, name_B)] = (score, score_breakdown)

    # Add to Graph if score > 0
    if score > 0:
        G.add_edge(name_A, name_B, weight=score)

# Compute Maximum Weight Matching
matched_pairs = nx.max_weight_matching(G, maxcardinality=True)

# Print Final Pairs with Score Breakdown
print("\nFinal Group Pairs with Score Calculation:\n")
for pair in matched_pairs:
    name_A, name_B = pair
    score, breakdown = pair_scores.get((name_A, name_B), pair_scores.get((name_B, name_A), (0, [])))

    print(f"{name_A} is paired with {name_B} (Final Score: {score})")
    print("\n".join(breakdown))  # Show detailed score calculations
    print("-" * 40)  # Separator


# import pandas as pd
# import networkx as nx
# import numpy as np
# from itertools import combinations
# from sklearn.cluster import SpectralClustering

# # Load Data from CSV
# file_path = "responses.csv"  # Change this to your actual file
# df = pd.read_csv(file_path)

# # Ensure correct column name for names
# name_column = "Name "  # Change this if necessary
# if name_column not in df.columns:
#     print("Error: 'Name' column not found! Check your CSV headers.")
#     exit()

# # Define weights for each question
# weights = [2, 2, 1.5, 2, 1, 1.5, 2, 1, 1, 0.5, 0.5, 0.5, 10]  # Adjust as needed

# # Create a Graph
# G = nx.Graph()

# # Calculate Matching Scores for all pairs
# for student_A, student_B in combinations(df.index, 2):
#     score = 0
#     for i, weight in enumerate(weights[:-1]):  # Exclude "Preferred Partner"
#         if df.iloc[student_A, i + 1] == df.iloc[student_B, i + 1]:
#             score += weight

#     # Extract Names
#     name_A = df.iloc[student_A][name_column]
#     name_B = df.iloc[student_B][name_column]

#     # Check Mutual Preference
#     preferred_A = df.iloc[student_A, -1]
#     preferred_B = df.iloc[student_B, -1]
#     if preferred_A == name_B and preferred_B == name_A:
#         score += weights[-1]  # Bonus points for mutual choice

#     # Add Edge to Graph
#     if score > 0:
#         G.add_edge(name_A, name_B, weight=score)

# # Convert Graph to Adjacency Matrix
# adj_matrix = nx.to_numpy_array(G, nodelist=df[name_column])

# # Apply Spectral Clustering with 6 groups
# num_groups = 6
# clustering = SpectralClustering(n_clusters=num_groups, affinity="precomputed", assign_labels="discretize", random_state=42)
# labels = clustering.fit_predict(adj_matrix)

# # Organize students into groups
# groups = {i: [] for i in range(num_groups)}
# for student, group in zip(df[name_column], labels):
#     groups[group].append(student)

# # Balance Groups to ensure 4,4,4,4,5,5 distribution
# sorted_groups = sorted(groups.values(), key=len, reverse=True)

# # If a group has more than 5, redistribute members
# while any(len(group) > 5 for group in sorted_groups):
#     for i, group in enumerate(sorted_groups):
#         if len(group) > 5:
#             # Move extra member to a smaller group
#             for j, smaller_group in enumerate(sorted_groups):
#                 if len(smaller_group) < 4:
#                     smaller_group.append(group.pop())
#                     break

# # Print Final Groups
# print("\nFinal Groups:")
# for i, group in enumerate(sorted_groups):
#     print(f"Group {i + 1}: {', '.join(group)}")

