from kivy.main import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.button import Button

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

class GuitarTuningApp(App):
    def build(self):
        self.title = "Guitar Tuning Calculator"

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.entry_strings = TextInput(hint_text="Enter number of strings", multiline=False)
        layout.add_widget(Label(text="Number of Strings:"))
        layout.add_widget(self.entry_strings)

        self.entry_current_tuning = TextInput(hint_text="e.g. C# G# C# F# A# D#", multiline=False)
        layout.add_widget(Label(text="Current Tuning (space-separated):"))
        layout.add_widget(self.entry_current_tuning)

        self.entry_desired_tuning = TextInput(hint_text="e.g. D A D G B E", multiline=False)
        layout.add_widget(Label(text="Desired Tuning (space-separated):"))
        layout.add_widget(self.entry_desired_tuning)

        self.button_calculate = Button(text="Calculate Semitone Differences", on_press=self.update_semitone_difference)
        layout.add_widget(self.button_calculate)

        self.semitone_diff_label = Label(text="Semitone Differences: ")
        layout.add_widget(self.semitone_diff_label)

        self.slider_label = Label(text="Semitone Change: 0")
        layout.add_widget(self.slider_label)

        self.semitone_slider = Slider(min=-12, max=12, step=1, value=0)
        self.semitone_slider.bind(value=self.update_tuning_label)
        layout.add_widget(self.semitone_slider)

        self.tuning_label = Label(text="New Tuning: ")
        layout.add_widget(self.tuning_label)

        return layout

    def update_semitone_difference(self, instance):
        current_tuning = self.entry_current_tuning.text.split()
        desired_tuning = self.entry_desired_tuning.text.split()
        semitone_differences = calculate_semitone_difference(current_tuning, desired_tuning)
        self.semitone_diff_label.text = "Semitone Differences: " + " ".join(map(str, semitone_differences))

    def update_tuning_label(self, instance, value):
        semitone_change = int(value)
        self.slider_label.text = f"Semitone Change: {semitone_change}"
        current_tuning = self.entry_current_tuning.text.split()
        new_tuning = calculate_new_tuning(current_tuning, semitone_change)
        self.tuning_label.text = "New Tuning: " + " ".join(new_tuning)

if __name__ == "__main__":
    GuitarTuningApp().run()
