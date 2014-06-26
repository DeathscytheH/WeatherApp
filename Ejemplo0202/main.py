""" 
Agregar algo de logica a la vista.

De la vista se retiro el @boxlayout para integrarlo en el .py

"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class AddLocationForm(BoxLayout):
    pass
        

class WeatherApp(App):
    pass

#El archivo .kv debe llevar el nombre de la clase pero sin App
WeatherApp().run()