from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

Window.clearcolor = (70/255.0,0,2,0)
# Window.size = ()


class MainApp(App):
    def build(self):
        self.title = 'Salah System'
        pass


if __name__ == '__main__':
        # return super().build()
    MainApp().run()