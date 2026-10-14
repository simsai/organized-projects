# 2D Pygame Platformer & Physics Simulation

## 1. Project Overview

This repository contains a 2D platformer and physics demo developed with Python and Pygame. The project combines player character animations, jump kinematics with gravity simulation, procedural platform/item generation, and bounding-box collision detection.

The project contains two distinct scripts:
1. **`Untitled-2.py`**: The complete platformer game featuring multi-directional sprite animations, jump physics, collision platforms (`wall`, `box`, `box2`), randomized collectible apples (`functioning_apple()`), and a real-time scoring HUD.
2. **`import pygame.py`**: A self-contained 60 FPS bouncing collision simulation demonstrating Pygame's `colliderect` method between two kinematic rectangles with boundary bounce physics (and an included commented sprite movement prototype).

---

## 2. Directory Structure & Asset Inventory

```
pygame-platformer/
├── import pygame.py          # Standalone bouncing collision mechanics demo
├── Untitled-2.py             # Full animated 2D platformer game with scoring
├── requirements.txt          # Pygame dependency specification (pygame>=2.0.0)
├── README.md                 # Project documentation and Windows run guide
├── left/                     # Left-facing player sprites & collectibles
│   ├── 1.png - 6.png         # Running cycle frames (left)
│   ├── 9.png, 10.png         # Running cycle frames (left)
│   ├── standing_straight.png # Idle player character sprite
│   └── apple.png             # Collectible bonus item
└── right/                    # Right-facing player sprites
    └── 1.png - 10.png        # Running cycle frames (right)
```

---

## 3. Gameplay Mechanics & Engine Architecture

### Physics & Jump Kinematics
- **Kinematic Jump Equation**: Jump velocity and acceleration are modeled using the kinetic energy impulse formula:
  $$F = \frac{1}{2} \cdot m \cdot v^2$$
  where initial impulse velocity $v = 10$ and player mass $m = 1$. As the player ascends, velocity decays ($v = v - 1$), causing the character to decelerate, apex, and accelerate downwards.
- **Platform Collision Bounding**: The player character bounding box (`image3`) tests for collisions against the ground `wall` (1200x600 px at $y=750$), floating obstacle `box`, and platform `box2`. Collision halts downward motion (`can_godown = False`).

### Procedural Collectible Generation
- The `functioning_apple()` function procedurally randomizes platform and apple positions within bounded safe zones:
  - `box`: Horizontal span 50–400 px, positioned at random $y \in [500, 700]$
  - `box2`: Floating platform relative to `box`
  - `apple`: Collectible target spawned above platform structures
- Upon colliding with the apple, the score increases by 1 and a new level layout is dynamically calculated.

### Controls Reference
| Key | Action |
|---|---|
| `A` / Left Arrow | Move Left (triggers left running animation cycle) |
| `D` / Right Arrow | Move Right (triggers right running animation cycle) |
| `Spacebar` | Jump (activates impulse physics) |
| `W` / Up Arrow | Upward adjustment |
| `S` / Down Arrow | Downward adjustment |
| `ESC` / Close | Exit game |

---

## 4. Strict Code Immutability & Legacy Hardcoded Path Notice

### Preservation Notice
Under strict code immutability requirements, **all user code files have been preserved 100% byte-for-byte untouched** (cryptographic SHA-256 match with the original files).

### Legacy Path Context
In `Untitled-2.py` (lines 56–84), sprite assets were originally loaded via hardcoded paths referencing the developer's original desktop environment:
```python
r'C:\Users\<legacy_user>\Desktop\right\\1.png'
r'C:\Users\<legacy_user>\Desktop\left\\1.png'
```

To run `Untitled-2.py` directly, you can adjust the path to relative paths or create a directory mapping as shown below.

---

## 5. Windows Execution Guide

### Prerequisites
- **Python 3.8+** installed on Windows and added to your `PATH`.
- Check Python installation:
  ```powershell
  python --version
  ```

### Step 1: Install Dependencies
Open PowerShell, navigate to the project folder, and install Pygame:
```powershell
cd "C:\Users\simsa\Desktop\Organized_Projects\pygame-platformer"
pip install -r requirements.txt
```
*(Or create a clean virtual environment: `python -m venv venv; .\venv\Scripts\Activate.ps1; pip install -r requirements.txt`)*

---

### Step 2: Running the Game

#### Option A: Run the Standalone Collision Demo (`import pygame.py`)
This script contains an executable, self-contained 60 FPS collision physics simulation that requires **zero external assets**:
```powershell
python "import pygame.py"
```
A 600x600 window will open showing two colored rectangles bouncing and reacting to bounding box collisions in real time.

---

#### Option B: Run the Full Platformer (`Untitled-2.py`)
Run the full platformer game with animated sprites:
```powershell
python Untitled-2.py
```
