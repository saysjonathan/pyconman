from ctypes import *
from conman import libconman
from conman.state import *
from conman.resource import Resource

class User(Resource):
	def __init__(self, name, group, homedir, shell, state=present, comment='', passwd='', uid=0):
		self._type = self._gettype()
		self.name = name
		self.state = state
		self.comment = comment
		self.group = group
		self.homedir = homedir
		self.passwd = passwd
		self.shell = shell
		self.uid = uid

	def get(self):
		self.init()
		super(User, self).get()
		self.deinit()

	def set(self):
		self.init()
		self._data.state = self.state
		self._data.comment = cast(self.comment, c_char_p).value
		self._data.group = cast(self.group, c_char_p).value
		self._data.homedir = cast(self.homedir, c_char_p).value
		self._data.passwd = cast(self.passwd, c_char_p).value
		self._data.shell = cast(self.shell, c_char_p).value
		self._data.uid = self.uid
		super(User, self).set()
