# Dictionary to map note names to their semitone values
notes_to_semitones = {
    'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11,
    'Db': 1, 'Eb': 3, 'Gb': 6, 'Ab': 8, 'Bb': 10
}

# List of semitone values to map back to note names
semitones_to_notes = {v: k for k, v in notes_to_semitones.items()}

def calculate_new_tuning(current_tuning, semitone_change):
    new_tuning = []
    for note in current_tuning:
        current_value = notes_to_semitones[note]
        new_value = (current_value + semitone_change) % 12
        new_tuning.append(semitones_to_notes[new_value])
    return new_tuning

# Example usage
number_of_strings = 6
current_tuning = ['C#', 'G#', 'C#', 'F#', 'A#', 'D#']  # Drop C# tuning

# Adjust the semitone difference using a slider (for example, +2 semitones)
semitone_change = 2

new_tuning = calculate_new_tuning(current_tuning, semitone_change)
print("New tuning after changing semitones:", new_tuning)
