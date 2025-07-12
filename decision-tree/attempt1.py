import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

# Load the CSV file
file_path = "./data.csv"
df = pd.read_csv(file_path)

# Display basic information about the dataset
df.info(), df.head()

# Define features and target variable
X = df.drop(columns=['love "back to the future"'])
y = df['love "back to the future"']

# Create and train the Gini decision tree
gini_tree = DecisionTreeClassifier(criterion='gini', random_state=42)
gini_tree.fit(X, y)

# Create and train the Entropy decision tree
entropy_tree = DecisionTreeClassifier(criterion='entropy', random_state=42)
entropy_tree.fit(X, y)

# Plot both trees
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 6))

tree.plot_tree(gini_tree, filled=True, feature_names=X.columns, class_names=["No", "Yes"], ax=axes[0])
axes[0].set_title("Decision Tree using Gini Impurity")

tree.plot_tree(entropy_tree, filled=True, feature_names=X.columns, class_names=["No", "Yes"], ax=axes[1])
axes[1].set_title("Decision Tree using Entropy")

plt.show()
