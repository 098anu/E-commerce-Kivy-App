import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import StringProperty,ObjectProperty
from kivymd.navigationdrawer import NavigationDrawer
from kivymd.toolbar import Toolbar
from kivymd.theming import ThemeManager
from kivy.uix.label import Label


class Navigator(NavigationDrawer):
    image_source = StringProperty('images/usi.jpg')
    
    title = StringProperty('Navigation')
    def __init__(self,**kwargs):
        super(Navigator, self).__init__(**kwargs)
        
        self.ids.lb1.text='Hi, User'
        self.ids.lb2.text='91-9661197143'
       
        self.lab=Label(text='  [b]MORE[/b]',color=(0,0,205,1),size_hint=(1,None),height=30, halign="left", valign="middle",markup=True)
        self.lab.bind(size=self.lab.setter('text_size')) 
        self.widget_list.add_widget(self.lab,6)
    def chg_scr(self):
        self.a = App.get_running_app()
        self.a.root.current='screen_20'
        self.a.nav_drawer.toggle()
class NavigateSales(NavigationDrawer):
    image_source = StringProperty('images/usi.jpg')
    title = StringProperty('Navigation')
    def __init__(self,**kwargs):
        super(NavigateSales, self).__init__(**kwargs)
        
        self.ids.lb1.text='Hi, User'
        self.ids.lb2.text='91-9661197143'
       

    def chg_scr(self):
        self.a = App.get_running_app()
        self.a.root.current='screen_20'
        self.a.nav_dra.toggle()
        
class Screen20(Screen):
    image_source=StringProperty('usi.jpg')
    def chg_scr(self):
        self.a = App.get_running_app()
        self.a.root.current='screen_4'
        self.a.nav_drawer.toggle()
    def on_press(self, index):
        flash_display_screen = self.manager.get_screen('screen_18')
        setattr(flash_display_screen, 'index', index)
        self.manager.current='screen_18'
class MultiApp(App):
    theme_cls=ThemeManager()
    nav_drawer = ObjectProperty()
    nav_dra =ObjectProperty()
    
    
    
    def build(self):
        print('hey')
        self.nav_drawer=Navigator()
        self.scre20=Screen20()
       
        self.nav_dra=NavigateSales()
        self.load_kv('multi.kv')

    def on_pause(self):
        return True

    def on_resume(self):
        pass
if __name__ == "__main__":
    MultiApp().run()
        
