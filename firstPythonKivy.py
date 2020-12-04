from kivy.app import App
from kivy.uix.button import Button

from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')

from kivy.uix.floatlayout import FloatLayout


class TestApp(App):
    def build(self):

        fl = FloatLayout(size = (300, 300))
        fl.add_widget(Button(text = 'hello world',
                      font_size = 16,
                      on_press = self.btn_press,
                      background_color = [.32, .85, .94, 1],
                      background_normal = '',
                      size_hint = (.5, .25),
                      pos = (640 / 2 - 160, 0)))

        return fl

    def btn_press(self, instance):
        print('кнопка нажата!')
        instance.text = 'hi'


if __name__ == '__main__':
    TestApp().run()
