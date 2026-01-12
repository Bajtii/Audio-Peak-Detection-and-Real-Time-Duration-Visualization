import librosa
import soundfile as sf
import os
import numpy as np

def load_audio(file_path, sr=44100):

    y, sr = librosa.load(file_path, sr=sr, mono=True)
    return y, sr

def save_wav(y, sr, output_path):

    folder = os.path.dirname(output_path)
    if folder != "" and not os.path.exists(folder):
        os.makedirs(folder)

    # Konwersja do float32
    y_to_save = y.astype(np.float32)

    sf.write(output_path, y_to_save, sr)
