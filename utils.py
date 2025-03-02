import colorama
import time

GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET
RED = colorama.Fore.RED
MAGENTA = colorama.Fore.MAGENTA

def generate_grid(start_x, start_y, step_x, step_y):
    return [[start_x + i * step_x, start_y + j * step_y] for j in range(3) for i in range(3)]

def print_intro():
    print(rf"{RED}          ______    __     __    _________    _________                                   ___ ___ ___                 ")
    print(rf"{GREEN}         |  ____|  |  |   |  |  |  _____  |  | ________|                                 |   |   |   |            ")
    print(rf"{GREEN}         | |       |  |   |  |  | |_____| |  | |____                                     |___|___|___|               ")
    print(rf"{GREEN}         | |       |  |   |  |  |  _____  |  |  ____|                                    |   |   |   |            ")
    print(rf"{GREEN}         | |____   |  |___|  |  | |_____| |  | |_______                                  |_N_|_I_|_C_|            ")
    print(rf"{GREEN}         |______|  |_________|  |_________|  |_________|                                 |   |   |   |            ")
    print(rf"{RED}                                                                                         |___|___|___|                     ")
    print(rf"{RED}                            _______    _________    __      ___      ___   ________    ________         ")
    print(rf"{GREEN}                           |  _____|  |   ___   |  |  |     \  \    /  /  |  ______|  |  _____ |    ")
    print(rf"{GREEN}                           | |_____   |  |   |  |  |  |      \  \  /  /   | |____     |  ______|    ")
    print(rf"{GREEN}                           |_____  |  |  |   |  |  |  |       \  \/  /    |  ____|    |   \  \        ")
    print(rf"{GREEN}                            _____| |  |  |___|  |  |  |____    \    /     | |______   |  | \  \       ")
    print(rf"{RED}                           |_______|  |_________|  |_______|    \__/      |________|  |__|  \__\      ")
    time.sleep(2)
    print("")
    print("")
    print(f"{MAGENTA}Please refer preview window for which side you have scanned and which color should be in centre on each side.")