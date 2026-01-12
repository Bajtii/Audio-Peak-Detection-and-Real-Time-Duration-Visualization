import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import sounddevice as sd
from audio_extraction import load_audio
from peak_detection import detect_peaks
from analysis import calculate_durations
import time

file_path = r"C:/Users/PLBAWOJ6/Desktop/Audios/Pirates.mp3"
y, sr = load_audio(file_path)

peaks_time, peaks_samples = detect_peaks(y, sr)
durations = calculate_durations(peaks_time)
print(f"Wykryto {len(durations)} pików")

max_duration = max([d['duration'] for d in durations if d['duration'] is not None])

fig, ax = plt.subplots(figsize=(12,5))
bars = ax.bar([d['numer'] for d in durations], np.zeros(len(durations)), color='blue')
ax.set_xlabel("Numer piku")
ax.set_ylabel("Czas trwania [s]")
ax.set_title("Czas trwania pików w czasie rzeczywistym | Aktualny czas: 0.00s")
ax.set_ylim(0, max_duration*1.1)
plt.ion()
plt.show()

end_program = False  

def end(event):
    global end_program
    sd.stop()
    end_program = True
    plt.close(fig)
    print("Program zakończony")


ax_end = plt.axes([0.8, 0.02, 0.1, 0.05])
btn_end = Button(ax_end, 'END')
btn_end.on_clicked(end)


sd.play(y, sr)
start_time = time.time()

for i, d in enumerate(durations):
    pik_start = d['start']
    pik_duration = d['duration'] if d['duration'] is not None else 0.05
    elapsed = 0

    while elapsed < pik_duration and not end_program:
        elapsed = time.time() - start_time - pik_start
        height = max(0, min(elapsed, pik_duration))
        bars[i].set_height(height)
        
        current_time = time.time() - start_time
        ax.set_title(f"Czas trwania pików w czasie rzeczywistym | Aktualny czas: {current_time:.2f}s")
        
        fig.canvas.draw()
        fig.canvas.flush_events()
        time.sleep(0.01)

sd.wait()
plt.ioff()
plt.show()
