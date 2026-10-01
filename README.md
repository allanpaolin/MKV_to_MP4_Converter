# 🎬 MKV to MP4 Converter (TV Optimized)

> **Automated CLI tool built in Python and FFmpeg to batch convert MKV video files to MP4 optimized for older TV models.**

---

## 📌 About The Project

As a tech enthusiast and Python developer, I believe the best portfolio projects are those that solve real-world daily problems. 

I frequently download public domain films and archives that come packaged in `.mkv` containers with multiple audio streams and embedded subtitles. However, playing these files on older smart TVs or via USB flash drives often results in playback errors or unsupported audio/video formats.

To eliminate the repetitive task of manually running complex terminal commands, I built this **Python CLI tool**. It automates the scanning, filtering, and re-muxing process using `FFmpeg` under the hood—ensuring 100% compatibility for TV playback while preserving video quality.

---

## ✨ Key Features

- **Automated Directory Scanning:** Intercepts invalid directory paths and verifies the presence of `.mkv` files using Python's native `os` module.
- **Smart Audio Mapping:** Allows the user to select 1 or 2 audio streams (extracting the primary audio stream, typically Portuguese/native).
- **Subtitle Control:** Keeps or strips embedded subtitles to avoid codec issues on legacy media players.
- **Ultra-Fast Stream Copying (`-c copy`):** Avoids time-consuming re-encoding, converting full-length 1080p movies in seconds without CPU burnout.
- **CLI Confirmation Summary:** Displays a clear configuration review before launching the batch job.
- **Live FFmpeg Progress Output:** Directly routes FFmpeg's real-time encoding speed, bitrate, and progress indicators to the terminal using `subprocess`.

---

## 🛠️ Tech Stack & Prerequisites

* **Language:** Python 3.x
* **Libraries:** `os`, `subprocess` (Python Native Standard Library)
* **System Environment:** Linux Mint / Linux Bash Terminal
* **Core External Dependency:** [FFmpeg](https://ffmpeg.org/)

> ⚠️ **Important Requirement:**  
> This script relies on `FFmpeg` to perform video/audio stream copying. Ensure `FFmpeg` is installed on your operating system and added to your system's PATH before running the application.  
> 
> On Linux Mint / Ubuntu, you can install it via terminal:
> sudo apt update && sudo apt install ffmpeg

---

## 🚀 How It Works

1. **Clone the repository:**
   git clone [https://github.com/allanpaolin/MKV_to_MP4_Converter.git](https://github.com/allanpaolin/MKV_to_MP4_Converter.git)
   cd MKV_to_MP4_Converter

2. **Run the application:**
   python3 main.py

3. **Follow the interactive CLI prompts:**
   MKV to MP4 Converter
   What is the files path? /home/user/Videos/Movies
   Found 2 MKV file(s)!
   MP4 with 1 or 2 audio tracks? [type 1 or 2]: 1
   Do you want to include subtitles? [y/n]: n

   --- SUMMARY ---
   Folder: /home/user/Videos/Movies
   Files to convert: 2
   Audio tracks selected: 1
   Subtitles selected: n
   ----------------
   Do you want to proceed with the conversion? [y/n]: y

   Starting conversion...
   Converting: Movie.mkv -> Movie.mp4
   Task finished successfully! All files converted.

---

## 💡 What I Learned / Engineering Takeaways

Building this tool was a key step in my transition to Back-End Development and Automation. Key technical accomplishments include:
- **String Manipulation & Slicing:** Dynamically stripping extensions (`file[:-4]`) and building output file names.
- **Loop Control & Validation:** Implementing `while True` logic blocks and error handling for robust user input parsing.
- **System Integration via `subprocess`:** Safely passing argument arrays (`list` format) to system binaries to handle file names containing spaces and special characters.
- **Automation Philosophy:** Applying code to eliminate manual, repetitive CLI workflows into a single executable script.

---

## 👤 Author

**Allan Jeison Paolin**  
*Back-End Python Developer | Automations & AI Solutions*  
- **LinkedIn:** [https://www.linkedin.com/in/allanpaolin/](https://www.linkedin.com/in/allanpaolin/)  
- **GitHub:** [https://github.com/allanpaolin](https://github.com/allanpaolin)