from ctypes import *
from conman import libconman
from conman.resource import Resource

class File(Resource):
	def __init__(self, path):
		self.name = path
		super(File, self).__init__()

	def get(self):
		self.init()
		super(File, self).get()
		self.deinit()

	def set(self, state=0, owner="", group="", mode="", source=""):
		self.init()
		self._data.state = state
		self._data.owner = cast(owner, c_char_p).value
		self._data.group = cast(group, c_char_p).value
		self._data.mode = cast(mode, c_char_p).value
		self._data.source = cast(source, c_char_p).value
		super(File, self).set()
