from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window



# This is the core of our game code, he says
class Game(Widget):
	def __init__(self, **kwargs):
		# This is important, such that the underlying
		# widget shit is called. 
		super(Game, self).__init__(**kwargs)
		# Canvas are a series of instructions run in sequence
		with self.canvas:
			# Now this sets the color for the rest of the shit that follows
			# The coordinate system of kivy starts from origin in the bottom left corner
			# Color is in r,g,b, and they are scaled in bright to dark. 
			# It doesnt use 0-255, so we have to map that shit down.
			Color(.5,.5,1.0)
			# The rectangle will use this color now
			Rectangle(pos=(1,0), size=self.size)



class GameApp(App):
	def build(self):
		# size is defaulted to 100 by 100,
		# but now we are setting it to the size of the shit instead
		return Game(size=Window.size)

if __name__ == '__main__':
	GameApp().run()