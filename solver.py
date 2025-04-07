import kociemba as Cube
import cv2
import numpy as np
from cube_state import CubeState
from ui import draw_preview_stickers, fill_stickers

sign_conv = {
    'green': 'F',
    'white': 'U',
    'blue': 'B',
    'red': 'R',
    'orange': 'L',
    'yellow': 'D'
}

def solve(state, stickers):
    raw = ''.join(sign_conv[j] for i in state for j in state[i])
    try:
        solution = Cube.solve(raw)
        print("Way to solve:", solution)
        return solution.split(' ')
    except Exception as e:
        print(f"Error when: {e}")
        return None


def process_step(step, cube):
    replace = {
        "F": [cube.rotate, 'front'],
        "F2": [cube.rotate, 'front', 'front'],
        "F'": [cube.revrotate, 'front'],
        "U": [cube.rotate, 'up'],
        "U2": [cube.rotate, 'up', 'up'],
        "U'": [cube.revrotate, 'up'],
        "L": [cube.rotate, 'left'],
        "L2": [cube.rotate, 'left', 'left'],
        "L'": [cube.revrotate, 'left'],
        "R": [cube.rotate, 'right'],
        "R2": [cube.rotate, 'right', 'right'],
        "R'": [cube.revrotate, 'right'],
        "D": [cube.rotate, 'down'],
        "D2": [cube.rotate, 'down', 'down'],
        "D'": [cube.revrotate, 'down'],
        "B": [cube.rotate, 'back'],
        "B2": [cube.rotate, 'back', 'back'],
        "B'": [cube.revrotate, 'back']
    }
    moves = replace[step]
    func = moves[0]
    for side in moves[1:]:
        func(side)


def display_solution_window(cube, stickers, steps, step_index):

    solution_window = np.zeros((700, 800, 3), np.uint8)
    draw_preview_stickers(solution_window, stickers)
    fill_stickers(solution_window, stickers, cube.state)

    # Current step in the right corner
    font = cv2.FONT_HERSHEY_SIMPLEX
    if step_index < len(steps):
        current_step = steps[step_index]
        cv2.putText(solution_window, f"Step: {current_step}", (600, 30), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
    else:
        cv2.putText(solution_window, "Done", (600, 30), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Full step
    full_solution = " ".join(steps)
    cv2.putText(solution_window, f"Solution: {full_solution}", (50, 600), font, 0.7, (0, 255, 255), 1, cv2.LINE_AA)

    cv2.imshow('solution', solution_window)