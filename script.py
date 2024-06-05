import tkinter as tk
from tkinter import ttk

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

def calculate_new_tuning(current_tuning, semitone_change):
    new_tuning = []
    for note in current_tuning:
        current_value = notes_to_semitones[note]
        new_value = (current_value + semitone_change) % 12
        new_tuning.append(semitones_to_notes[new_value])
    return new_tuning

def update_tuning_label():
    semitone_change = semitone_slider.get()
    new_tuning = calculate_new_tuning(current_tuning_var.get().split(), semitone_change)
    tuning_label.config(text="New Tuning: " + " ".join(new_tuning))

def update_semitone_difference():
    current_tuning = current_tuning_var.get().split()
    desired_tuning = desired_tuning_var.get().split()
    semitone_differences = calculate_semitone_difference(current_tuning, desired_tuning)
    semitone_diff_label.config(text="Semitone Differences: " + " ".join(map(str, semitone_differences)))

# Create the main application window
root = tk.Tk()
root.title("Guitar Tuning Calculator")

# Input for number of strings
number_of_strings_label = tk.Label(root, text="Number of Strings:")
number_of_strings_label.pack()
number_of_strings = tk.IntVar()
number_of_strings.set(6)
number_of_strings_entry = tk.Entry(root, textvariable=number_of_strings)
number_of_strings_entry.pack()

# Input for current tuning
current_tuning_label = tk.Label(root, text="Current Tuning (space-separated):")
current_tuning_label.pack()
current_tuning_var = tk.StringVar()
current_tuning_var.set('C# G# C# F# A# D#')
current_tuning_entry = tk.Entry(root, textvariable=current_tuning_var)
current_tuning_entry.pack()

# Input for desired tuning
desired_tuning_label = tk.Label(root, text="Desired Tuning (space-separated):")
desired_tuning_label.pack()
desired_tuning_var = tk.StringVar()
desired_tuning_var.set('D A D G B E')
desired_tuning_entry = tk.Entry(root, textvariable=desired_tuning_var)
desired_tuning_entry.pack()

# Button to calculate semitone differences
calculate_button = tk.Button(root, text="Calculate Semitone Differences", command=update_semitone_difference)
calculate_button.pack()

# Label to display semitone differences
semitone_diff_label = tk.Label(root, text="Semitone Differences: ")
semitone_diff_label.pack()

# Create and place the slider for semitone change
semitone_slider = tk.Scale(root, from_=-12, to=12, orient=tk.HORIZONTAL, label="Semitone Change")
semitone_slider.pack()

# Create and place the label to display the new tuning
tuning_label = tk.Label(root, text="New Tuning: ")
tuning_label.pack()

# Update the tuning label whenever the slider value changes
semitone_slider.bind("<Motion>", lambda event: update_tuning_label())

# Start the Tkinter event loop
root.mainloop()
