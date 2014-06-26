""" 
Ejemplo 2-5. Agregando una propiedad que apunte al widget de busqueda
Y modificando el .kv para agregar la busqueda y el valor de la propiedad.
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()
    def search_location(self):
        print "Explicito es mejor que implicito"
        

class WeatherApp(App):
    pass

#El archivo .kv debe llevar el nombre de la clase pero sin App
WeatherApp().run()