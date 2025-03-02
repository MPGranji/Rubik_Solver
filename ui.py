import cv2
from cube_state import CubeState
from config import stickers, color_boxes, buttons, textPoints, face_buttons

selected_color = None

def draw_stickers(frame, stickers, name):
    for x, y in stickers[name]:
        cv2.rectangle(frame, (x, y), (x + 30, y + 30), (255, 255, 255), 2)

def draw_preview_stickers(frame, stickers):
    stick = ['front', 'back', 'left', 'right', 'up', 'down']
    for name in stick:
        for x, y in stickers[name]:
            cv2.rectangle(frame, (x, y), (x + 40, y + 40), (255, 255, 255), 2)

    for i, (x, y) in enumerate(color_boxes):
        cv2.rectangle(frame, (x, y), (x + 50, y + 50), (255, 255, 255), 2)
        cv2.rectangle(frame, (x + 1, y + 1), (x + 49, y + 49), list(CubeState().color.values())[i], -1)
        if selected_color == list(CubeState().color.keys())[i]:
            cv2.circle(frame, (x + 25, y + 25), 15, (255, 255, 255), 2)

    cv2.rectangle(frame, buttons['cancel'], (buttons['cancel'][0] + 80, buttons['cancel'][1] + 40), (100, 100, 100), -1)
    cv2.putText(frame, 'Cancel', (buttons['cancel'][0] + 10, buttons['cancel'][1] + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.rectangle(frame, buttons['clear'], (buttons['clear'][0] + 80, buttons['clear'][1] + 40), (100, 100, 100), -1)
    cv2.putText(frame, 'Clear', (buttons['clear'][0] + 15, buttons['clear'][1] + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

def fill_stickers(frame, stickers, sides):
    for side, colors in sides.items():
        num = 0
        for x, y in stickers[side]:
            cv2.rectangle(frame, (x, y), (x + 40, y + 40), CubeState().color[colors[num]], -1)
            num += 1

def texton_preview_stickers(frame, stickers):
    stick = ['front', 'back', 'left', 'right', 'up', 'down']
    font = cv2.FONT_HERSHEY_SIMPLEX
    for name in stick:
        for x, y in stickers[name]:
            sym, x1, y1 = textPoints[name][0][0], textPoints[name][0][1], textPoints[name][0][2]
            cv2.putText(frame, sym, (x1, y1), font, 1, (0, 0, 0), 1, cv2.LINE_AA)
            sym, col, x1, y1 = textPoints[name][1][0], textPoints[name][1][1], textPoints[name][1][2], textPoints[name][1][3]
            cv2.putText(frame, sym, (x1, y1), font, 0.5, col, 1, cv2.LINE_AA)

def mouse_callback_preview(event, x, y, flags, param, cube):
    global selected_color
    valid_faces = ['up', 'right', 'front', 'down', 'left', 'back']  # Chỉ xử lý các mặt hợp lệ
    if event == cv2.EVENT_LBUTTONDOWN:
        for i, (cx, cy) in enumerate(color_boxes):
            if cx <= x <= cx + 40 and cy <= y <= cy + 40:
                selected_color = list(cube.color.keys())[i]
                return

        if buttons['cancel'][0] <= x <= buttons['cancel'][0] + 80 and buttons['cancel'][1] <= y <= buttons['cancel'][1] + 40:
            selected_color = None
            return

        if buttons['clear'][0] <= x <= buttons['clear'][0] + 80 and buttons['clear'][1] <= y <= buttons['clear'][1] + 40:
            for face in cube.state:
                cube.state[face] = ['white'] * 9
            return

        if selected_color:
            for face, positions in stickers.items():
                if face in valid_faces:  # Chỉ xử lý nếu face là mặt hợp lệ
                    for i, (sx, sy) in enumerate(positions):
                        if sx <= x <= sx + 37 and sy <= y <= sy + 37:
                            cube.state[face][i] = selected_color
                            return

def draw_face_buttons(frame):
    for face, (x, y, btn_color) in face_buttons.items():
        cv2.rectangle(frame, (x - 5, y - 5), (x + 75, y + 55), (255, 255, 255), 2)
        cv2.rectangle(frame, (x, y), (x + 70, y + 50), CubeState().color[btn_color], -1)
        cv2.putText(frame, face, (x + 25, y + 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

def mouse_callback_frame(event, x, y, flags, param, cube, current_state):
    if event == cv2.EVENT_LBUTTONDOWN:
        for face, (bx, by, _) in face_buttons.items():
            if bx <= x <= bx + 70 and by <= y <= by + 50:
                print(f"Clicked {face}")
                if face == 'U':
                    cube.state['up'] = current_state
                elif face == 'R':
                    cube.state['right'] = current_state
                elif face == 'F':
                    cube.state['front'] = current_state
                elif face == 'D':
                    cube.state['down'] = current_state
                elif face == 'L':
                    cube.state['left'] = current_state
                elif face == 'B':
                    cube.state['back'] = current_state
                return