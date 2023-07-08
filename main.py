from kivy.config import Config
Config.set('graphics', 'resizable', False)
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget


class MainWidget(Widget):
    pass

Builder.load_file('main.kv')
class MyApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 1)
        Window.size = (1080, 720)
        self.title = 'Exchange Sort'
        return MainWidget()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    MyApp().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
