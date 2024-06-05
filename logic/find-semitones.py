# Dictionary to map note names to their semitone values
notes_to_semitones = {
    'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11,
    'Db': 1, 'Eb': 3, 'Gb': 6, 'Ab': 8, 'Bb': 10
}

# List of semitone values to map back to note names
semitones_to_notes = {v: k for k, v in notes_to_semitones.items()}

def calculate_semitone_difference(current_tuning, desired_tuning):
    differences = []
    for current_note, desired_note in zip(current_tuning, desired_tuning):
        current_value = notes_to_semitones[current_note]
        desired_value = notes_to_semitones[desired_note]
        difference = desired_value - current_value
        differences.append(difference)
    return differences

# Example usage
number_of_strings = 6
current_tuning = ['C#', 'G#', 'C#', 'F#', 'A#', 'D#']  # Drop C# tuning
desired_tuning = ['D', 'A', 'D', 'G', 'B', 'E']  # Drop D tuning

semitone_differences = calculate_semitone_difference(current_tuning, desired_tuning)
print("Semitone differences for each string:", semitone_differences)
