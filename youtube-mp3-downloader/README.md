# YouTube MP3 Downloader

A lightweight, threaded desktop graphical user interface (GUI) application built with Python and Tkinter that downloads and extracts high-quality MP3 audio from YouTube videos.

---

## 1. Overview & Features

- **Graphical User Interface**: Compact Tkinter interface featuring an input field for video URLs, action buttons, and animated progress indications.
- **Multithreaded Background Downloads**: Download and extraction tasks run asynchronously on a background worker thread (`threading.Thread`), preventing the UI from freezing or becoming unresponsive while streaming large files.
- **Animated Progress Bar**: Uses an indeterminate `ttk.Progressbar` widget that animates throughout video information querying and audio extraction.
- **Dynamic File Naming**: Automatically extracts the YouTube video title via metadata querying and saves the resulting audio directly as `<Title>.mp3` in the current working directory.
- **Feedback & Auto-Resetting State**:
  - Displays a green **"downloaded"** confirmation upon successful audio completion.
  - Displays a red **"not entered youtube link or syntax error"** message if an invalid URL is passed or a network failure occurs.
  - Status labels automatically clean up after 4 seconds, allowing the user to paste and download multiple tracks sequentially.

---

## 2. Requirements & Prerequisites

### A. Python Environment
- **Python 3.8+** on Windows (standard Windows Python installations include `tkinter`).

### B. Python Libraries (`requirements.txt`)
- `youtube-dl>=2021.12.17`: Audio and video streaming extraction library imported directly by the script.
- `yt-dlp>=2024.0.0`: Actively maintained modern fork recommended as a drop-in upgrade for handling ongoing YouTube cipher and signature updates.

### C. System Dependency: FFmpeg (Mandatory for MP3 Conversion)
The underlying downloader queries audio streams from YouTube (which are typically encoded as Opus/WebM or AAC/M4A). **FFmpeg** is required on your system PATH to extract the audio stream and transcode it into the destination `.mp3` format.

#### Installing FFmpeg on Windows:

- **Via Windows Package Manager (Winget - Recommended)**:
  ```powershell
  winget install Gyan.FFmpeg
  ```
- **Via Chocolatey**:
  ```powershell
  choco install ffmpeg
  ```
- **Via Scoop**:
  ```powershell
  scoop install ffmpeg
  ```
- **Manual Installation**:
  1. Download the latest release essentials build from [gyan.dev/ffmpeg/builds](https://www.gyan.dev/ffmpeg/builds/).
  2. Extract the archive to a permanent folder (e.g., `C:\ffmpeg`).
  3. Add `C:\ffmpeg\bin` to your Windows System `PATH` environment variable.

#### Verify FFmpeg Installation:
Open PowerShell or Command Prompt and run:
```powershell
ffmpeg -version
```
If properly configured, the FFmpeg version banner will be displayed.

---

## 3. Legacy Architecture & Python 3 Compatibility

### The `ttk` Import Shim
- **Background**: The original script specifies `import youtube_dl, threading ,ttk, time` at line 1. In Python 2, `ttk` was an independent top-level module, whereas in Python 3 it is located at `tkinter.ttk`. Directly executing the script under Python 3 without compatibility handling raises `ModuleNotFoundError: No module named 'ttk'`.
- **Code Immutability Compliance**: Under project governance rules, user source files must remain 100% byte-for-byte untouched.
- **Solution (`ttk.py`)**: A non-intrusive 2-line compatibility shim `ttk.py` is bundled in the same directory:
  ```python
  # Compatibility shim for Python 3 execution of legacy script importing ttk
  from tkinter.ttk import *
  ```
  When Python executes `download yt vid as mp3.py`, Python resolves `ttk` locally from the application directory, exposing `Progressbar` and all ttk widgets without modifying a single byte of user code.

---

## 4. Step-by-Step Windows Run Instructions

### Step 1: Open PowerShell and Navigate to the Project Directory
```powershell
cd "C:\Users\simsa\Desktop\Organized_Projects\youtube-mp3-downloader"
```

### Step 2: (Optional but Recommended) Create and Activate a Virtual Environment
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Step 3: Install Required Dependencies
```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Launch the Downloader Application
```powershell
python "download yt vid as mp3.py"
```

### Step 5: Download Audio
1. Copy any valid YouTube video URL to your clipboard (e.g., `https://www.youtube.com/watch?v=...`).
2. Paste the URL into the application text entry field.
3. Click the **enter** button.
4. The progress bar will animate while the stream is fetched and converted.
5. Once complete, the status label indicates **downloaded**, and the `.mp3` file will appear in the directory where the application was launched.

---

## 5. Troubleshooting & Tips

- **"ffprobe or avconv not found" error**:
  - FFmpeg is not detected in your system PATH. Install FFmpeg as described in Section 2.C, then restart your terminal.
- **YouTube Extraction / HTTP 403 / "Sign in to confirm you're not a bot"**:
  - YouTube periodically updates its bot detection mechanisms and video player formats.
  - If `youtube-dl` encounters an extraction failure on newer YouTube links, upgrade `yt-dlp`:
    ```powershell
    pip install --upgrade yt-dlp
    ```
- **Where are files saved?**:
  - The script saves files relative to the working directory:
    ```python
    filename = f"{video_info['title']}.mp3"
    ```
  - When running from PowerShell in `C:\Users\simsa\Desktop\Organized_Projects\youtube-mp3-downloader`, the MP3 will be saved directly in that directory.
