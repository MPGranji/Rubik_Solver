import cv2
import numpy as np
import colorama
from cube_state import CubeState
from color_detection import color_detect_kmeans
from ui import draw_stickers, draw_preview_stickers, fill_stickers, texton_preview_stickers, mouse_callback_preview, \
    draw_face_buttons, mouse_callback_frame
from solver import solve, process_step, display_solution_window
from utils import print_intro
from config import stickers

colorama.init()


def apply_white_balance(img):

    b, g, r = cv2.split(img)

    avg_b = np.mean(b)
    avg_g = np.mean(g)
    avg_r = np.mean(r)

    if avg_g == 0:
        return img
    scale_b = avg_g / avg_b if avg_b != 0 else 1
    scale_r = avg_g / avg_r if avg_r != 0 else 1

    b = np.clip(b * scale_b, 0, 255).astype(np.uint8)
    r = np.clip(r * scale_r, 0, 255).astype(np.uint8)

    return cv2.merge([b, g, r])


if __name__ == "__main__":
    print_intro()

    cap = cv2.VideoCapture(0)
    cv2.namedWindow('frame')
    preview = np.zeros((700, 800, 3), np.uint8)

    cube = CubeState()
    current_state = []
    solution_steps = None
    step_index = 0
    solution_active = False

    while True:
        ret, img = cap.read()
        if not ret:
            print("Can't read from camera")
            break

        img = apply_white_balance(img)

        #  Lọc Gaussian
        img = cv2.GaussianBlur(img, (5, 5), 0)
        frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = np.zeros(frame.shape, dtype=np.uint8)

        draw_stickers(img, stickers, 'main')
        draw_stickers(img, stickers, 'current')
        draw_preview_stickers(preview, stickers)
        fill_stickers(preview, stickers, cube.state)
        texton_preview_stickers(preview, stickers)
        draw_face_buttons(img)

        current_state = []
        pixel_values = []
        for i in range(9):
            x, y = stickers['main'][i][0] + 20, stickers['main'][i][1] + 20
            # 15x15 pixel
            region = frame[max(0, y - 7):y + 8, max(0, x - 7):x + 8]
            if region.size > 0:

                hsv_value = np.mean(region, axis=(0, 1))
                pixel_values.append(hsv_value)
            else:
                pixel_values.append([0, 0, 0])

        color_names = color_detect_kmeans(pixel_values)

        #update current state
        a = 0
        for x, y in stickers['current']:
            color_name = color_names[a]

            cv2.rectangle(img, (x, y), (x + 30, y + 30), cube.color[color_name], -1)
            a += 1
            current_state.append(color_name)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
        elif k == ord('u'):
            cube.state['up'] = current_state
        elif k == ord('r'):
            cube.state['right'] = current_state
        elif k == ord('l'):
            cube.state['left'] = current_state
        elif k == ord('d'):
            cube.state['down'] = current_state
        elif k == ord('f'):
            cube.state['front'] = current_state
        elif k == ord('b'):
            cube.state['back'] = current_state
        elif k == ord('\r'):
            if not solution_active:
                solution_steps = solve(cube.state, stickers)
                if solution_steps:
                    step_index = 0
                    solution_active = True
                    display_solution_window(cube, stickers, solution_steps, step_index)
            elif solution_active and step_index < len(solution_steps):
                process_step(solution_steps[step_index], cube)
                step_index += 1
                display_solution_window(cube, stickers, solution_steps, step_index)
            elif solution_active and step_index >= len(solution_steps):
                cv2.destroyWindow('solution')
                solution_active = False
                solution_steps = None
                step_index = 0

        cv2.imshow('preview', preview)
        cv2.setMouseCallback('preview',
                             lambda event, x, y, flags, param: mouse_callback_preview(event, x, y, flags, param, cube))
        cv2.imshow('frame', img)
        cv2.setMouseCallback('frame',
                             lambda event, x, y, flags, param: mouse_callback_frame(event, x, y, flags, param, cube,
                                                                                    current_state))

    cap.release()
    cv2.destroyAllWindows()