class CubeState:
    def __init__(self):
        self.state = {
            'up': ['white'] * 9,
            'right': ['white'] * 9,
            'front': ['white'] * 9,
            'down': ['white'] * 9,
            'left': ['white'] * 9,
            'back': ['white'] * 9
        }
        self.state['right'][4] = 'red'
        self.state['front'][4] = 'green'
        self.state['down'][4] = 'yellow'
        self.state['left'][4] = 'orange'
        self.state['back'][4] = 'blue'
        self.color = {
            'red': (0, 0, 255),
            'orange': (0, 165, 255),
            'blue': (255, 0, 0),
            'green': (0, 255, 0),
            'white': (255, 255, 255),
            'yellow': (0, 255, 255)
        }

    def rotate(self, side):
        main = self.state[side]
        front = self.state['front']
        left = self.state['left']
        right = self.state['right']
        up = self.state['up']
        down = self.state['down']
        back = self.state['back']

        if side == 'front':
            left[2], left[5], left[8], up[6], up[7], up[8], right[0], right[3], right[6], down[0], down[1], down[2] = down[
                0], down[1], down[2], left[8], left[5], left[2], up[6], up[7], up[8], right[6], right[3], right[0]
        elif side == 'up':
            left[0], left[1], left[2], back[0], back[1], back[2], right[0], right[1], right[2], front[0], front[1], front[
                2] = front[0], front[1], front[2], left[0], left[1], left[2], back[0], back[1], back[2], right[0], right[1], right[2]
        elif side == 'down':
            left[6], left[7], left[8], back[6], back[7], back[8], right[6], right[7], right[8], front[6], front[7], front[
                8] = back[6], back[7], back[8], right[6], right[7], right[8], front[6], front[7], front[8], left[6], left[
                7], left[8]
        elif side == 'back':
            left[0], left[3], left[6], up[0], up[1], up[2], right[2], right[5], right[8], down[6], down[7], down[8] = up[2], \
            up[1], up[0], right[2], right[5], right[8], down[8], down[7], down[6], left[0], left[3], left[6]
        elif side == 'left':
            front[0], front[3], front[6], down[0], down[3], down[6], back[2], back[5], back[8], up[0], up[3], up[6] = up[0], \
            up[3], up[6], front[0], front[3], front[6], down[6], down[3], down[0], back[8], back[5], back[2]
        elif side == 'right':
            front[2], front[5], front[8], down[2], down[5], down[8], back[0], back[3], back[6], up[2], up[5], up[8] = down[
                2], down[5], down[8], back[6], back[3], back[0], up[8], up[5], up[2], front[2], front[5], front[8]

        main[0], main[1], main[2], main[3], main[4], main[5], main[6], main[7], main[8] = main[6], main[3], main[0], main[
            7], main[4], main[1], main[8], main[5], main[2]

    def revrotate(self, side):
        main = self.state[side]
        front = self.state['front']
        left = self.state['left']
        right = self.state['right']
        up = self.state['up']
        down = self.state['down']
        back = self.state['back']

        if side == 'front':
            left[2], left[5], left[8], up[6], up[7], up[8], right[0], right[3], right[6], down[0], down[1], down[2] = up[8], \
            up[7], up[6], right[0], right[3], right[6], down[2], down[1], down[0], left[2], left[5], left[8]
        elif side == 'up':
            left[0], left[1], left[2], back[0], back[1], back[2], right[0], right[1], right[2], front[0], front[1], front[
                2] = back[0], back[1], back[2], right[0], right[1], right[2], front[0], front[1], front[2], left[0], left[
                1], left[2]
        elif side == 'down':
            left[6], left[7], left[8], back[6], back[7], back[8], right[6], right[7], right[8], front[6], front[7], front[
                8] = front[6], front[7], front[8], left[6], left[7], left[8], back[6], back[7], back[8], right[6], right[7], \
            right[8]
        elif side == 'back':
            left[0], left[3], left[6], up[0], up[1], up[2], right[2], right[5], right[8], down[6], down[7], down[8] = down[
                6], down[7], down[8], left[6], left[3], left[0], up[0], up[1], up[2], right[8], right[5], right[2]
        elif side == 'left':
            front[0], front[3], front[6], down[0], down[3], down[6], back[2], back[5], back[8], up[0], up[3], up[6] = down[
                0], down[3], down[6], back[8], back[5], back[2], up[0], up[3], up[6], front[0], front[3], front[6]
        elif side == 'right':
            front[2], front[5], front[8], down[2], down[5], down[8], back[0], back[3], back[6], up[2], up[5], up[8] = up[2], \
            up[5], up[8], front[2], front[5], front[8], down[8], down[5], down[2], back[6], back[3], back[0]

        main[0], main[1], main[2], main[3], main[4], main[5], main[6], main[7], main[8] = main[2], main[5], main[8], main[
            1], main[4], main[7], main[0], main[3], main[6]