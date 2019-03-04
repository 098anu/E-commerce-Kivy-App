import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.listview import ListView,ListItemButton
from kivy.adapters.listadapter import ListAdapter
class Screen6(Screen):
    def getset(sertext):
        print(sertext)
        """
        xi=[]
        filename='state.csv'
        file=open(filename,'r')
        for line in file:
            xi.append(line.rstrip("\n"))
        if(loctext!=""):
            for y in xi:
                w=y[0]
                r1=re.findall(str(loctext.upper()),str(w))
                if(r1):
                    self.ids.loclist.adapter.data.append(str(y))
                
        else:
            self.ids.loclist.adapter.data=''
        self.ids.loclist.adapter.bind(on_selection_change=self.back)
        
        y=''
    
    def back(self,adapter):
        if len(self.ids.loclist.adapter.selection) == 0:
            print("No selected item")
            
        else:
            print(self.ids.loclist.adapter.selection[0].text)
            
            self.ids.loc.text=self.ids.loclist.adapter.selection[0].text
            self.ids['nav'].text = self.ids.loclist.adapter.selection[0].text
            self.ids.loclist.adapter.data=''
            print("afyter")
            print(self.ids.loclist.adapter.data)
            
            
            self.ids.loc.text=''

"""
