from ctypes import *
from conman import libconman
from conman.resource import Resource

class Dir(Resource):
	def __init__(self, path, state=0, owner='', group='', mode='', recurse=0):
		self._type = self._gettype()
		self.name = path
		self.state = state
		self.owner = owner
		self.group = group
		self.mode = mode
		self.recurse = recurse

	def get(self):
		self.init()
		super(Dir, self).get()
		self.deinit()

	def set(self):
		self.init()
		self._data.state = self.state
		self._data.owner = cast(self.owner, c_char_p).value
		self._data.group = cast(self.group, c_char_p).value
		self._data.mode = cast(self.mode, c_char_p).value
		self._data.recurse = self.recurse
		super(Dir, self).set()
