import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen

class Screen12(Screen):
    def chg_scr(self):
        self.a = App.get_running_app()
        self.a.root.current='screen_4'
