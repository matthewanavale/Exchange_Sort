from kivy.config import Config
from kivy.core.text import Label
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

Config.set('graphics', 'resizable', False)
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget

class CustomPopup(BoxLayout):
    message = StringProperty("")
class MainWidget(Widget):
    inputs = [24,36,12,96,72,60,84,48]
    inputs.sort()

    def interpolation_search(self, search_input):
        low = 0
        high = len(self.inputs) -1
        while low <= high and search_input >= self.inputs[low] and search_input <= self.inputs[high]:
            pos = low + ((search_input - self.inputs[low]) // (self.inputs[high] - self.inputs[low])) * (high - low)
            pos = int(pos)
            if self.inputs[pos] == search_input:
                return pos
            elif self.inputs[pos] < search_input:
                low = pos + 1
            else:
                high = pos - 1

        return -1

    def on_enter(self):
        search_input_text = self.ids.inputs.text

        if search_input_text.strip():
            popup_content = CustomPopup()
            try:
                search_input = int(search_input_text)
                result = self.interpolation_search(search_input)

                if result == -1:
                    popup_content.message = str(search_input) + " does not exist." + "\n" + str(self.inputs)
                else:
                    popup_content.message = str(search_input) + " is at index " + str(result) + "\n" + str(self.inputs)

                popup = Popup(title="Search Result", content=popup_content, size_hint=(None, None), size=(400, 200))
                popup.open()

            except ValueError:
                popup_content.message = "Invalid input. Please enter an integer."
                popup = Popup(title="Error", content=popup_content, size_hint=(None, None), size=(400, 200))
                popup.open()

Builder.load_file('main.kv')
class MyApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 1)
        Window.size = (480, 360)
        self.title = 'Interpolation Search'
        return MainWidget()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    MyApp().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
