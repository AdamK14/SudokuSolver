import pygame, random, time

WIDTH, HEIGHT = 540, 540
CELL_SIZE = WIDTH // 9
BACKGROUND_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
RANDOM_NUMBER_COLOR = (255, 0, 0)
LIVE_NUMBER_COLOR = (0, 0, 0)
SOLVED_NUMBER_COLOR = (0, 255, 0)
FPS = 30

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")
font = pygame.font.SysFont("Calibri", 40)

def draw_grid(grid, original_clues = None, final = False):
    screen.fill(BACKGROUND_COLOR)

    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), 4)
            pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), 4)
        else:
            pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), 2)
            pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), 2)
    
    for row in range(9):
        for col in range(9):
            if grid[row][col] != 0:
                if original_clues and (row, col) in original_clues:
                    color = RANDOM_NUMBER_COLOR
                elif final:
                    color = SOLVED_NUMBER_COLOR
                else:
                    color = LIVE_NUMBER_COLOR
                text = font.render(str(grid[row][col]), True, color)
                screen.blit(text, (col * CELL_SIZE + 15, row * CELL_SIZE + 10))
    
    pygame.display.update()

def is_valid(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    
    return True

def find_empty_cell(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None

def solve_sudoku(grid, visualize = False, original_clues = None):
    empty = find_empty_cell(grid)
    if not empty:
        return True
    
    row, col = empty
    nums = list(range(1, 10))
    random.shuffle(nums)
    
    for num in nums:
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            if visualize:
                draw_grid(grid, original_clues)
                time.sleep(0.005)
            
            if solve_sudoku(grid, visualize, original_clues):
                return True
            
            grid[row][col] = 0
            if visualize:
                draw_grid(grid, original_clues)
                time.sleep(0.005)
    
    return False

def count_solutions(grid):
    solutions = [0]
    
    def backtrack():
        cell = find_empty_cell(grid)
        if not cell:
            solutions[0] += 1
            return
        
        row, col = cell
        for num in range(1, 10):
            if is_valid(grid, row, col, num):
                grid[row][col] = num
                backtrack()
                grid[row][col] = 0
    
    backtrack()
    return solutions[0]

def create_fully_solved_grid():
    grid = [[0] * 9 for _ in range(9)]
    solve_sudoku(grid)
    return grid

def remove_numbers(grid):
    attempts = 5
    while attempts > 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        while grid[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        
        backup = grid[row][col]
        grid[row][col] = 0
        
        grid_copy = [row[:] for row in grid]
        if count_solutions(grid_copy) != 1:
            grid[row][col] = backup
            attempts -= 1
    
    return grid

def main():
    running = True
    clock = pygame.time.Clock()  # To control the frame rate

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Close the program when the user quits
        
        solved_grid = create_fully_solved_grid()
        unsolved_grid = remove_numbers(solved_grid)
        original_clues = {(row, col) for row in range(9) for col in range(9) if unsolved_grid[row][col] != 0}
        
        draw_grid(unsolved_grid, original_clues)
        time.sleep(3)
        
        solve_sudoku(unsolved_grid, visualize=True, original_clues=original_clues)
        draw_grid(unsolved_grid, original_clues, final=True)
        time.sleep(3)

        clock.tick(FPS)  # Limit the frame rate to the desired FPS

    pygame.quit()  # Ensure pygame exits properly

main()