from ctypes import *
from conman import libconman
from conman.state import *
from conman.resource import Resource

class Group(Resource):
	def __init__(self, name, state=present, gid=0):
		self._type = self._gettype()
		self.name = name
		self.state = state
		self.gid = gid

	def get(self):
		self.init()
		super(Group, self).get()
		self.deinit()

	def set(self):
		self.init()
		self._data.state = self.state
		self._data.gid = self.gid
		super(Group, self).set()
