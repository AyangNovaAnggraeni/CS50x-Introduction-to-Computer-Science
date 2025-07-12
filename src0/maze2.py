import sys
import heapq
import itertools
from PIL import Image, ImageDraw, ImageFont

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

class GreedyFrontier():
    def __init__(self, goal):
        self.goal = goal
        self.frontier = []
        self.counter = itertools.count()

    def heuristic(self, state):
        return abs(state[0] - self.goal[0]) + abs(state[1] - self.goal[1])

    def add(self, node):
        priority = self.heuristic(node.state)
        count = next(self.counter)
        heapq.heappush(self.frontier, (priority, count, node))

    def empty(self):
        return len(self.frontier) == 0

    def contains_state(self, state):
        return any(node.state == state for _, _, node in self.frontier)

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        _, _, node = heapq.heappop(self.frontier)
        return node

class AStarFrontier():
    def __init__(self, goal):
        self.goal = goal
        self.frontier = []
        self.counter = itertools.count()
        self.g_scores = {}

    def heuristic(self, state):
        return abs(state[0] - self.goal[0]) + abs(state[1] - self.goal[1])

    def add(self, node, g):
        f = g + self.heuristic(node.state)
        count = next(self.counter)
        heapq.heappush(self.frontier, (f, count, node))
        self.g_scores[node.state] = g

    def empty(self):
        return len(self.frontier) == 0

    def contains_state(self, state):
        return any(node.state == state for _, _, node in self.frontier)

    def get_g(self, state):
        return self.g_scores.get(state, float("inf"))

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        _, _, node = heapq.heappop(self.frontier)
        return node

class Maze():
    def __init__(self, filename):
        with open(filename) as f:
            contents = f.read()

        if contents.count("A") != 1 or contents.count("B") != 1:
            raise Exception("Maze must have exactly one start point and one goal.")

        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    char = contents[i][j]
                    if char == "A":
                        self.start = (i, j)
                        row.append(False)
                    elif char == "B":
                        self.goal = (i, j)
                        row.append(False)
                    elif char == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)

        self.solution = None
        self.num_explored = 0

    def print(self):
        solution = self.solution[1] if self.solution is not None else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("█", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("B", end="")
                elif solution is not None and (i, j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()

    def neighbors(self, state):
        row, col = state
        directions = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]
        result = []
        for action, (r, c) in directions:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result

    def solve(self, algorithm="greedy"):
        self.algorithm = algorithm
        start = Node(state=self.start, parent=None, action=None)
        self.g_scores = {}
        if algorithm == "greedy":
            frontier = GreedyFrontier(goal=self.goal)
            frontier.add(start)
        elif algorithm == "astar":
            self.g_scores[start.state] = 0
            frontier = AStarFrontier(goal=self.goal)
            frontier.add(start, g=0)
        else:
            raise Exception("Unsupported algorithm")

        self.explored = set()
        self.num_explored = 0

        while True:
            if frontier.empty():
                raise Exception("no solution")

            node = frontier.remove()
            self.num_explored += 1

            if node.state == self.goal:
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return

            self.explored.add(node.state)

            for action, state in self.neighbors(node.state):
                g = 0
                if algorithm == "astar":
                    g = frontier.get_g(node.state) + 1
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action)
                    if algorithm == "greedy":
                        frontier.add(child)
                    elif algorithm == "astar":
                        self.g_scores[state] = g
                        frontier.add(child, g)

    def output_image(self, filename, show_solution=True, show_explored=False, show_heuristic=False):
        cell_size = 50
        cell_border = 2

        img = Image.new("RGBA", (self.width * cell_size, self.height * cell_size), "black")
        draw = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype("arial.ttf", 12)
        except:
            font = ImageFont.load_default()

        solution = self.solution[1] if self.solution is not None else None
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    fill = (40, 40, 40)
                elif (i, j) == self.start:
                    fill = (255, 0, 0)
                elif (i, j) == self.goal:
                    fill = (0, 171, 28)
                elif solution is not None and show_solution and (i, j) in solution:
                    fill = (220, 235, 113)
                elif solution is not None and show_explored and (i, j) in self.explored:
                    fill = (212, 97, 85)
                else:
                    fill = (237, 240, 252)

                draw.rectangle(
                    ([(j * cell_size + cell_border, i * cell_size + cell_border),
                      ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)]),
                    fill=fill
                )

                if show_heuristic and not col:
                    h = abs(i - self.goal[0]) + abs(j - self.goal[1])
                    if hasattr(self, 'algorithm') and self.algorithm == "astar":
                        g = self.g_scores.get((i, j), "-")
                        f = h + g if g != "-" else "-"
                        text = f"h:{h}\ng:{g}\nf:{f}"
                    else:
                        text = f"h:{h}"


        img.save(filename)

# MAIN EXECUTION

if len(sys.argv) != 2:
    sys.exit("Usage: python maze.py maze.txt")

m = Maze(sys.argv[1])
print("Maze:")
m.print()

print("Solving with Greedy Best-First Search...")
m.solve(algorithm="greedy")
print("States Explored (Greedy):", m.num_explored)
print("Solution Length:", len(m.solution[1]) if m.solution else "No solution")
m.print()
m.output_image("greedy.png", show_solution=True, show_explored=True, show_heuristic=True)

print("Solving with A* Search...")
m.solve(algorithm="astar")
print("States Explored (A*):", m.num_explored)
print("Solution Length:", len(m.solution[1]) if m.solution else "No solution")
m.print()
m.output_image("astar.png", show_solution=True, show_explored=True, show_heuristic=True)
