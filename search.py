import pygame
import sys
from queue import PriorityQueue

goal_state = [
    [2, 8, 3],
    [1, 6, 4],
    [7, 0, 5]
]

def misplaced_tiles(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
                count += 1
    return count

def find_blank_tile(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate_new_states(state):
    x, y = find_blank_tile(state)
    possible_moves = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            possible_moves.append(new_state)

    return possible_moves

def a_star_search(initial_state):
    pq = PriorityQueue()
    pq.put((misplaced_tiles(initial_state), 0, initial_state, []))
    visited = set()

    while not pq.empty():
        _, depth, current_state, path = pq.get()

        if current_state == goal_state:
            return path + [current_state]

        visited.add(tuple(map(tuple, current_state)))

        for new_state in generate_new_states(current_state):
            if tuple(map(tuple, new_state)) not in visited:
                pq.put((misplaced_tiles(new_state) + depth + 1, depth + 1, new_state, path + [current_state]))

    return []

def draw_grid(screen, state):
    screen.fill((255, 255, 255))
    font = pygame.font.Font(None, 80)
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                pygame.draw.rect(screen, (0, 128, 255), (j * 100, i * 100, 100, 100))
                text = font.render(str(value), True, (255, 255, 255))
                screen.blit(text, (j * 100 + 35, i * 100 + 25))
    pygame.display.flip()

def visualize_solution(solution):
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("8-Puzzle Solver")

    for state in solution:
        draw_grid(screen, state)
        pygame.time.delay(500)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    pygame.time.delay(2000)
    pygame.quit()

initial_state = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

solution_path = a_star_search(initial_state)
if solution_path:
    visualize_solution(solution_path)
else:
    print("No solution found")
