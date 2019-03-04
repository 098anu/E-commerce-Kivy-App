import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager,Screen
import geocoder
from kivy.properties import ObjectProperty,StringProperty
from kivy.clock import Clock
import socket
from toast.kivytoast import toast
qw=0
class Screen4(Screen):
    def __init__(self, **kwargs):
        super(Screen4, self).__init__(**kwargs)
    def do_try():
        print('trying scrren 4')
    
    def detect(self):
        
        
        hostname = socket.gethostname()    
        IPAddr = socket.gethostbyname(hostname)    
        print("Your Computer Name is:" + hostname)    
        print("Your Computer IP Address is:" + IPAddr)
        g=geocoder.ip(IPAddr)
        g=geocoder.ip('me')
        print(g.latlng,g.state,g.city,g.street,g.country)
       # print(g.city)
        lep=[g.city,g.country,g.street]
        self.ids['nav'].text = str(','.join(lep))

        global qw
        qw+=1
        if(qw==1):
            toast('Current location is %s,\ntap again if you want to change location manually'% str(','.join(lep)))
            print(qw)
            
        else:
            
            print(qw)
            self.a = App.get_running_app()
            self.a.root.current='screen_5'
            
            qw=0
         
    def do_pass(self,setext):
        if(len(setext)==0):
            print('hry')
        else:
            self.a = App.get_running_app()
            self.a.root.current='screen_6'
            self.ids.se.text=''
