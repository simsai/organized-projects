# Pygame Space Shooter Arcade Game

## 1. Project Overview

**Pygame Space Shooter** is a complete, self-contained 2D arcade space combat game developed in Python using Pygame. The game features fast-paced 60 FPS combat, procedural vector graphics, three distinct enemy archetypes, six dynamic collectible power-ups, an evolving weapon spread system, and a full game state machine (Main Menu, Instructions, Active Combat, Pause, and Game Over loop).

---

## 2. Directory Structure

```
pygame-space-shooter/
├── space-shooter-game.py     # Complete standalone space shooter game
├── requirements.txt          # Pygame dependency specification (pygame>=2.0.0)
└── README.md                 # Project documentation and Windows run guide
```

---

## 3. Architecture & Procedural Rendering

### Zero-Asset Procedural Graphics
The entire game is self-contained within `space-shooter-game.py`. It requires **no external image assets, fonts, or texture packs**:
- **Player & Enemy Ships**: Rendered procedurally as geometric polygons using `pygame.draw.polygon`. Player ships point upward, while enemy ships point downward.
- **Projectiles & HUD**: Player and enemy laser beams, health bars, shields, and power-up boxes are dynamically drawn using Pygame vector primitives.
- **Shield Effect**: When active, the temporary shield surrounds the player ship with an orange protective energy aura.

### Game State Machine
The game loop manages five distinct states:
1. **Menu (`show_menu`)**: Start screen with options to begin combat or view instructions.
2. **Instructions (`show_instructions`)**: In-game guide detailing ship controls, enemy types, and power-up effects.
3. **Combat Loop**: Real-time 60 FPS gameplay, player movement, projectile physics, and collision detection.
4. **Pause (`paused`)**: Activated via `ESC`, freezing game physics while maintaining screen state.
5. **Game Over (`show_game_over`)**: Displays final score with instant restart functionality (`P`).

---

## 4. Gameplay Mechanics

### Enemy Archetypes
Enemies spawn from the top of the screen at randomized horizontal intervals with unique combat profiles:
| Type | Color | Health | Speed | Fire Rate | Weapon Type |
|---|---|---|---|---|---|
| **Scout** | Red | 30 HP | Fast (2) | Moderate (delay: 60) | Single direct laser |
| **Cruiser** | Blue | 50 HP | Slow (1) | Heavy (delay: 90) | Dual spread lasers (15° spread) |
| **Interceptor** | Yellow | 40 HP | Agile (3) | Rapid (delay: 75) | Triple spread lasers (30° spread) |

### Power-Up System
Power-ups spawn periodically across the combat zone with color-coded effects:
| Power-Up | Color | Effect | Duration |
|---|---|---|---|
| **Health** | Purple | Restores +50% player health instantly | Instantaneous |
| **Damage Boost** | Green | Doubles bullet damage (2x multiplier) | 5 Seconds |
| **Speed Boost** | Cyan | Increases player maneuverability speed | 5 Seconds |
| **Shield** | Orange | Renders player ship invulnerable to collisions and lasers | 3 Seconds |
| **Rapid Fire** | Pink | Drastically reduces shooting delay | 5 Seconds |
| **Spread Shot** | Brown | Widens player bullet spray angle for maximum area coverage | 5 Seconds |

### Evolving Weapon Mechanics
Every 20 seconds of survival (`spread_change_timer`), the player's weapon automatically recalculates bullet spread angle and projectile density, cycling combat dynamics between concentrated narrow streams and wide bullet blankets.

---

## 5. Controls Reference

| Context | Key | Action |
|---|---|---|
| **Movement** | `W` | Move Ship Up |
| **Movement** | `A` | Move Ship Left |
| **Movement** | `S` | Move Ship Down |
| **Movement** | `D` | Move Ship Right |
| **Firing** | *Automatic* | Lasers fire automatically based on weapon cooldown |
| **Main Menu** | `P` | Start Game |
| **Main Menu** | `I` | Open Instructions |
| **Instructions**| `B` | Return to Main Menu |
| **In-Game** | `ESC` | Pause / Unpause Game |
| **Game Over** | `P` | Replay / Restart Game |

---

## 6. Windows Execution Guide

### Prerequisites
- **Python 3.8+** installed on Windows.
- Check Python availability:
  ```powershell
  python --version
  ```

### Step 1: Install Dependencies
Open PowerShell, navigate to the project directory, and install requirements:
```powershell
cd "C:\Users\simsa\Desktop\Organized_Projects\pygame-space-shooter"
pip install -r requirements.txt
```

*(Recommended: Run inside an isolated virtual environment)*:
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Step 2: Launch the Game
Run the game using Python:
```powershell
python space-shooter-game.py
```
A 800x600 window will open. Press **`P`** to launch into space combat.
