from kivy.config import Config
Config.set('graphics', 'resizable', False)
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget


class MainWidget(Widget):
    inputs = [87, 25, 33, 48, 52, 58, 93, 999]
    inputs.sort()

    def interpolation_search(self, search_input):
        low = 0
        high = len(self.inputs) - 1

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
        input_text = self.ids.inputs.text
        self.ids.inputs.text = ""

        search_input = int(input_text)
        pos = int(self.interpolation_search(search_input))

        if pos == -1:
            print( str(search_input) + " does not exist.")
        else:
            print(pos)
            print(str(search_input) + " is at index " + str(pos))
            print("index " + str(pos) + " is: " + str(self.inputs[pos]))

Builder.load_file('main.kv')
class MyApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 1)
        Window.size = (1080, 720)
        self.title = 'Interpolation Search'
        return MainWidget()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    MyApp().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
