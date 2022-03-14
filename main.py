import kivy
import sys
import os
import urllib3

from kivy.app import App
from kivy import Config
Config.set('graphics', 'multisamples', '0')
kivy.require('1.10.0')
new_environ = os.environ.copy()

from kivy.uix.button import Label, Button 
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.base import runTouchApp


######################################
import requests 
######################################


class LameApp():
    def __init__(self, **kwargs):
       self.layout = BoxLayout(orientation='vertical')

       self.post = TextInput(multiline=False)
      
       self.submit = Button(text="Submit", font_size=40)
       self.submit.bind(on_press=self.pressed) 

       self.layout.add_widget(self.post)
       self.layout.add_widget(self.submit)

       self.dumbmessage =  Label(text = "congrats!" )

       self.mainpage = Button(text = "See all Posts!")
       self.mainpage.bind(on_press = self.postpage)


       runTouchApp(self.layout)

    def pressed(self, instance):
        print("blah blah")

        print("blah blah")

        dictToSend = {'content': self.post.text }
        res = requests.post('http://104.237.128.94:5000/post', json=dictToSend)

        
        self.layout.remove_widget(self.post)
        self.layout.remove_widget(self.submit)
        try: 
            self.layout.remove_widget(self.dumbmessage)
        except  UnboundLocalError:
          print("something went wrong: dumbmessage") 
        try: 
            self.layout.remove_widget(self.mainpage)
        except  UnboundLocalError:
          print("something went wrong: self.mainpage")


        
        self.post = TextInput(multiline=False)
        
        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed) 

        self.layout.add_widget(self.dumbmessage)
        self.layout.add_widget(self.post)
        self.layout.add_widget(self.submit)

        self.layout.add_widget(self.mainpage)



    
    def postpage(self, instance):
        print("postpage pressed")

        self.layout.remove_widget(self.post)
        self.layout.remove_widget(self.submit)
        self.layout.remove_widget(self.dumbmessage)

        res = requests.get('http://104.237.128.94:5000/api/all')
        if res.ok:
            for post in res.json():
              l = Label(text = post['content'])
              self.layout.add_widget(l)
               
       
class Dumbclass(App):
    def build(self):
        return LameApp()
Dumbclass().run()
   
