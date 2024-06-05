import customtkinter as ctk
import tkinter as tk

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

class GuitarTuningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Guitar Tuning Calculator")

        # Set customtkinter appearance mode and color theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # Create main frame with customtkinter style
        self.frame = ctk.CTkFrame(master=root)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        # Number of strings input
        self.label_strings = ctk.CTkLabel(master=self.frame, text="Number of Strings:", font=("Helvetica", 14, "bold"))
        self.label_strings.grid(row=0, column=0, pady=5, padx=10, sticky="w")
        self.entry_strings = ctk.CTkEntry(master=self.frame, placeholder_text="Enter number of strings", font=("Helvetica", 12))
        self.entry_strings.grid(row=0, column=1, pady=5, padx=10, sticky="w")

        # Current tuning input
        self.label_current_tuning = ctk.CTkLabel(master=self.frame, text="Current Tuning (space-separated):", font=("Helvetica", 14, "bold"))
        self.label_current_tuning.grid(row=1, column=0, pady=5, padx=10, sticky="w")
        self.entry_current_tuning = ctk.CTkEntry(master=self.frame, placeholder_text="e.g. C# G# C# F# A# D#", font=("Helvetica", 12))
        self.entry_current_tuning.grid(row=1, column=1, pady=5, padx=10, sticky="w")

        # Desired tuning input
        self.label_desired_tuning = ctk.CTkLabel(master=self.frame, text="Desired Tuning (space-separated):", font=("Helvetica", 14, "bold"))
        self.label_desired_tuning.grid(row=2, column=0, pady=5, padx=10, sticky="w")
        self.entry_desired_tuning = ctk.CTkEntry(master=self.frame, placeholder_text="e.g. D A D G B E", font=("Helvetica", 12))
        self.entry_desired_tuning.grid(row=2, column=1, pady=5, padx=10, sticky="w")

        # Calculate button for semitone differences
        self.button_calculate = ctk.CTkButton(master=self.frame, text="Calculate Semitone Differences", command=self.update_semitone_difference)
        self.button_calculate.grid(row=3, column=1, pady=20)

        # Label to display semitone differences
        self.semitone_diff_label = ctk.CTkLabel(master=self.frame, text="Semitone Differences: ", font=("Helvetica", 12))
        self.semitone_diff_label.grid(row=4, column=0, columnspan=2, pady=10)

        # Slider for semitone change
        self.semitone_slider = ctk.CTkSlider(master=self.frame, from_=-12, to=12, number_of_steps=24, command=self.update_tuning_label)
        self.semitone_slider.grid(row=5, column=0, columnspan=2, pady=20)
        self.slider_label = ctk.CTkLabel(master=self.frame, text="Semitone Change: 0", font=("Helvetica", 12))
        self.slider_label.grid(row=6, column=0, columnspan=2)

        # Label to display the new tuning
        self.tuning_label = ctk.CTkLabel(master=self.frame, text="New Tuning: ", font=("Helvetica", 12))
        self.tuning_label.grid(row=7, column=0, columnspan=2, pady=10)

    def update_semitone_difference(self):
        try:
            current_tuning = self.entry_current_tuning.get().split()
            desired_tuning = self.entry_desired_tuning.get().split()
            semitone_differences = calculate_semitone_difference(current_tuning, desired_tuning)
            self.semitone_diff_label.configure(text="Semitone Differences: " + " ".join(map(str, semitone_differences)))
        except Exception as e:
            print(f"Error in calculating semitone difference: {e}")

    def update_tuning_label(self, value):
        try:
            semitone_change = int(float(value))
            self.slider_label.configure(text=f"Semitone Change: {semitone_change}")
            current_tuning = self.entry_current_tuning.get().split()
            new_tuning = calculate_new_tuning(current_tuning, semitone_change)
            self.tuning_label.configure(text="New Tuning: " + " ".join(new_tuning))
        except Exception as e:
            print(f"Error in updating tuning label: {e}")

if __name__ == "__main__":
    root = ctk.CTk()
    app = GuitarTuningApp(root)
    root.mainloop()
