from dialogue import *
_libs = {}
_libdirs = []

_libs["objc"] = load_library("objc")

class struct_objc_class(Structure):
    pass

Class = POINTER(struct_objc_class) 



class struct_objc_object(Structure):
    pass

struct_objc_object.__slots__ = [
    'isa',
]
struct_objc_object._fields_ = [
    ('isa', Class),
]

id = POINTER(struct_objc_object) 



if hasattr(_libs['objc'], 'objc_sync_enter'):
    objc_sync_enter = _libs['objc'].objc_sync_enter
    objc_sync_enter.argtypes = [id]
    objc_sync_enter.restype = c_int


if hasattr(_libs['objc'], 'objc_sync_exit'):
    objc_sync_exit = _libs['objc'].objc_sync_exit
    objc_sync_exit.argtypes = [id]
    objc_sync_exit.restype = c_int


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_sync_wait'):
        continue
    objc_sync_wait = _lib.objc_sync_wait
    objc_sync_wait.argtypes = [id, c_longlong]
    objc_sync_wait.restype = c_int
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_sync_notify'):
        continue
    objc_sync_notify = _lib.objc_sync_notify
    objc_sync_notify.argtypes = [id]
    objc_sync_notify.restype = c_int
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_sync_notifyAll'):
        continue
    objc_sync_notifyAll = _lib.objc_sync_notifyAll
    objc_sync_notifyAll.argtypes = [id]
    objc_sync_notifyAll.restype = c_int
    break

enum_anon_2 = c_int 


OBJC_SYNC_SUCCESS = 0 


OBJC_SYNC_NOT_OWNING_THREAD_ERROR = (-1) 


OBJC_SYNC_TIMED_OUT = (-2) 


OBJC_SYNC_NOT_INITIALIZED = (-3) 