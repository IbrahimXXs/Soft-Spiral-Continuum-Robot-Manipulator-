# Soft Spiral Robot Simulation with MuJoCo

## 🧭 Overview

*A biologically-inspired, tendon-driven soft robotic manipulator, simulated using [MuJoCo](https://mujoco.org/). This project explores the capabilities of soft continuum structures through a multi-segmented, muscle-actuated spiral design.*

---

![image](https://github.com/user-attachments/assets/fbe706a3-ba9c-4e27-a5c9-9d519cba4a26)




## Features

- **Continuum Manipulator:** 28 soft segments linked in series, enabling smooth bending and contraction.
- **Tendon-Based Actuation:** Dual tendons provide bidirectional control through virtual muscles.
- **MuJoCo Physics Simulation:** High-performance physics with compliant tendon routing and dynamic response.
- **Real-Time Keyboard Control:** Interactive user input via simple `k`/`l` keypresses to actuate each tendon.

---

## Project Structure

- `Long_Manipulator.xml` – Full XML specification for the soft spiral robot in MuJoCo.
- `controller.py` – Python script to run the simulation and control actuation in real-time.
- `requirements.txt` – Dependencies for Python and MuJoCo integration.
- `/3D/` – STL mesh files for platform, base, and all segment geometries.

---

## Prerequisites

- [MuJoCo](https://mujoco.org/)
- `mujoco-python`
- `pynput`
- Python 3.8+

Install all dependencies:

```bash
pip install -r requirements.txt

##  Installation & Usage

### Clone the repository:

```bash
git clone https://github.com/your-username/soft-spiral-robot.git
cd soft-spiral-robot

#  Soft Robotic Controller

A MuJoCo-based soft robot simulation that mimics tendon-driven actuation through keyboard-controlled joints. This project explores elasticity, geometry scaling, and tendon-based control using realistic 3D models.

---

##  Run the Simulation

```bash
python XXX.py

#### Contributing

Contributions are welcome! If you'd like to enhance the project or fix issues, please follow these steps:

Fork the project.

Create your feature branch

Commit your changes

Push to the branch

Open a pull request

#### License

This project is licensed under the MIT License.

#### Acknowledgments

Thank you to the Rhino3D and Grasshopper communities for their invaluable resources and support.

#### Contact

For inquiries and feedback, please contact

