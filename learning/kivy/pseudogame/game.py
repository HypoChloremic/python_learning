from kivy.app import App
from kivy.uix.widget import Widget
# from kivy.graphics import Color, Rectangle
from kivy.core.window import Window



# This is the core of our game code, he says
class Game(Widget):
	pass
	

class GameApp(App):
	# build has to return a widget, which becomes 
	# the top level app. 
	def build(self):
		# size is defaulted to 100 by 100,
		# but now we are setting it to the size of the shit instead
		return Game(size=Window.size)

if __name__ == '__main__':
	GameApp().run()