from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
from kivy.uix.listview import ListItemButton
from kivy.factory import Factory # This seemingly allows us to access dynamic classes we constructed inside the kivy file. 
import json

class WeatherApp(App):
	pass

class WeatherRoot(BoxLayout):
	def show_current_weather(self, location):
		self.clear_widgets() # This will remove the current window, or widget
		# self.add_widget(Label(text=location)) # This will replace the now empty windows with a new widget, containing a label
		current_weather = Factory.CurrentWeather() # We are accessing the dynamic class inside the kivy file. 
		current_weather.location = location
		self.add_widget(current_weather)
	
	def add_location_form(self):
		self.clear_widgets()
		self.add_widget(AddLocationForm())

class AddLocationForm(BoxLayout):
	"""docstring for AddLocationForm; It seems that 
	if we do <AddLocationForm@BoxLayout>: insinde the 
	kv file, is the same as this class definition"""
	search_input = ObjectProperty()
	current_weather = ObjectProperty() # We are going to store an entire widget in here. 

	def search_location(self):
		# it seems that the search_input thing wants to be referenced with self before. 
		# I assume because we r referencing to the original root class etc.  
		search_template = "http://api.openweathermap.org/data/2.5/find?q={}&type=like"
		search_url = search_template.format(self.search_input.text)
		# request = UrlRequest(url = search_url, method = self.found_location(), debug=True)
		self.found_location()

	def found_location(self):
		
		# data = json.loads(data.decode()) if not isinstance(datam, dict) else data
		# cities = [ "{} ({})".format(d["name"], d["sys"]["country"]) for d in data["list"]]
		cities = [ "Palo Alto", "Vancouver", "Stockholm" ]
		
		"""Here we are defining something from the inside of the kivy file to
		inside the python script file. Prior to this, weäve been pulling data from the kivy environment."""
		# self.search_results.item_strings = cities
		self.search_results.adapter.data.clear()
		self.search_results.adapter.data.extend(cities)
		self.search_results.item_strings = cities

	def input_text(self):
		print(self.text_enter.text)

	def show_current_weather(self, location=None):
		self.clear_widgets()

		if location is None and self.current_weather is None:
			location = "New York"
			
		if location is not None:
			self.current_weather = Factory.CurrentWeather()
			self.current_weather.location = location

		self.add_widget(self.current_weather)



class LocationButton(ListItemButton):
	pass

if __name__ == '__main__':
	WeatherApp().run()