"""
CP1404 Practical 8
Miles to Kilometres Converter exercise.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILE_TO_KM_RATE = 1.60934


class ConvertMilesKm(App):
    """Kivy App for converting miles to kilometres."""
    output_text = StringProperty()

    def build(self):
        """Build the Kivy App using the .kv file."""
        Window.size = (600, 400)
        self.title = "Miles to Kilometres Conversion App"
        self.root = Builder.load_file("convert_miles_km.kv")
        self.output_text = ""
        return self.root

    def handle_convert(self):
        """Handle conversion of miles to kilometres, output result to Label Widget."""
        result = self.get_valid_miles() * MILE_TO_KM_RATE
        self.output_text = str(result)

    def handle_number_increment(self, change):
        """Handle increment of input number in the TextInput Widget."""
        value = self.get_valid_miles() + change
        self.root.ids.input_number.text = str(value)

    def get_valid_miles(self):
        """Get the input miles as a float, returns 0 if the input is empty or a string."""
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


ConvertMilesKm().run()
