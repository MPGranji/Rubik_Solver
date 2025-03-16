# Rubik_Solver

A Python-based Rubik's Cube solver using OpenCV for color detection and Kociemba's algorithm for generating solutions. This project provides a demo to scan a Rubik's Cube via webcam, detect its colors, and display a step-by-step solution.

## Getting Started

### Prerequisites

To run this project, you need to install the following dependencies:

- **Python 3.x**
- **OpenCV**: For image processing and webcam integration (`pip install opencv-python`)
- **Kociemba**: For solving the Rubik's Cube (`pip install kociemba`)

<h3>Prerequisites</h3> Before running the project, ensure you have the following installed: - <strong>Python 3.x</strong>: Download from <a href="https://www.python.org/downloads/">here</a>. - A webcam connected to your computer. <h3>Install Dependencies</h3>
Install the required libraries:
bash

Thu gọn

Bọc lại

Sao chép
pip install opencv-python kociemba
(Optional) Use an IDE like <strong>PyCharm</strong> or <strong>Visual Studio Code</strong> for a better development experience.

<h3>Run the Application</h3>
Launch the program:

bash

Thu gọn

Bọc lại

Sao chép
python main.py
This opens the Frame window for scanning.

Scan the Cube:
Place a face of the Rubik's Cube in the webcam's scanning area.
Press the corresponding keys (or buttons if using a front-facing camera) to assign colors:
U (Up): White
D (Down): Yellow
L (Left): Orange
R (Right): Red
F (Front): Green
B (Back): Blue
Check the Preview window to ensure all faces are scanned correctly.
Solve the Cube:
Once all six faces are scanned, press Enter to view the solution in the Solution window.
Tips:
Ensure good lighting and camera focus for accurate color detection.
Verify the cube state in the Preview window before solving.
</details>
Cube Face Definitions
The solver uses standard Rubik's Cube notation with the following color assignments:

F (Front): Green
B (Back): Blue
U (Up): White
D (Down): Yellow
L (Left): Orange
R (Right): Red
Project Structure
main.py: Integrates scanning, state management, and solving logic.
cube_state.py: Manages the cube's state and rotations.
ui.py: Renders the Frame and Preview windows.
