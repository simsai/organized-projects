# Voice Assistant ("Simi")

A personal Windows desktop voice assistant named **"Simi"** featuring real-time speech recognition, text-to-speech synthesis, automated desktop window controls, application launching, web searching, note-taking, and instant messaging automation.

---

## 1. Project Overview

The Voice Assistant project provides an interactive voice-controlled environment on Windows. It listens via microphone streams using Google Speech Recognition, processes spoken commands, and performs automated operating system actions or queries, delivering vocal feedback through offline text-to-speech (`pyttsx3`) as well as visual desktop toast notifications (`plyer`).

### Core Capabilities
- **Speech Recognition & Synthesis**: Online speech-to-text transcription via Google Speech API (`SpeechRecognition`) and high-performance offline text-to-speech vocal responses (`pyttsx3`).
- **Application Control**:
  - Automatically queries the Windows registry (`winapps`) to locate installed software and launch executables on voice command.
  - Terminates running processes by process name using Windows `TASKKILL`.
  - Captures and minimizes active foreground windows on demand (`win32gui`).
- **Web Automation & Search**:
  - Triggers default browser search queries using `pywhatkit`.
  - Scrapes Google search result snippets in real-time (`requests`, `beautifulsoup4`, `lxml`) and reads the top summary snippets aloud.
- **WhatsApp Desktop Automation**:
  - Automates desktop WhatsApp via `pyautogui`, focusing the application, searching contacts, and sending spoken messages hands-free.
- **Floating Sticky Notes**:
  - Spawns custom draggable, yellow Tkinter sticky notes containing spoken transcriptions with add/delete controls.
- **Global Hotkeys & System Feedback**:
  - Global hotkeys (`keyboard`, `pynput`) to interrupt speech synthesis (`q`) or halt engine hooks.
  - Native Windows desktop toast notifications with custom branding (`icon.ico`).

---

## 2. Audio & Visual Assets

The project bundle includes dedicated sound effects and graphical branding:

| Asset File | Purpose & Role |
|---|---|
| `icon.ico` | Application icon used for desktop toast notifications (`plyer.notification`) and window branding. |
| `Ozz.mp3` | Extended audio clip / wake sound asset utilized for assistant initialization and audio alerts. |
| `Vine Boom Sound Effect (Longer Verison For Real).mp3` | Bass-boosted comedic / dramatic sound effect trigger. |
| `Biggest Criminal In India.mp3` | Humorous audio clip asset associated with assistant voice responses. |
| `PyWhatKit_DB.txt` | Local database history log managed by `pywhatkit` for web searches and queued actions. |

---

## 3. Project Structure

```text
voice-assistant/
├── spech.py                                              # Main interactive voice assistant script
├── spech.pyw                                             # Silent background daemon variant
├── icon.ico                                              # Notification and window icon
├── Biggest Criminal In India.mp3                         # Audio asset
├── Ozz.mp3                                               # Audio asset
├── Vine Boom Sound Effect (Longer Verison For Real).mp3  # Audio asset
├── PyWhatKit_DB.txt                                      # Local action history tracking
├── requirements.txt                                      # Python package dependencies
└── README.md                                             # Project documentation and run guide
```

---

## 4. Dependencies & Prerequisites

