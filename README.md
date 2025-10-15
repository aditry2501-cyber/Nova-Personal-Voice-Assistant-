# 🎙️ Nova - Voice-Activated Personal Assistant

A Python-based voice assistant that responds to voice commands to open websites, play music, and perform various tasks using speech recognition and text-to-speech capabilities.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

---

## 🌟 Features

- **Wake Word Activation**: Responds to "Nova" keyword for hands-free operation
- **Speech Recognition**: Uses Google Speech Recognition API for accurate voice command processing
- **Text-to-Speech**: Natural voice responses using pyttsx3 (SAPI5 engine)
- **Web Automation**: Opens popular websites (Google, YouTube, LinkedIn, Facebook, Instagram, Gmail)
- **Music Player**: Plays songs from custom music library via YouTube links
- **Ambient Noise Calibration**: Automatically adjusts for background noise
- **Continuous Listening**: Always-on mode with timeout handling
- **Error Handling**: Robust exception handling for unrecognized commands

---

## 🛠️ Tech Stack

- **Python 3.x**
- **SpeechRecognition** - Google Speech API integration
- **pyttsx3** - Text-to-speech engine (SAPI5)
- **PyAudio** - Audio I/O for microphone access
- **webbrowser** - Browser automation for opening websites

---

## 📋 Prerequisites

Before you begin, ensure you have:

- Python 3.8 or higher installed
- Working microphone
- Stable internet connection (required for Google Speech Recognition)
- Windows OS (uses SAPI5 voice engine)
- Chrome or default browser installed

---

## 🚀 Installation

### 1. Clone the repository

