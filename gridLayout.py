from kivy.app import App
from kivy.uix.button import Button

from kivy.uix.gridlayout import GridLayout


class GridApp(App):
    def build(self):
        gl = GridLayout(cols = 2, rows = 2)

        gl.add_widget(Button(text = 'button 1'))
        gl.add_widget(Button(text = 'button 2'))
        gl.add_widget(Button(text = 'button 3'))
        gl.add_widget(Button(text = 'button 4'))

        return gl


if __name__ == '__main__':
    GridApp().run()
