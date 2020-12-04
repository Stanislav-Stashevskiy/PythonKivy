from kivy.app import App
from kivy.uix.button import Button

from kivy.uix.boxlayout import BoxLayout


class BoxApp(App):
    def build(self):
        bl = BoxLayout(orientation = 'vertical', padding = [20],spacing = 25)

        bl.add_widget(Button(text = 'hello'))
        bl.add_widget(Button(text = 'hi'))
        bl.add_widget(Button(text = '123'))

        return bl


if __name__ == '__main__':
   BoxApp().run()
