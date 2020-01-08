from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window._window_sdl2 import _WindowSDL2Storage

class TestApp(App):
    def build(self):
        return Button(text='Hello World')

TestApp().run()