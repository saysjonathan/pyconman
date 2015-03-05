from ctypes import *

class CMFile(Structure):
	_fields_ = [
		('state', c_int),
		('owner', c_char_p),
		('group', c_char_p),
		('mode', c_char_p),
		('source', c_char_p),
		('hash', c_char_p)
	]

cm = CDLL('/usr/local/lib/libconman.so')

cm.cm_strerror.argtypes = [c_int]
cm.cm_strerror.restypes = [c_char_p]

cm.cm_file_init.argtypes = [POINTER(CMFile)]
cm.cm_file_init.restypes = [c_int]
cm.cm_file_get.argtypes = [c_char_p, POINTER(CMFile)]
cm.cm_file_get.restypes = [c_int]
cm.cm_file_set.argtypes = [c_char_p, POINTER(CMFile)]
cm.cm_file_set.restypes = [c_int]
