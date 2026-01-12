import numpy as np
import librosa
from scipy.signal import find_peaks

def detect_peaks(y, sr, hop_length=512, backtrack=True):

    onset_env = librosa.onset.onset_strength(y=y, sr=sr, hop_length=hop_length)

    peaks = find_peaks(onset_env, height=np.mean(onset_env)*1.5, distance=sr*0.05/hop_length)[0]

    peaks_samples = [p * hop_length for p in peaks]

    peaks_time = [p / sr for p in peaks_samples]
    
    return peaks_time, peaks_samples
