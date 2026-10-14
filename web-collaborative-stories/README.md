# Web Collaborative Stories

A dynamic, client-side web application designed for interactive and collaborative storytelling. The platform showcases a responsive board of animated, procedurally generated story cards, customizable color themes, rich story reader views, and an animated neon login portal.

---

## 1. Project Overview & Purpose

**Web Collaborative Stories** is an interactive front-end web project that provides:
- **Interactive Story Board**: A grid of 60 dynamically generated, procedurally colored story cards with smooth hover and scroll animations.
- **Story Reader Mode**: A dedicated reading interface (`content.html`) presenting rich formatted narrative text (*"Title: Echoes of the Forgotten"*) with custom gradients and typography.
- **Customizable Appearance**: An integrated real-time color picker enabling users to dynamically customize card colors and background aesthetics.
- **Accessibility & Motion Control**: A settings modal powered by SweetAlert2 that allows users to toggle animations on and off via custom DOM events.
- **Glowing Neon Login Portal**: An animated multi-colored rotating ring login screen (`loginScreen/loginScreen.html`) for user authentication styling.

---

## 2. Component Architecture & File Structure

The project is structured into modular front-end components across root and dedicated feature directories:

```
web-collaborative-stories/
│
├── index.html                   # Main landing page & interactive story card board
├── content.html                 # Full story reader view ("Echoes of the Forgotten")
├── index.js                     # Procedural card generation (60 cards), gradients, help modal
├── animatingSquares.js          # IntersectionObserver viewport animations & motion toggles
├── colorPicker.js               # Vanilla-Picker v2 integration for dynamic card recoloring
├── square.css                   # Core stylesheet: cards, layouts, gradients, transitions
│
├── loginScreen/                 # Dedicated login screen module
│   ├── loginScreen.html         # Glowing neon multi-ring rotating login interface
│   ├── loginScreen.css          # Keyframe animations (@keyframes animate) & neon glow filters
│   └── loginScreen.js           # Form interaction handler & client-side authentication logic
│
└── settings/                    # Settings & user preferences module
    ├── settings.css             # Toggle switch styles & SweetAlert2 popup overrides
    └── settings.js              # SweetAlert2 modal logic & custom event dispatching
```

### Detailed Component Roles:

1. **`index.html`**:
   The primary entry point. Sets up the document head with CDN stylesheets, scripts, header branding ("collaborative stories"), the story card container (`#basic`), settings gear icon, help button, and navigation link to the login screen.

2. **`content.html`**:
   The reader view. Contains the full text for the story *"Echoes of the Forgotten"*, complete with drop caps, text shadows, responsive margins, and a floating gradient back button linking back to `index.html`.

3. **`index.js`**:
   Generates 60 unique floating story blocks in the DOM on load, calculates gradient color palettes for each block, binds event listeners, and provides the `helpfunction()` modal dialog explaining site rules.

4. **`animatingSquares.js`**:
   Utilizes modern browser APIs (`IntersectionObserver`) to observe card visibility, triggering scale and fade animations as the user scrolls. Listens for custom `animationsOff` and `animationsOn` events from the settings module to dynamically disable or restore motion.

5. **`colorPicker.js`**:
   Initializes the `VanillaPicker` instance, attaching color picker popups to card elements so users can pick custom hex/RGBA colors in real time.

6. **`square.css`**:
   Defines the grid layout, box shadows, border radii, hover transformations, font styles, and header styling for the main interface.

7. **`loginScreen/`**:
   A standalone visual component featuring three concentric rotating neon rings (`#00ff0a`, `#ff0057`, `#fffd44`) rendered with CSS conic gradients and blur filters, encasing a minimalist login form with username and password inputs.

8. **`settings/`**:
   Implements an animated slide toggle switch inside a SweetAlert2 modal. When toggled, it broadcasts `animationsOff` or `animationsOn` custom DOM events to `#para`, allowing decoupled state synchronization across components.

---

## 3. Dependencies & CDN Libraries

This is a pure client-side static web application requiring no compilation, bundler, or backend server. All external libraries are loaded directly from trusted public CDNs inside `index.html`:

| Library | Version | CDN URL | Purpose |
|---|---|---|---|
| **SweetAlert2** | v11 | `https://cdn.jsdelivr.net/npm/sweetalert2@11` | Responsive modal dialogs for settings & help |
| **Vanilla-Picker** | v2 | `https://unpkg.com/vanilla-picker@2` | Interactive zero-dependency color picker |
| **jQuery** | v3.7.1 | `https://code.jquery.com/jquery-3.7.1.min.js` | Fast DOM traversal and event handling utilities |

---

## 4. How to View & Run on Windows

You can run and explore the project using either of the following two methods:

### Method 1: Direct Browser Launch (Simplest)

1. Open File Explorer and navigate to:
   ```
   C:\Users\simsa\Desktop\Organized_Projects\web-collaborative-stories
   ```
2. Double-click **`index.html`** to launch it directly in your default browser (Chrome, Edge, Firefox, Brave).
3. Alternatively, launch from Windows PowerShell:
   ```powershell
   cd "C:\Users\simsa\Desktop\Organized_Projects\web-collaborative-stories"
   Start-Process index.html
   ```

### Method 2: Local HTTP Server (Recommended)

Running through a local web server ensures seamless loading of CDN assets and prevents any browser local-file CORS restrictions:

1. Open PowerShell and navigate to the project directory:
   ```powershell
   cd "C:\Users\simsa\Desktop\Organized_Projects\web-collaborative-stories"
   ```
2. Start Python's built-in HTTP server:
   ```powershell
   python -m http.server 8000
   ```
3. Open your browser and navigate to:
   ```
   http://localhost:8000/
   ```

---

## 5. User Interaction & Features Guide

- **Reading Stories**: Scroll through the floating cards on `index.html`. Click **"Visit Example"** on any card to navigate directly to `content.html` and read *"Echoes of the Forgotten"*. Click the **"Back"** button on `content.html` to return to the board.
- **Toggling Animations**: Click the **Gear icon** in the top area to open the Settings modal. Toggle the switch to turn scroll animations on or off, then click **OK**.
- **Help & Rules**: Click the **"i" Help icon** to display the platform information dialog.
- **Customizing Colors**: Click on any story square or the color picker control to open the color palette and select new accent colors.
- **Accessing Login Portal**: Click the **"login"** button in the bottom navigation to open `loginScreen/loginScreen.html` and experience the neon ring visual animation.
