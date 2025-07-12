import matplotlib.pyplot as plt
import networkx as nx
import os
import imageio

# Graph representation of the map
graph = {
    "Arad": ["Zerind", "Timisoara", "Sibiu"],
    "Zerind": ["Arad", "Oradea"],
    "Oradea": ["Zerind", "Sibiu"],
    "Timisoara": ["Arad", "Lugoj"],
    "Lugoj": ["Timisoara", "Mehadia"],
    "Mehadia": ["Lugoj", "Dobreta"],
    "Dobreta": ["Mehadia", "Craiova"],
    "Craiova": ["Dobreta", "Rimnicu Vilcea", "Pitesti"],
    "Sibiu": ["Arad", "Oradea", "Fagaras", "Rimnicu Vilcea"],
    "Fagaras": ["Sibiu", "Bucharest"],
    "Rimnicu Vilcea": ["Sibiu", "Craiova", "Pitesti"],
    "Pitesti": ["Rimnicu Vilcea", "Craiova", "Bucharest"],
    "Bucharest": ["Fagaras", "Pitesti", "Urziceni", "Giurgiu"],
    "Urziceni": ["Bucharest", "Hirsova", "Vaslui"],
    "Hirsova": ["Urziceni", "Eforie"],
    "Eforie": ["Hirsova"],
    "Vaslui": ["Urziceni", "Iasi"],
    "Iasi": ["Vaslui", "Neamt"],
    "Neamt": ["Iasi"],
    "Giurgiu": ["Bucharest"]
}

# Create a folder to store visualization frames
os.makedirs("frames", exist_ok=True)

# Function to visualize the graph
def draw_graph(explored, path, step, algorithm):
    plt.figure(figsize=(10, 6))
    G = nx.Graph()

    # Add edges to the graph
    for node in graph:
        for neighbor in graph[node]:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G, seed=42)  # Position nodes for visualization

    # Draw all nodes
    nx.draw(G, pos, with_labels=True, node_color="lightgray", edge_color="gray", node_size=2000, font_size=10)

    # Highlight explored nodes
    nx.draw_networkx_nodes(G, pos, nodelist=explored, node_color="orange")

    # Highlight final path
    nx.draw_networkx_nodes(G, pos, nodelist=path, node_color="red")

    plt.title(f"{algorithm} Step {step}")

    # Save each step as an image
    plt.savefig(f"frames/{algorithm.lower()}_step_{step}.png")
    plt.close()


# BFS Algorithm with visualization
def bfs(start, goal):
    queue = [[start]]
    explored = set()
    step = 0

    while queue:
        path = queue.pop(0)
        node = path[-1]

        # Visualization step
        draw_graph(list(explored), path, step, "BFS")
        step += 1

        if node == goal:
            return path

        if node not in explored:
            explored.add(node)
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None


# DFS Algorithm with visualization
def dfs(start, goal):
    stack = [[start]]
    explored = set()
    step = 0

    while stack:
        path = stack.pop()
        node = path[-1]

        # Visualization step
        draw_graph(list(explored), path, step, "DFS")
        step += 1

        if node == goal:
            return path

        if node not in explored:
            explored.add(node)
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)

    return None


# Run BFS and DFS
bfs_path = bfs("Arad", "Bucharest")
dfs_path = dfs("Arad", "Bucharest")

print("BFS Path:", bfs_path)
print("DFS Path:", dfs_path)
