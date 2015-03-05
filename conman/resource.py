from ctypes import *
from conman import libconman

class Resource(object):
	def _gettype(self):
		return self.__class__.__name__.lower()

	def get(self):
		get = getattr(getattr(libconman, 'cm'), "cm_{0}_get".format(self._type))
		i = get(cast(self.name, c_char_p), byref(self._data))
		if i < 0:
			raise ValueError("[{0}] {1}: {2}".format(self._type, self.name, i))

	def set(self):
		set = getattr(getattr(libconman, 'cm'), "cm_{0}_set".format(self._type))
		i = set(cast(self.name, c_char_p), byref(self._data))
		if i < 0:
			raise ValueError("[{0}] {1}: {2}".format(self._type, self.name, i))
		
	def init(self):
		data = getattr(libconman, "CM{0}".format(self._type.capitalize()))
		self._data = data()
		init = getattr(getattr(libconman, 'cm'), "cm_{0}_init".format(self._type))
		init(byref(self._data))
		return self

	def deinit(self):
		deinit = getattr(getattr(libconman, 'cm'), "cm_{0}_deinit".format(self._type))
		deinit(byref(self._data))
		
