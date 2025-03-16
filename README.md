# Rubik_Solver

A Python-based Rubik's Cube solver using OpenCV for color detection and Kociemba's algorithm for generating solutions. This project provides a demo to scan a Rubik's Cube via webcam, detect its colors, and display a step-by-step solution.

## Getting Started

### Prerequisites
To run this project, you need to install the following dependencies:
- **Python 3.x**
- **OpenCV**: For image processing and webcam integration (`pip install opencv-python`)
- **Kociemba**: For solving the Rubik's Cube (`pip install kociemba`)

### Installation
1. Clone or download the source code from the repository:
git clone https://github.com/MPGranji/Rubik_Solver.git
cd Rubik_Solver

text

Thu gọn

Bọc lại

Sao chép
2. Install the required libraries:
pip install opencv-python kociemba

text

Thu gọn

Bọc lại

Sao chép
3. Ensure a webcam is connected to your computer.

### Usage
1. **Launch the Program**:
Run the main script:
python main.py

text

Thu gọn

Bọc lại

Sao chép
This opens the Frame window for scanning.

2. **Scan the Cube**:
- Place a face of the Rubik's Cube in the scanning area of the webcam.
- Assign colors to each face by pressing the corresponding keys (or buttons if using a front-facing camera):
  - `U` (Up): White
  - `D` (Down): Yellow
  - `L` (Left): Orange
  - `R` (Right): Red
  - `F` (Front): Green
  - `B` (Back): Blue
- Check the Preview window to ensure all faces are scanned correctly.

3. **Solve the Cube**:
- Once all six faces are scanned, press `Enter` to generate and view the solution in the Solution window.

4. **Tips**:
- Ensure good lighting and camera focus for accurate color detection.
- Refer to the Preview window to verify the cube state before solving.

## Cube Face Definitions
The solver uses standard Rubik's Cube notation with the following color assignments:
- **F (Front)**: Green
- **B (Back)**: Blue
- **U (Up)**: White
- **D (Down)**: Yellow
- **L (Left)**: Orange
- **R (Right)**: Red

## Project Structure
- `main.py`: Integrates scanning, state management, and solving logic.
- `cube_state.py`: Manages the cube's state and rotations.
- `ui.py`: Renders the Frame and Preview windows.

## Additional Details
- **Color Detection**: Uses HSV ranges defined in the code (e.g., Red: H: 0-10, S: 100-255, V: 100-255).
- **Algorithm**: Implements Kociemba’s two-phase algorithm for solutions under 20 moves.
- Full source code and updates are available at: [https://github.com/MPGranji/Rubik_Solver](https://github.com/MPGranji/Rubik_Solver).

## Appendices
For a detailed demo guide, formulas, and configurations, refer to the appendices in the project documentation.
