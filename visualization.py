import matplotlib.pyplot as plt
import numpy as np

def plot_durations_bar(durations):
    """
    Rysuje wykres słupkowy czasu trwania każdego dźwięku
    
    Args:
        durations (list of dict): lista z czasem rozpoczęcia i trwania dźwięku
    """
    numbers = [d['numer'] for d in durations if d['duration'] is not None]
    duration_values = [d['duration'] for d in durations if d['duration'] is not None]

    plt.figure(figsize=(14, 5))
    plt.bar(numbers, duration_values, color='skyblue')
    plt.xlabel("Numer piku")
    plt.ylabel("Czas trwania [s]")
    plt.title("Czas trwania każdego szarpnięcia struny")
    plt.show()

def plot_duration_histogram(durations, bins=30):
    """
    Rysuje histogram czasów trwania dźwięków
    
    Args:
        durations (list of dict): lista z czasem trwania dźwięku
        bins (int): liczba przedziałów histogramu
    """
    duration_values = [d['duration'] for d in durations if d['duration'] is not None]

    plt.figure(figsize=(10, 4))
    plt.hist(duration_values, bins=bins, color='salmon', edgecolor='black')
    plt.xlabel("Czas trwania [s]")
    plt.ylabel("Liczba pików")
    plt.title("Histogram czasów trwania szarpnięć strun")
    plt.show()

def print_duration_stats(durations):
    """
    Wypisuje podstawowe statystyki czasów trwania
    """
    duration_values = [d['duration'] for d in durations if d['duration'] is not None]
    if not duration_values:
        print("Brak danych do analizy statystycznej")
        return

    mean = np.mean(duration_values)
    min_val = np.min(duration_values)
    max_val = np.max(duration_values)
    std = np.std(duration_values)

    print("\nStatystyki czasów trwania szarpnięć strun:")
    print(f"Średni czas: {mean:.3f}s")
    print(f"Minimalny czas: {min_val:.3f}s")
    print(f"Maksymalny czas: {max_val:.3f}s")
    print(f"Odchylenie standardowe: {std:.3f}s")
