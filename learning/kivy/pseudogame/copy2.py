from kivy.app import App
from kivy.uix.widget import Widget
# from kivy.graphics import Color, Rectangle
from kivy.core.window import Window



# This is the core of our game code, he says
class Game(Widget):
	# The remaining shit is going to be read from the 
	# .kv file, in that order. 
	pass

class GameApp(App):
	def build(self):
		# size is defaulted to 100 by 100,
		# but now we are setting it to the size of the shit instead
		return Game(size=Window.size)

if __name__ == '__main__':
	GameApp().run()