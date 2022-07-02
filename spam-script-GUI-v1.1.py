from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
import pyautogui as pg
import sys
import time

class spam:
	def __init__(self):
		pass
	def start_spam(self):
		while True:
			pg.write("spam")
			pg.press("enter")
	def stop_spam(self):
		sys.exit()
	def exit_spam(self):
		print("Spegnendo il programma...")
		time.sleep(1.5)
		sys.exit()

class LayoutClass(BoxLayout):
	def __init__(self, **kwargs):
		super(LayoutClass, self).__init__(**kwargs)
		list = [10, 10]
		self.orientation = "vertical"
		label = Label(text = "Spam App", color="magenta", font_size=65, font_family = "Dejavu Sans", bold = True)
		self.add_widget(label)
		var_spam = spam()
		button = Button(text="Start spam", font_size = 50, font_family = "Dejavu Sans", bold = False, color = "white", background_color = "purple")
		button2 = Button(text="Stop spam", font_size = 50, font_family = "Dejavu Sans", bold = False, color = "white", background_color = "purple")
		button3 = Button(text="Exit", font_size = 50, font_family = "Dejavu Sans", bold = False, color = "red", background_color = "magenta")
		button2.bind(on_press = lambda a : var_spam.stop_spam())
		button.bind(on_press = lambda a : var_spam.start_spam())
		button3.bind(on_press = lambda a : var_spam.exit_spam())
		self.add_widget(button)
		self.add_widget(button2)
		self.add_widget(button3)

class SpamAppApp(App):
	def build(self):
		return LayoutClass()
SpamAppApp().run()
