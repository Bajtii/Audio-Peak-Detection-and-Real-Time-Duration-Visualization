import numpy as np
from scipy.signal import butter, lfilter

def stereo_to_mono(y):
    """
    Konwertuje sygnał stereo do mono, jeśli sygnał ma 2 kanały
    """
    if len(y.shape) == 2:
        y = np.mean(y, axis=1)
    return y

def normalize_audio(y):
    """
    Normalizuje sygnał audio do zakresu -1.0 do 1.0
    """
    max_val = np.max(np.abs(y))
    if max_val == 0:
        return y
    return y / max_val

def butter_bandpass(lowcut, highcut, fs, order=4):
    """
    Tworzy współczynniki filtra pasmowo-przepustowego
    """
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def bandpass_filter(y, lowcut=80, highcut=5000, fs=44100, order=4):
    """
    Stosuje filtr pasmowo-przepustowy do sygnału audio
    """
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y_filtered = lfilter(b, a, y)
    return y_filtered
