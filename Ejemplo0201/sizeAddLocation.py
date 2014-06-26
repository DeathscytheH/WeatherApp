""" 
Agregar algo de logica a la vista.

De la vista se retiro el @boxlayout para integrarlo en el .py

"""
from kivy.app import App       

class sizeAddLocationApp(App):
    pass

#El archivo .kv debe llevar el nombre de la clase pero sin App
sizeAddLocationApp().run()