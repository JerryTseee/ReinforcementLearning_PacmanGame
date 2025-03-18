import os, sys
def read_layout_problem(file_path):
    with open(file_path, 'r') as f:
        lines = [line.rstrip('\n') for line in f]
    
    seed = int(lines[0].split(' ')[-1])
    layout = lines[1:]
    pacman = None
    ghost = None
    food = set()
    walls = set()
    for i in range(len(layout)):
        row = layout[i]
        for j in range(len(row)):
            char = row[j]
            if char == 'P':
                pacman = (i, j) # start to read from upper left corner, vertical: i, horizontal: j
            elif char == 'W':
                ghost = (i, j)
            elif char == '.':
                food.add((i, j))
            elif char == '%':
                walls.add((i, j))

    return {
        'seed': seed,
        'pacman': pacman,
        'ghost': ghost,
        'food': food,
        'walls': walls
    }

def write_layout_solution(food, walls, ghost, pacman):
    """
    Converts the parsed layout data back into a layout file format.
    
    Args:
        file_path (str): Path to save the layout file.
        food (set): Set of food coordinates.
        walls (set): Set of wall coordinates.
        ghost (tuple): Ghost position (row, col).
        pacman (tuple): Pacman position (row, col).
    """
    # Determine the dimensions of the layout
    max_row = max(row for row, col in walls)
    max_col = max(col for row, col in walls)

    # Initialize the layout grid
    layout = []
    for i in range(max_row + 1):
        row = []
        for j in range(max_col + 1):
            if (i, j) == pacman:
                row.append('P')
            elif (i, j) == ghost:
                row.append('W')
            elif (i, j) in food:
                row.append('.')
            elif (i, j) in walls:
                row.append('%')
            else:
                row.append(' ')  # Empty space
        layout.append(''.join(row))

    
    # Write the layout to the file
    return '\n'.join(layout)



if __name__ == "__main__":
    if len(sys.argv) == 3:
        problem_id, test_case_id = sys.argv[1], sys.argv[2]
        problem = read_layout_problem(os.path.join('test_cases','p'+problem_id, test_case_id+'.prob'))
        print(problem)
    else:
        print('Error: I need exactly 2 arguments!')