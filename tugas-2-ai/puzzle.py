import pygame
import heapq
import time
import os

# Constants
WIDTH, HEIGHT = 400, 400
ROWS, COLS = 3, 3
TILE_SIZE = WIDTH // COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 50, 255)

pygame.init()
screen = pygame.Surface((WIDTH, HEIGHT))
font = pygame.font.Font(None, 50)

# Goal state
GOAL_STATE = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]  # 0 is the empty space

# Create output folder
OUTPUT_FOLDER = "puzzle_images"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def heuristic(state):
    """ Manhattan Distance Heuristic """
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x, goal_y = (value - 1) // 3, (value - 1) % 3
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def get_neighbors(state):
    """ Returns a list of possible next states """
    neighbors = []
    x, y = find_blank(state)
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)

    return neighbors


def a_star_solver(start_state):
    """ A* Algorithm """
    pq = []  # Priority queue (heap)
    heapq.heappush(pq, (heuristic(start_state), 0, start_state, []))
    visited = set()
    explored_states = 0
    all_explored = []

    while pq:
        f, g, state, path = heapq.heappop(pq)
        explored_states += 1

        if state == GOAL_STATE:
            return path, explored_states, all_explored

        state_tuple = tuple(tuple(row) for row in state)
        if state_tuple in visited:
            continue

        visited.add(state_tuple)
        all_explored.append(state)  # Save explored states

        for neighbor in get_neighbors(state):
            if tuple(tuple(row) for row in neighbor) not in visited:
                new_g = g + 1
                new_h = heuristic(neighbor)
                new_f = new_g + new_h
                new_path = path + [neighbor]

                heapq.heappush(pq, (new_f, new_g, neighbor, new_path))

    return None, explored_states, all_explored  # No solution found


def draw_puzzle(state, step, label):
    screen.fill(WHITE)
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                pygame.draw.rect(screen, BLUE, (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                text = font.render(str(state[i][j]), True, WHITE)
                screen.blit(text, (j * TILE_SIZE + TILE_SIZE // 3, i * TILE_SIZE + TILE_SIZE // 3))

    # Save image
    filename = os.path.join(OUTPUT_FOLDER, f"{label}_step_{step}.png")
    pygame.image.save(screen, filename)
    print(f"Saved {filename}")


def visualize_solution(start_state):
    path, explored, all_explored = a_star_solver(start_state)
    if not path:
        print("No solution found!")
        return
    print(f"Total states explored: {explored}")

    # Save explored states
    for step, state in enumerate(all_explored):
        draw_puzzle(state, step, "explored")
        time.sleep(0.1)

    # Save final solution path
    for step, state in enumerate(path):
        draw_puzzle(state, step, "solution")
        time.sleep(0.5)


def main():
    start_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]  # Example start
    visualize_solution(start_state)


if __name__ == "__main__":
    main()
