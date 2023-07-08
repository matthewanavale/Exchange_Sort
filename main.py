from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

Builder.load_file('main.kv')


class SuggestionButton(Button):
    pass


class PhonebookSearchApp(App):
    def build(self):
        Window.clearcolor = (0/255, 25/255, 51/255, 1)
        Window.size = (360, 390)
        return PhonebookSearchLayout()


class PhonebookSearchLayout(Widget):
    def on_enter(self, instance):
        search_input = (instance.text)
        instance.text = ""

        phone_number = self.interpolation_search(search_input)

        if phone_number is None:
            popup_content = Label(text="Name not found in phonebook")
            popup = Popup(title='Search Result', content=popup_content, size_hint=(None, None), size=(300, 150))
            popup.open()
        else:
            popup_content = Label(text="Phone Number: " + phone_number)
            popup = Popup(title='Search Result', content=popup_content, size_hint=(None, None), size=(300, 150))
            popup.open()
    def interpolation_search(self, search_input):
        phonebook = [
            {'name': 'daph', 'phone': '09079419021'},
            {'name': 'denden', 'phone': '09123456734'},
            {'name': 'jaypee', 'phone': '09298837811'},
            {'name': 'jk', 'phone': '09876543210'},
            {'name': 'sienna', 'phone': '09761709251'}
        ]

        sorted_phonebook = sorted(phonebook, key=lambda entry: entry['name'].lower())  # Sort phonebook by name

        low = 0
        high = len(sorted_phonebook) - 1

        while low <= high and search_input.lower() >= sorted_phonebook[low]['name'].lower() and search_input.lower() <= sorted_phonebook[high]['name'].lower():
            pos = low + ((search_input.lower() >= sorted_phonebook[low]['name'].lower()) * (high - low)) // (sorted_phonebook[high]['name'].lower() >= sorted_phonebook[low]['name'].lower())
            pos = int(pos)

            if sorted_phonebook[pos]['name'].lower() == search_input.lower():
                return sorted_phonebook[pos]['phone']
            elif sorted_phonebook[pos]['name'].lower() < search_input.lower():
                low = pos + 1
            else:
                high = pos - 1

        return None  # Return None when the name is not found

    def show_suggestions(self, text):
        suggestions_box = self.ids.suggestions_box
        suggestions_box.clear_widgets()

        if text:
            for entry in self.get_matching_entries(text):
                suggestion_button = SuggestionButton(text=entry['name'])
                suggestion_button.bind(on_release=lambda button: self.fill_input(button.text))
                suggestions_box.add_widget(suggestion_button)

    def get_matching_entries(self, text):
        phonebook = [
            {'name': 'daph', 'phone': '09079362021'},
            {'name': 'denden', 'phone': '09123456734'},
            {'name': 'jaypee', 'phone': '09298808811'},
            {'name': 'jk', 'phone': '09176543210'},
            {'name': 'sienna', 'phone': '09761743251'}
        ]

        return [entry for entry in phonebook if entry['name'].startswith(text)]

    def fill_input(self, text):
        input_box = self.ids.input_box
        input_box.text = text

    def set_focus(self):
        input_box = self.ids.input_box
        input_box.focus = True



PhonebookSearchApp().run()
