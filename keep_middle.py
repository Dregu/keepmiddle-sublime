"""
# KeepMiddle Sublime Text 3 plugin

Always keeps the current line in the middle of the screen for context and focus.
Requires package MouseEventListener to fix selecting text with mouse.
"""

import sublime, sublime_plugin, pprint
from functools import reduce
try:
	import mouse_event_listener
except:
	pass

class KeepMiddle(sublime_plugin.EventListener):
	isDisabled = False
	counter = 0
	def on_pre_mouse_down(self, view):
		self.isDisabled = True
		self.counter = 3
	def on_selection_modified(self, view):
		pprint.pprint([self.counter, self.isDisabled])
		self.counter -= 1
		if(view.sel()[0].a == view.sel()[0].b and self.counter <= 0):
			self.isDisabled = False
			self.counter = 0
		if(self.isDisabled):
			return
		if(self.counter <= 0):
			view.show_at_center(view.sel()[0])
