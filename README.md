# 🎸 Audio Peak Detection & Real-Time Duration Visualization  
### Python Audio Signal Processing Project

---

## 📌 Project Description

This project focuses on **audio signal analysis** and **real-time visualization** of transient sound events such as **guitar string plucks**.

The system detects **temporal peaks** in an audio signal, computes their **durations**, and visualizes them dynamically while the audio is being played.

The project combines **digital signal processing (DSP)** techniques with **real-time animation** and **audio playback synchronization**, providing both **offline analysis** and **live visualization**.

---

## 🔁 Project Workflow

The project workflow is divided into the following stages:

---

### 1️⃣ Audio Loading and Preprocessing Phase

The input audio file (`.mp3`) is loaded and converted into a **mono waveform**.  
The signal is then **normalized** and optionally filtered using a **band-pass filter** to isolate relevant frequency ranges (e.g. guitar strings).

<img width="1112" height="387" alt="Audio Preprocessing" src="https://github.com/user-attachments/assets/143088d0-79c7-4430-a84f-982fdfbd4093" />

---

### 2️⃣ Peak (Pluck) Detection Phase

Transient peaks are detected from the processed waveform.  
Each peak corresponds to a likely **string pluck** or **sound onset**.

The detected peaks are visualized directly on the waveform, allowing clear verification of detection accuracy.

<img width="1149" height="439" alt="Peak Detection" src="https://github.com/user-attachments/assets/33ec9e56-2c88-4f18-be14-671fea848ba5" />

---

### 3️⃣ Duration Analysis Phase

Durations are computed as **time differences between consecutive detected peaks**.

Each detected sound event is represented as:

- **start time**
- **duration until the next event**

The results can be printed to the console and exported to a **CSV file** for further analysis.

<img width="400" height="752" alt="Duration Analysis Output" src="https://github.com/user-attachments/assets/c743b290-dd60-4861-954b-dfafd09515e5" />

---

### 4️⃣ Static Visualization Phase

A static **bar chart** is generated, where:

- **X-axis** represents the peak number  
- **Y-axis** represents the duration of each detected sound  

This provides a clear global overview of **rhythmic structure** and **note spacing**.

<img width="1575" height="893" alt="Static Visualization" src="https://github.com/user-attachments/assets/f8d2b71a-7dc8-4d2b-a97f-58783e55e366" />

---

### 5️⃣ Real-Time Playback and Animated Visualization Phase

The audio is played back while a **real-time animated bar chart** visualizes the duration of each peak:

- Bars grow smoothly while the sound is active  
- The animation is synchronized with audio playback  
- The **current playback time** is displayed above the chart  
- An interactive **END button** allows clean termination of playback and visualization  

This phase demonstrates **real-time synchronization** between audio processing and graphical rendering.

<img width="1066" height="470" alt="Real-Time Visualization" src="https://github.com/user-attachments/assets/cd9d28d3-9299-40a5-a6de-54af4b3db676" />

---

The project is implemented entirely in **Python**, integrating signal processing, numerical computation, real-time audio playback, and data visualization into a coherent analytical tool.

---

## ⚙️ Technologies and Tools

- **Python 3.10+** – core programming language  
- **NumPy** – numerical operations on audio signals  
- **Librosa** – audio loading and preprocessing  
- **SciPy** – digital signal processing (filters)  
- **SoundDevice** – real-time audio playback  
- **Matplotlib** – plotting and real-time animation  
- **SoundFile** – saving processed audio to WAV  

---

## 🧠 Core Concepts Implemented

- Digital signal preprocessing  
- Peak (onset) detection  
- Temporal event analysis  
- Real-time visualization loops  
- Audio–visual synchronization  
- Modular pipeline design  

---

## 🧩 Features

- Detection of transient audio events (plucks)  
- Accurate timing with millisecond precision  
- Duration analysis between consecutive peaks  
- Static and real-time visualizations  
- Smooth animated bar growth  
- Live playback time display  
- Interactive GUI button for controlled termination  
- Exportable numerical results (CSV)  
- Clean, modular code structure  

---

## 📂 Project Structure

```text
Audio_detection/
│
├── audio_extraction.py        # Audio loading and saving
├── preprocessing.py           # Normalization and filtering
├── peak_detection.py          # Peak detection logic
├── analysis.py                # Duration calculations
├── visualization.py           # Static plots
├── main.py                    # Offline analysis pipeline
├── real_time_visualization.py # Real-time playback & animation
│
└── test_audio/
    └── sample_filtered.wav
