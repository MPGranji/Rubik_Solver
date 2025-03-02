import cv2
import numpy as np
import time
import colorama
from cube_state import CubeState
from color_detection import color_detect
from ui import draw_stickers, draw_preview_stickers, fill_stickers, texton_preview_stickers, mouse_callback_preview, draw_face_buttons, mouse_callback_frame
from solver import solve, process_step, display_solution_window
from utils import GREEN, RED, MAGENTA, RESET, print_intro
from config import stickers

colorama.init()

if __name__ == "__main__":
    print_intro()

    cap = cv2.VideoCapture(0)
    cv2.namedWindow('frame')
    preview = np.zeros((700, 800, 3), np.uint8)

    cube = CubeState()
    current_state = []
    solution_steps = None  # Lưu danh sách các bước giải
    step_index = 0  # Chỉ số bước hiện tại
    solution_active = False  # Kiểm tra xem cửa sổ solution đang mở không

    while True:
        hsv = []
        ret, img = cap.read()
        if not ret:
            print("Không thể đọc từ camera!")
            break

        frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = np.zeros(frame.shape, dtype=np.uint8)

        # Vẽ giao diện
        draw_stickers(img, stickers, 'main')
        draw_stickers(img, stickers, 'current')
        draw_preview_stickers(preview, stickers)
        fill_stickers(preview, stickers, cube.state)
        texton_preview_stickers(preview, stickers)
        draw_face_buttons(img)

        # Xử lý màu từ camera
        current_state = []  # Reset current_state mỗi khung hình
        for i in range(9):
            hsv.append(frame[stickers['main'][i][1] + 20][stickers['main'][i][0] + 20])

        a = 0
        for x, y in stickers['current']:
            color_name = color_detect(hsv[a][0], hsv[a][1], hsv[a][2])
            cv2.rectangle(img, (x, y), (x + 30, y + 30), cube.color[color_name], -1)
            a += 1
            current_state.append(color_name)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:  # Nhấn ESC để thoát toàn bộ chương trình
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
        elif k == ord('\r'):  # Nhấn Enter
            if not solution_active:  # Lần đầu nhấn Enter: Giải và mở solution window
                solution_steps = solve(cube.state, stickers)
                if solution_steps:
                    step_index = 0
                    solution_active = True
                    display_solution_window(cube, stickers, solution_steps, step_index)
            elif solution_active and step_index < len(solution_steps):  # Các lần Enter tiếp theo: Xoay từng bước
                process_step(solution_steps[step_index], cube)
                step_index += 1
                display_solution_window(cube, stickers, solution_steps, step_index)
            elif solution_active and step_index >= len(solution_steps):  # Khi hoàn thành: Đóng solution window
                cv2.destroyWindow('solution')
                solution_active = False
                solution_steps = None
                step_index = 0

        cv2.imshow('preview', preview)
        cv2.setMouseCallback('preview', lambda event, x, y, flags, param: mouse_callback_preview(event, x, y, flags, param, cube))
        cv2.imshow('frame', img)
        cv2.setMouseCallback('frame', lambda event, x, y, flags, param: mouse_callback_frame(event, x, y, flags, param, cube, current_state))

    cap.release()
    cv2.destroyAllWindows()