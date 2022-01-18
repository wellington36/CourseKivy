from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color
from kivy.properties import Clock


class WidgetsExample(GridLayout):
	can_count = BooleanProperty(False)
	count = 0
	my_text = StringProperty("0")
	text_input_str = StringProperty("foo")
	#my_slider_value = StringProperty("0")
	
	def on_button_click(self):
		if self.can_count:
			print("Button clicked")
			self.count += 1
			self.my_text = str(self.count)
	
	def on_toggle_button_state(self, widget):
		print("toggle state: " + widget.state)
		if widget.state == "normal":
			widget.text = "OFF"
			self.can_count = False
		else:
			widget.text = "ON"
			self.can_count = True
	
	def on_switch_active(self, widget):
		print("Switch: " + str(widget.active))
	
	#def on_slider_value(self, widget):
		#print("Slider: " + str(int(widget.value)))
		#self.my_slider_value = str(int(widget.value))

	def on_text_validate(self, widget):
		self.text_input_str = str(widget.text)

# https://kivy.org/doc/stable/gettingstarted/layouts.html
class StackLayoutExample(StackLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		for i in range(0, 100):
			# size = dp(100) + i*10
			size = dp(100)
			b = Button(text=str(i+1), size_hint=(None, None), size=(size, size))
			self.add_widget(b)

#class GridLayoutExample(GridLayout):
#	pass

class AnchorLayoutExample(AnchorLayout):
	pass

class BoxLayoutExample(BoxLayout):
	pass

"""
    def __init__(self, **kwargs):
    	super().__init__(**kwargs)
    	self.orientation = "vertical"
    	b1 = Button(text="A")
    	b2 = Button(text="B")
    	b3 = Button(text="C")
    	self.add_widget(b1)
    	self.add_widget(b2)
    	self.add_widget(b3)
"""

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass


class CanvasExample1(Widget):
	pass

class CanvasExample2(Widget):
	pass

class CanvasExample3(Widget):
	pass

class CanvasExample4(Widget):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		with self.canvas:
			Line(points=(100, 100, 400, 500), width=2)
			Color(0, 1, 0)
			Line(circle=(400, 200, 80), width=2)
			Line(rectangle=(700, 500, 150, 100), width=2)
			self.rect = Rectangle(pos=(700, 200), size=(150, 100))
	
	def on_button_a_click(self):
		x, y = self.rect.pos
		w, h = self.rect.size
		
		inc = dp(10)
		
		diff = self.width - (x + w)
		
		if diff < inc:
			inc = diff
		
		x += inc
		
		self.rect.pos = (x, y)


class CanvasExample5(Widget):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.ball_size = dp(50)
		self.vx = dp(2)
		self.vy = dp(2)

		with self.canvas:
			self.ball = Ellipse(pos=self.center, size=(self.ball_size, self.ball_size))
		Clock.schedule_interval(self.update, 0.01)
	
	def on_size(self, *args):
		#print("on size: " + str(self.width) + ", " + str(self.heigth))
		self.ball.pos = (self.center_x - self.ball_size/2, self.center_y - self.ball_size/2)
		
	def update(self, dt):
		# print("update")
		w, h = self.size
		x, y = self.ball.pos
		
		x += self.vx
		y += self.vy
		
		if y + self.ball_size > self.height:
			y = self.height - self.ball_size
			self.vy = -1 * self.vy
		
		if x + self.ball_size > self.width:
			x = self.width - self.ball_size
			self.vx = -1 * self.vx
		
		if y < 0:
			y = 0
			self.vy = -1 * self.vy
		
		if x < 0:
			x = 0
			self.vx = -1 * self.vx
		
		
		self.ball.pos = (x, y)


class CanvasExample6(Widget):
	pass

class CanvasExample7(BoxLayout):
	pass


TheLabApp().run()




