import csv

def calculate_durations(peaks_time):

    durations = []
    for i in range(len(peaks_time)):
        start = peaks_time[i]
        if i < len(peaks_time) - 1:
            duration = peaks_time[i+1] - start
        else:
            duration = None  
        durations.append({
            "numer": i+1,
            "start": start,
            "duration": duration
        })
    return durations

def save_durations_csv(durations, filename):

    with open(filename, mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["numer", "start", "duration"])
        writer.writeheader()
        for row in durations:
            writer.writerow(row)