### Hardware & System Prerequisites
1. **Operating System**: Windows 10 or Windows 11 (uses Windows-specific APIs including `win32gui`, `winapps`, and `TASKKILL`).
2. **Microphone**: A functional audio input device set as the Windows default recording device.
3. **VLC Media Player (64-bit)**: The `python-vlc` package requires the 64-bit VLC media player (`libvlc.dll`) installed on the system to initialize the VLC audio backend. Download from [videolan.org](https://www.videolan.org/vlc/).
4. **Python Version**: Recommended Python 3.10 to 3.12 (64-bit).

### Python Libraries (`requirements.txt`)
- `SpeechRecognition>=3.10.0` — Speech recognition engine with Google Speech API support
- `PyAudio>=0.2.14` — Microphone audio stream capture
- `pyttsx3>=2.90` — Offline Text-to-Speech synthesis
- `pywin32>=306` — Windows API bindings (`win32gui`, `win32con`, `win32api`, `win32process`)
- `winapps>=0.2.0` — Windows installed software registry search
- `pyautogui>=0.9.54` — GUI automation (keyboard shortcuts, typing, mouse clicks)
- `plyer>=2.1.0` — Windows desktop toast notifications
- `pywhatkit>=5.4.3` — Web searches and automation
- `beautifulsoup4>=4.12.0` — HTML parsing and extraction
- `lxml>=5.0.0` — High-performance XML/HTML parser backend
- `pynput>=1.7.6` — Global mouse and keyboard monitoring
- `keyboard>=0.13.5` — Global hotkey detection
- `python-vlc>=3.0.20123` — VLC media playback bindings
- `requests>=2.31.0` — HTTP requests for web scraping

---

## 5. Setup & Installation Guide

### Step 1: Open Terminal in Project Directory
Open PowerShell or Command Prompt and navigate to the project directory:
```powershell
cd "C:\Users\simsa\Desktop\Organized_Projects\voice-assistant"
```

### Step 2: Create and Activate a Virtual Environment (Recommended)
Creating an isolated virtual environment prevents library version conflicts:
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Step 3: Install Required Packages
```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

> **PyAudio Installation Troubleshooting on Windows**:
> If building `PyAudio` via pip fails due to missing C++ build tools:
> ```powershell
> pip install pipwin
> pipwin install pyaudio
> ```
> Or install a pre-compiled wheel directly from Christoph Gohlke's unofficial Windows binaries or PyPI.

---

## 6. How to Run

### Mode A: Interactive Console Assistant (`spech.py`)
This is the primary full-featured assistant with vocal feedback, console transcription logs, sticky note generation, and active command execution:
```powershell
python spech.py
```
- Upon launch, the assistant speaks `"here for you"` and displays a Windows toast notification: *"simi started but hidden, to stop script say kill"*.
- The assistant listens continuously via the default microphone.
- Press **`q`** on the keyboard at any time to immediately interrupt current speech synthesis.

### Mode B: Silent Background Daemon (`spech.pyw`)
`spech.pyw` runs silently in the background without opening a terminal window:
```powershell
pythonw spech.pyw
```
- Listens for core commands and provides desktop notifications.
- Say `"stop"` to terminate the background process gracefully, or end it via Windows Task Manager.

---

## 7. Voice Command Reference

| Spoken Command | Action Executed by Assistant |
|---|---|
| `"minimise"` | Minimizes the currently focused foreground window (`win32gui.ShowWindow`). |
| `"open <app>"` | Searches installed Windows applications via registry and launches the executable (e.g. `"open chrome"`, `"open notepad"`). |
| `"close <app>"` | Terminates `<app>.exe` via `TASKKILL /F /IM <app>.exe` and confirms vocal closure. |
| `"tell me <query>"` | Opens the default browser and performs a search via Google (`pywhatkit.search`). |
| `"simi <query>"` | Queries Google directly via `requests`, parses snippets via `BeautifulSoup` (`lxml`), and vocalizes the top 3 results. |
| `"note <content>"` | Spawns a frameless, yellow Tkinter sticky note populated with transcribed note text. |
| `"WhatsApp <message> to <contact>"` | Launches WhatsApp Desktop, navigates to contact via `ctrl+f`, and pastes the spoken message. |
| `"type <text>"` | Emulates keyboard typing of dictated text into the currently active text field. |
| `"find <text>"` | Triggers `Ctrl+F` and inputs `<text>` into the active document or browser tab. |
| `"set a timer for <seconds>"` | Starts a countdown timer for the specified duration. |
| `"stop"` / `"kill"` | Displays a exit notification, vocally bids farewell, and terminates the assistant process. |

---

## 8. Code Immutability Note

In accordance with strict project preservation rules, original source code files (`spech.py`, `spech.pyw`) and binary assets (`icon.ico`, MP3 audio files) are preserved **100% byte-for-byte identical** to their source counterparts with matching SHA-256 cryptographic hashes.
