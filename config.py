from utils import generate_grid

stickers = {
    'main': generate_grid(200, 120, 100, 100),
    'current': generate_grid(20, 20, 34, 34),
    'preview': generate_grid(20, 130, 34, 34),
    'left': generate_grid(50, 280, 44, 44),
    'front': generate_grid(188, 280, 44, 44),
    'right': generate_grid(326, 280, 44, 44),
    'up': generate_grid(188, 128, 44, 44),
    'down': generate_grid(188, 434, 44, 44),
    'back': generate_grid(464, 280, 44, 44),
}

color_boxes = [(50 + i * 60, 35) for i in range(6)]
buttons = {'cancel': (450, 35), 'clear': (550, 35)}

textPoints = {
    'up': [['U', 242, 202], ['W', (255, 255, 255), 260, 208]],
    'right': [['R', 380, 354], ['R', (0, 0, 255), 398, 360]],
    'front': [['F', 242, 354], ['G', (0, 255, 0), 260, 360]],
    'down': [['D', 242, 508], ['Y', (0, 255, 255), 260, 514]],
    'left': [['L', 104, 354], ['O', (0, 165, 255), 122, 360]],
    'back': [['B', 518, 354], ['B', (255, 0, 0), 536, 360]],
}

face_buttons = {
    'U': (550, 50, 'white'),
    'R': (550, 110, 'red'),
    'F': (550, 170, 'green'),
    'D': (550, 230, 'yellow'),
    'L': (550, 290, 'orange'),
    'B': (550, 350, 'blue')
}