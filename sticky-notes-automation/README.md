# Sticky Notes Automation

A custom desktop sticky notes application with a frameless draggable Tkinter graphical interface, SQLite database persistence, and built-in Windows automation and computer vision hooks.

---

## 1. Project Overview

`sticky-notes-automation` provides a lightweight, post-it note experience on Windows. It creates floating, yellow sticky notes that stay pinned on top of active windows, allowing quick note-taking, multi-note management, and integration with desktop automation tools.

### Key Highlights
- **Frameless Draggable UI**: Utilizes Tkinter's `overrideredirect(True)` to remove standard OS window borders, replacing them with a custom draggable header bar (`#F8F796`).
- **Cascading Multi-Note Windows**: Spawn multiple notes simultaneously using the `+` button, with smart coordinate offsets so notes do not overlap entirely.
- **Always-on-Top & Resizable**: Keeps important reminders visible across desktop workflows while allowing edge-resizing.
- **SQLite Database Persistence**: Bundled with `pin_your_note.db` featuring `notes_table` for saving and retrieving note records.
- **Desktop Automation Integration**: Built-in functions for low-level Windows API cursor movement and click simulation (`win32api`), OpenCV template matching hooks (`cv2`), keyboard event capturing, and web queries.
- **Visual Branding**: Bundled with a custom sticky note graphic asset (`sticky note.png`).

---

## 2. File Organization & Manifest

```
sticky-notes-automation/
├── README.md              # Project documentation and Windows run guide
├── requirements.txt       # Python package dependencies
├── stickynotes.py         # Main Tkinter application and automation script
├── pin_your_note.db       # SQLite3 database for note persistence
└── sticky note.png        # Sticky note icon/graphic asset (244x244 PNG)
```

### File Details & Hashes
| File | Size | Role | SHA-256 Checksum |
|---|---|---|---|
| `stickynotes.py` | 3,391 bytes | Main Python script | `8FBD00CEC9DD214F7774BB704FBF0D0708C4B82B3A7676C63C5793F82FFB988D` |
| `pin_your_note.db` | 8,192 bytes | SQLite3 database | `E6898A30FA5624BE6BFE801896F52BECFFA48A0D55779232ED812648CA15EE13` |
| `sticky note.png` | 2,942 bytes | UI graphic asset | `7DFC644643C61C246159F4614866EA92C6230A439C77474C89F5F076BE1863E4` |

---

## 3. Database Architecture & Schema

The application includes a pre-configured SQLite database: **`pin_your_note.db`**.

### Table Schema: `notes_table`
```sql
CREATE TABLE notes_table (
    date text,
    notes_title text,
    notes text
);
```

### Column Specifications
- **`date`** (`TEXT`): Timestamp or date string when the note was created or last modified.
- **`notes_title`** (`TEXT`): Short summary or title of the note.
- **`notes`** (`TEXT`): Full text body containing the user's notes and reminders.

### Inspecting Database via Python
You can inspect or query the database at any time using Python's built-in `sqlite3`:
```powershell
python -c "import sqlite3; conn = sqlite3.connect('pin_your_note.db'); print(conn.execute('SELECT * FROM notes_table').fetchall())"
```

---

## 4. UI Architecture & Features

### 1. Frameless Window Design
- **Window Geometry**: Initial size of `250x250` pixels, positioned near the right-hand side of the monitor (`1000 - 30 * window_count`, `100 + 20 * window_count`).
- **Styling**: Pastel yellow background (`#FDFDCA`) with a darker yellow draggable header bar (`#F8F796`) and Comic Sans MS italicized typography.
- **Shadow Borders**: Side and bottom shadow frame simulation (`#838383`).

### 2. Window Controls
- **Drag Header**: Left-click (`<Button-1>`) on the yellow title bar and drag (`<B1-Motion>`) to move the note freely anywhere on your screen.
- **Add Note (`+`)**: Left-click the `+` button on the top-left to spawn an additional sticky note window.
- **Delete Note (`X`)**: Left-click the `X` button on the top-right. A confirmation dialog (`messagebox.askyesno`) prompts: *"Are you sure you want to delete this note?"*. Confirming deletes the note; deleting the last remaining note cleanly terminates the application.

### 3. Automation & System Utilities
The module imports and implements automation hooks:
- **`click(x, y)`**: Direct Windows API mouse positioning and left-click dispatch via `win32api.SetCursorPos` and `win32api.mouse_event(MOUSEEVENTF_LEFTDOWN / LEFTUP)`.
- **OpenCV (`cv2`)**: Computer vision template matching integration for UI recognition.
- **`pyautogui` & `keyboard`**: Screen capture and global keyboard listeners.
- **`winapps` & `win32gui`**: Detection of running Windows software and window handles.
- **`pywhatkit` & `googlesearch`**: Instant web lookups and automation helpers.

---

## 5. Prerequisites & Requirements

### System Requirements
- **OS**: Windows 10 or Windows 11 (64-bit recommended).
- **Python**: Python 3.9 through 3.12 (with standard Tkinter support included in the official Windows installer).

### Dependencies (`requirements.txt`)
- `googlesearch-python>=1.2.3`
- `pywhatkit>=5.4.3`
- `winapps>=0.2.0`
- `pywin32>=306`
- `pyautogui>=0.9.54`
- `keyboard>=0.13.5`
- `opencv-python>=4.9.0`

---

## 6. Windows Run Guide

Follow these step-by-step instructions in PowerShell or Command Prompt:

### Step 1: Open PowerShell
Press `Win + X` and select **PowerShell** or **Terminal**.

### Step 2: Navigate to the Project Folder
```powershell
cd "C:\Users\simsa\Desktop\Organized_Projects\sticky-notes-automation"
```

### Step 3: (Recommended) Create and Activate a Virtual Environment
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Step 4: Install Dependencies
```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Step 5: Launch the Sticky Notes Application
```powershell
python stickynotes.py
```

---

## 7. Troubleshooting & Notes

- **Tkinter Missing**: If running a custom or embedded Python installation without Tkinter, ensure the standard Python Windows installer from `python.org` was installed with the "tcl/tk and IDLE" option checked.
- **PyWin32 Post-Install**: If `win32api` throws a DLL load error upon first launch, run:
  ```powershell
  python .\venv\Scripts\pywin32_postinstall.py -install
  ```
- **Code Immutability**: All original scripts, database files, and assets are strictly preserved byte-for-byte from the user's original setup.
