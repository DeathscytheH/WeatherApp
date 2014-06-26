""" 
Ejemplo 2-8. Recuperando info de los mapas utilizando request e 
imprimiendo la lista de las ciudades en la consola
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
import json

class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()
    def search_location(self):
        search_template="http://api.openweathermap.org/data/2.5/" + "find?q={}&type=like"
        search_url=search_template.format(self.search_input.text)
        request=UrlRequest(search_url, self.found_location)

    def found_location(self, request, data):
        data=json.loads(data.decode()) if not isinstance(data, dict) else data
        cities = ["{} ({})".format(d['name'],d['sys']['country']) 
            for d in data['list']]
        #print "\n".join(cities)
        self.search_results.item_strings = cities

class WeatherApp(App):
    pass

#El archivo .kv debe llevar el nombre de la clase pero sin App
WeatherApp().run()