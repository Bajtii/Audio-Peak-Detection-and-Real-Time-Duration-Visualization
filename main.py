from audio_extraction import load_audio, save_wav
from preprocessing import normalize_audio, bandpass_filter
from peak_detection import detect_peaks
from analysis import calculate_durations, save_durations_csv
from visualization import plot_durations_bar, plot_duration_histogram, print_duration_stats
import matplotlib.pyplot as plt
import os


file_path = "C:/Users/PLBAWOJ6/Desktop/Audios/LastConverted.mp3"
y, sr = load_audio(file_path)
print(f"Wczytano audio: {len(y)} próbek, sr={sr} Hz")

y_norm = normalize_audio(y)
print("Audio znormalizowane")

y_filtered = bandpass_filter(y_norm, lowcut=80, highcut=5000, fs=sr)
print("Zastosowano filtr pasmowo-przepustowy")

output_folder = "C:/Users/PLBAWOJ6/Documents/work/Audio_detection/test_audio"
output_path = os.path.join(output_folder, "sample_filtered.wav")

save_wav(y_filtered, sr, output_path)
print(f"Zapisano przetworzone audio jako {output_path}")

peaks_time, peaks_samples = detect_peaks(y_filtered, sr)
print(f"Wykryto {len(peaks_time)} pików")


plt.figure(figsize=(12, 4))
plt.plot(y_filtered, color='blue', label='Sygnał')
plt.vlines(peaks_samples, ymin=min(y_filtered), ymax=max(y_filtered), color='red', alpha=0.7, label='Piki')
plt.title("Sygnał audio po normalizacji i filtracji z zaznaczonymi pikami")
plt.xlabel("Próbki")
plt.ylabel("Amplituda")
plt.legend()
plt.show()

print("Wszystkie wykryte piki (czas w sekundach):")
for i, t in enumerate(peaks_time, start=1):
    print(f"{i:3d}: {t:.3f}s")  

print(f"\nŁączna liczba wykrytych pików: {len(peaks_time)}")

durations = calculate_durations(peaks_time)

print("\nWszystkie dźwięki z czasem trwania:")
for d in durations:
    duration_str = f"{d['duration']:.3f}s" if d['duration'] is not None else "Brak następnego piku"
    print(f"{d['numer']:3d}: start={d['start']:.3f}s, duration={duration_str}")

output_csv = os.path.join(output_folder, "durations.csv")
save_durations_csv(durations, output_csv)
print(f"\nWyniki analizy czasu trwania zapisane do pliku: {output_csv}")

plot_durations_bar(durations)
plot_duration_histogram(durations)
print_duration_stats(durations)

