""" 
Ejemplo 2-7. Accesando 
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()
    def search_location(self):
        print "El usuario busco '{}'".format(self.search_input.text)
        

class WeatherApp(App):
    pass

#El archivo .kv debe llevar el nombre de la clase pero sin App
WeatherApp().run()