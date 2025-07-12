import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Genetic Algorithm Visualization: Evolving a Population to Find the Optimal Solution

# Function to generate a random population
def generate_population(size, x_range=(-10, 10)):
    return np.random.uniform(x_range[0], x_range[1], size)

# Fitness function (maximize y = -x^2 + 10)
def fitness_function(x):
    return -x**2 + 10

# Selection: Pick the best individuals (higher fitness)
def select_best(population, fitness, num_selected):
    indices = np.argsort(fitness)[-num_selected:]  # Get top individuals
    return population[indices]

# Crossover: Combine two parents to create children
def crossover(parents, num_children):
    children = []
    for _ in range(num_children):
        p1, p2 = np.random.choice(parents, 2, replace=False)
        child = (p1 + p2) / 2  # Simple average crossover
        children.append(child)
    return np.array(children)

# Mutation: Randomly alter some individuals
def mutate(population, mutation_rate=0.1, mutation_strength=1.0):
    for i in range(len(population)):
        if np.random.rand() < mutation_rate:
            population[i] += np.random.uniform(-mutation_strength, mutation_strength)
    return population

# Parameters
pop_size = 20
generations = 20
elite_size = 5  # Number of best individuals to keep
mutation_rate = 0.2

# Initialize population
population = generate_population(pop_size)
history = []

# Evolution process
for gen in range(generations):
    fitness = fitness_function(population)
    best_individuals = select_best(population, fitness, elite_size)
    children = crossover(best_individuals, pop_size - elite_size)
    population = np.concatenate((best_individuals, children))
    population = mutate(population, mutation_rate)
    history.append((population.copy(), fitness_function(population.copy())))

# Animation to visualize the evolution process
fig, ax = plt.subplots()
x = np.linspace(-10, 10, 100)
y = fitness_function(x)
ax.plot(x, y, label="Fitness Function", color='black')

sc = ax.scatter([], [], color='red', label="Population")
ax.legend()
ax.set_xlabel("Solution (x)")
ax.set_ylabel("Fitness (y)")
ax.set_title("Genetic Algorithm Evolution")

def update(frame):
    ax.set_title(f"Generation {frame + 1}")
    sc.set_offsets(np.c_[history[frame][0], history[frame][1]])

ani = animation.FuncAnimation(fig, update, frames=generations, interval=500)
plt.show()
