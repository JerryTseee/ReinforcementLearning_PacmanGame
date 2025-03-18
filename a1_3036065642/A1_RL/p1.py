import sys
import random
from collections import defaultdict
import math
import grader
import parse

"""
Q-Learning Pacman Assignment - Part A

Objective: Implement a random Pacman player that competes against a single random Ghost.

Part 1: Familiarize Yourself with the Parser and Data Structure
- Explore the provided parser and understand the data structures used in the assignment. This will help you effectively manipulate game states.
Part 2: Implement Random Actions
 - Create the get_action method that allows Pacman to select random valid actions during the game.

Testing
To test your implementation, run the following command in your terminal:
- python p1.py 1


"""


class GameState:
    def __init__(self, walls, food, ghost_pos):
        self.walls = walls
        self.food = food
        self.ghost_pos = ghost_pos


def get_position(pos, action):
    direction_mapping = {
        'N': (-1, 0),
        'S': (1, 0),
        'W': (0, -1),
        'E': (0, 1)
    }
    dx, dy = direction_mapping[action]
    return (pos[0] + dx, pos[1] + dy)


class BasicPacman:
    def __init__(self, pos):
        self.pos = pos

    def get_legal_actions(self, state):
        """
        get legal action from the state
        """
        legal_actions = [d for d in ['N', 'S', 'W', 'E'] if get_position(self.pos, d) not in state.walls]
        return legal_actions

    def get_action(self, state):
        """
        TODO: a simple random choice
        return action
        """
        # Student implementation here
        ###############################

        legal_actions = self.get_legal_actions(state)
        if legal_actions:
            action = random.choice(legal_actions)
        else:
            action = None
        
        ###############################
        return action


    def set_new_position(self, action):
        """
        TODO: update position according to the action
        return the update position
        """
        # Student implementation here
        ###############################
        if action:
            self.pos = get_position(self.pos, action) # update new position
        ###############################
        return self.pos


def run_game(walls, food, ghost_pos, pacman, seed):
    output = [f"seed: {seed}", str(0), parse.write_layout_solution(food, walls, ghost_pos, pacman.pos)]
    step = 0

    while True:
        state = GameState(walls, food, ghost_pos)

        # Pacman action
        action = pacman.get_action(state)
        new_pos = pacman.set_new_position(action)
        
        if new_pos in food:
            food.remove(new_pos)

        step += 1
        output.append(f"{step}: P moving {action}")
        output.append(parse.write_layout_solution(food, walls, ghost_pos, pacman.pos))

        if pacman.pos == ghost_pos or not food:
            winner = 'Pacman' if not food else "Ghost"
            output.append(f"WIN: {winner}")  # Log the winner
            return winner, '\n'.join(output)

        # Ghost action
        ghost_actions = [d for d in ['N', 'S', 'W', 'E'] if get_position(ghost_pos, d) not in walls]
        ghost_move = random.choice(ghost_actions)
        ghost_pos = (
            ghost_pos[0] + {'N': -1, 'S': 1}.get(ghost_move, 0),
            ghost_pos[1] + {'W': -1, 'E': 1}.get(ghost_move, 0)
        )

        step += 1
        output.append(f"W moving {ghost_move}")  # Log the action
        output.append(parse.write_layout_solution(food, walls, ghost_pos, pacman.pos))

        if pacman.pos == ghost_pos or not food:
            winner = 'Pacman' if not food else "Ghost"
            output.append(f"WIN: {winner}")  # Log the winner
            return winner, '\n'.join(output)


def random_play_single_ghost(problem):
    random.seed(problem['seed'])
    walls = problem['walls']
    food = set(problem['food'])
    ghost_pos = problem['ghost']
    pacman = BasicPacman(pos=problem['pacman'])

    _, solution = run_game(walls, food, ghost_pos, pacman, problem['seed'])
    return solution


if __name__ == "__main__":
    test_case_id = int(sys.argv[1])
    problem_id = 1
    grader.grade(problem_id, test_case_id, random_play_single_ghost, parse.read_layout_problem)