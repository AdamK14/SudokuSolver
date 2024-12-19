# Sudoku Solver with Visualization

This Python script generates, solves, and visualizes Sudoku puzzles using the `pygame` library. It creates a fully solved Sudoku grid, removes numbers to generate a playable puzzle, and then solves it while visualizing the process step by step.

## Features
- Generates a fully solved 9x9 Sudoku grid.
- Removes numbers to create a playable Sudoku puzzle.
- Solves the puzzle using a backtracking algorithm.
- Visualizes the solving process with `pygame`.
- Highlights original clues, live numbers during solving, and solved numbers.

## Prerequisites
Make sure you have the following installed:

- **Python 3.6+**
- **pip** (Python package installer)

## Dependencies
The script requires the following Python libraries:

- `pygame` (for visualization)

### Install Dependencies
You can install the required dependency using pip:
```bash
pip install pygame
```

## How to Run
1. Clone or download this repository to your local machine.
2. Navigate to the directory containing the script.
3. Run the script using Python:
   ```bash
   python sudoku_solver.py
   ```

## How It Works

### 1. Generate a Fully Solved Grid
The `create_fully_solved_grid` function generates a complete Sudoku grid using a randomized backtracking algorithm.

### 2. Remove Numbers
The `remove_numbers` function removes numbers from the grid while ensuring the puzzle has a unique solution. This is done by testing the grid's solvability after each number removal.

### 3. Visualize the Puzzle and Solution
The `draw_grid` function uses `pygame` to display the Sudoku grid. Different colors are used to indicate the type of number:
- **Red:** Original clues.
- **Black:** Numbers added during the solving process.
- **Green:** Final solved numbers.

### 4. Solve with Visualization
The `solve_sudoku` function uses a backtracking algorithm to solve the puzzle, visualizing the process in real-time.

## Key Bindings
- The script runs automatically and does not require user interaction. Simply watch the visualization as it generates and solves the Sudoku puzzle.

## File Structure
- `sudoku_solver.py`: Main script containing all functionality.

## Troubleshooting
### Common Issues
1. **`pygame` window does not open**
   - Ensure the `pygame` library is installed correctly. Run `pip install pygame`.
   - Check if your environment supports graphical windows (e.g., running locally rather than on a server).

2. **Performance issues**
   - If the solving visualization is too slow, adjust the `time.sleep()` duration in the `solve_sudoku` function.

### Debugging Tips
- Run the script in a terminal to view any error messages.
- Test `pygame` with a minimal script to ensure it works correctly.

## Example Output
When the script runs, you will see:
1. A generated Sudoku puzzle displayed in a grid.
2. The solving process visualized step by step.
3. The final solved grid highlighted in green.

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

## Acknowledgments
- Thanks to the developers of `pygame` for providing a great library for creating visualizations.

Enjoy solving and visualizing Sudoku puzzles!

