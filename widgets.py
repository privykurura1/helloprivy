#import kivy
import kivy 
# put the minimum support for kivy
kivy.require('1.7.0')

# import the app , thus our main app 
from kivy.app import App
from kivy.uix.widget import Widget

#you can create your own widgets like example below
class MyWidget(Widget):
    pass

class WidgetApp(App):
    def build(self):
        return MyWidget()
    
    
if __name__== "__main__":
    WidgetApp().run()