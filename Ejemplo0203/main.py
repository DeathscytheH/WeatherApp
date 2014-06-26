""" 
Ejemplo 2-3. Agregando logica muy simple
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class AddLocationForm(BoxLayout):
    def search_location(self):
        print "Explicito es mejor que implicito"
        

class WeatherApp(App):
    pass

#El archivo .kv debe llevar el nombre de la clase pero sin App
WeatherApp().run()