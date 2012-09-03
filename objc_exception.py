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



if hasattr(_libs['objc'], 'objc_exception_throw'):
    objc_exception_throw = _libs['objc'].objc_exception_throw
    objc_exception_throw.argtypes = [id]
    objc_exception_throw.restype = None


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_exception_try_enter'):
        continue
    objc_exception_try_enter = _lib.objc_exception_try_enter
    objc_exception_try_enter.argtypes = [POINTER(None)]
    objc_exception_try_enter.restype = None
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_exception_try_exit'):
        continue
    objc_exception_try_exit = _lib.objc_exception_try_exit
    objc_exception_try_exit.argtypes = [POINTER(None)]
    objc_exception_try_exit.restype = None
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_exception_extract'):
        continue
    objc_exception_extract = _lib.objc_exception_extract
    objc_exception_extract.argtypes = [POINTER(None)]
    objc_exception_extract.restype = id
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_exception_match'):
        continue
    objc_exception_match = _lib.objc_exception_match
    objc_exception_match.argtypes = [Class, id]
    objc_exception_match.restype = c_int
    break


class struct_anon_2(Structure):
    pass

struct_anon_2.__slots__ = [
    'version',
    'throw_exc',
    'try_enter',
    'try_exit',
    'extract',
    'match',
]
struct_anon_2._fields_ = [
    ('version', c_int),
    ('throw_exc', CFUNCTYPE(UNCHECKED(None), id)),
    ('try_enter', CFUNCTYPE(UNCHECKED(None), POINTER(None))),
    ('try_exit', CFUNCTYPE(UNCHECKED(None), POINTER(None))),
    ('extract', CFUNCTYPE(UNCHECKED(id), POINTER(None))),
    ('match', CFUNCTYPE(UNCHECKED(c_int), Class, id)),
]

objc_exception_functions_t = struct_anon_2 



for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_exception_get_functions'):
        continue
    objc_exception_get_functions = _lib.objc_exception_get_functions
    objc_exception_get_functions.argtypes = [POINTER(objc_exception_functions_t)]
    objc_exception_get_functions.restype = None
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_exception_set_functions'):
        continue
    objc_exception_set_functions = _lib.objc_exception_set_functions
    objc_exception_set_functions.argtypes = [POINTER(objc_exception_functions_t)]
    objc_exception_set_functions.restype = None
    break