# Atmos

> **A weather and time-aware dynamic wallpaper engine for your desktop.**

Atmos is an open-source desktop application that automatically adapts your wallpaper to the **time of day and current weather**.

The goal is simple: make your desktop feel connected to the world outside.

> 🚧 **Atmos is currently under active development.**
> The project is being built from the ground up as a learning-focused open-source project.

---

## ✨ Vision

Imagine opening your laptop on a rainy morning and seeing a quiet, cinematic rainy scene.

As the day progresses:

```text
🌅 Morning
      ↓
☀️ Day
      ↓
🌇 Golden Hour
      ↓
🌙 Night
```

And when the weather changes:

```text
☀️ Clear      → Bright daytime scene
☁️ Cloudy     → Overcast atmosphere
🌧️ Rain       → Rainy scene
⛈️ Storm      → Dark storm scene
🌫️ Fog        → Misty scene
❄️ Snow       → Winter scene
```

Atmos combines these signals to determine what your desktop should look like.

---

## 🎯 Goals

* Automatically change wallpapers based on **time of day**
* React to **current weather conditions**
* Provide smooth and unobtrusive wallpaper transitions
* Support user-provided wallpaper collections
* Keep resource usage low while running in the background
* Eventually support multiple operating systems
* Make the project easy to extend and contribute to

---

## 🛠️ Tech Stack

Atmos is being built with a deliberately lightweight stack:

* **Python** — Core application
* **PySide6** — Desktop interface
* **Pillow** — Image processing
* **HTTP client** — Weather API communication
* **pytest** — Testing
* **Ruff** — Linting and formatting
* **GitHub Actions** — CI/CD

The stack may evolve as the project grows.

---

## 🏗️ Architecture

The application is designed around several independent components:

```text
                    ┌─────────────────┐
                    │    Atmos UI     │
                    │    (PySide6)    │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │   Scene Engine  │
                    └───────┬─┬───────┘
                            │ │
               ┌────────────┘ └────────────┐
               ▼                           ▼
        ┌──────────────┐            ┌──────────────┐
        │ Time Engine  │            │Weather Engine│
        └──────┬───────┘            └──────┬───────┘
               │                           │
               └────────────┬──────────────┘
                            ▼
                   ┌─────────────────┐
                   │Wallpaper Engine │
                   └────────┬────────┘
                            ▼
                    🖥️ Desktop
```

The architecture is intentionally modular so new functionality can be added without rewriting the entire application.

---

## 🚀 Roadmap

### Phase 0 — Foundation

* [ ] Repository setup
* [ ] Python project structure
* [ ] Development environment
* [ ] Basic logging
* [ ] Initial test suite

### Phase 1 — Wallpaper Engine

* [ ] Set Windows desktop wallpaper
* [ ] Load wallpapers from a local directory
* [ ] Wallpaper selection
* [ ] Basic wallpaper switching

### Phase 2 — Time Engine

* [ ] Detect current time
* [ ] Define time-of-day periods
* [ ] Time-based wallpaper selection
* [ ] Automatic scheduled switching

### Phase 3 — Weather Engine

* [ ] Integrate weather API
* [ ] Retrieve current conditions
* [ ] Normalize weather conditions
* [ ] Handle API/network failures
* [ ] Cache weather information

### Phase 4 — Scene Engine

* [ ] Combine time + weather
* [ ] Scene resolution system
* [ ] Weather intensity
* [ ] Scene priorities
* [ ] User-configurable rules

### Phase 5 — Desktop Application

* [ ] PySide6 interface
* [ ] Current scene preview
* [ ] Settings
* [ ] Location configuration
* [ ] Enable/disable automatic switching
* [ ] Background operation

### Future

* [ ] Smooth wallpaper transitions
* [ ] Multi-monitor support
* [ ] Wallpaper packs
* [ ] User-created themes
* [ ] Animated wallpapers
* [ ] Sunrise/sunset integration
* [ ] Battery-aware behavior
* [ ] Windows startup integration
* [ ] Linux support
* [ ] macOS support
* [ ] Plugin system
* [ ] Community wallpaper ecosystem

> The roadmap is intentionally flexible and will evolve as Atmos develops.

---

## 📁 Project Structure

```text
atmos/
├── src/
│   └── atmos/
│       ├── core/
│       ├── wallpaper/
│       ├── platform/
│       ├── ui/
│       └── config/
│
├── tests/
├── assets/
│   └── wallpapers/
├── docs/
├── scripts/
│
├── pyproject.toml
├── README.md
├── CONTRIBUTING.md
└── LICENSE
```

---

## 🧑‍💻 Development

### Requirements

* Python 3.12+
* Windows 10/11 *(initial development target)*
* Git

### Clone

```bash
git clone https://github.com/<your-username>/atmos.git
cd atmos
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate it

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### Install dependencies

```bash
pip install -e ".[dev]"
```

### Run

```bash
python -m atmos
```

> Development commands may change as the project structure evolves.

---

## 🤝 Contributing

Atmos is an open-source project and contributions will eventually be welcome.

Possible areas to contribute:

* New platform support
* Wallpaper providers
* Weather providers
* Scene logic
* UI improvements
* Performance improvements
* Tests
* Documentation
* Bug fixes

Before contributing, please read [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

## 📜 License

Atmos is open source and will be released under the **MIT License**.

See [`LICENSE`](LICENSE) for details.

---

## 🌌 Philosophy

Atmos isn't meant to constantly demand your attention.

It should quietly adapt to the world around you.

**Your desktop, in sync with the atmosphere.**

---

⭐ If you find Atmos interesting, consider starring the repository and following its development.
