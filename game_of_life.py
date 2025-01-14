import os
import time
import random

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_grid(grid):
    """Print the grid to the console."""
    for row in grid:
        print(''.join(row))
    print()

def initialize_grid(rows, cols, fill_chance=0.3):
    """
    Initialize the grid with random live ('#') and dead (' ') cells.
    :param rows: Number of rows in the grid.
    :param cols: Number of columns in the grid.
    :param fill_chance: Probability that a cell starts as live.
    :return: The initialized grid.
    """
    return [['#' if random.random() < fill_chance else ' ' for _ in range(cols)] for _ in range(rows)]

def count_neighbors(grid, x, y):
    """
    Count the live neighbors of a cell.
    :param grid: The grid.
    :param x: Row index of the cell.
    :param y: Column index of the cell.
    :return: Number of live neighbors.
    """
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    rows, cols = len(grid), len(grid[0])
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '#':
            count += 1
    return count

def update_grid(grid):
    """
    Update the grid based on the rules of the Game of Life.
    :param grid: The current grid.
    :return: The updated grid.
    """
    rows, cols = len(grid), len(grid[0])
    new_grid = [[' ' for _ in range(cols)] for _ in range(rows)]
    for x in range(rows):
        for y in range(cols):
            live_neighbors = count_neighbors(grid, x, y)
            if grid[x][y] == '#':
                # A live cell survives if it has 2 or 3 live neighbors.
                new_grid[x][y] = '#' if live_neighbors in [2, 3] else ' '
            else:
                # A dead cell becomes alive if it has exactly 3 live neighbors.
                new_grid[x][y] = '#' if live_neighbors == 3 else ' '
    return new_grid

def main():
    """Run the Game of Life in the console."""
    rows, cols = 20, 50  # Adjust size as needed
    grid = initialize_grid(rows, cols)

    try:
        while True:
            clear_screen()
            print_grid(grid)
            grid = update_grid(grid)
            time.sleep(0.3)  # Adjust speed as needed
    except KeyboardInterrupt:
        print("\nGame of Life ended.")

if __name__ == "__main__":
    main()
