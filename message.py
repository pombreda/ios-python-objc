from dialogue import *
from dialogue.typedefs import _variadic_function
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



class struct_objc_selector(Structure):
    pass

SEL = POINTER(struct_objc_selector) 


IMP = CFUNCTYPE(UNCHECKED(id), id, SEL) 



class struct_objc_method(Structure):
    pass

Method = POINTER(struct_objc_method) 



class struct_objc_ivar(Structure):
    pass


class struct_objc_ivar_list(Structure):
    pass


class struct_objc_method_list(Structure):
    pass


class struct_objc_cache(Structure):
    pass


class struct_objc_protocol_list(Structure):
    pass

struct_objc_class.__slots__ = [
    'isa',
    'super_class',
    'name',
    'version',
    'info',
    'instance_size',
    'ivars',
    'methodLists',
    'cache',
    'protocols',
]
struct_objc_class._fields_ = [
    ('isa', Class),
    ('super_class', Class),
    ('name', String),
    ('version', c_long),
    ('info', c_long),
    ('instance_size', c_long),
    ('ivars', POINTER(struct_objc_ivar_list)),
    ('methodLists', POINTER(POINTER(struct_objc_method_list))),
    ('cache', POINTER(struct_objc_cache)),
    ('protocols', POINTER(struct_objc_protocol_list)),
]

Protocol = struct_objc_object 


struct_objc_protocol_list.__slots__ = [
    'next',
    'count',
    'list',
]
struct_objc_protocol_list._fields_ = [
    ('next', POINTER(struct_objc_protocol_list)),
    ('count', c_long),
    ('list', POINTER(Protocol) * 1),
]

struct_objc_ivar.__slots__ = [
    'ivar_name',
    'ivar_type',
    'ivar_offset',
]
struct_objc_ivar._fields_ = [
    ('ivar_name', String),
    ('ivar_type', String),
    ('ivar_offset', c_int),
]

struct_objc_ivar_list.__slots__ = [
    'ivar_count',
    'ivar_list',
]
struct_objc_ivar_list._fields_ = [
    ('ivar_count', c_int),
    ('ivar_list', struct_objc_ivar * 1),
]

struct_objc_method.__slots__ = [
    'method_name',
    'method_types',
    'method_imp',
]
struct_objc_method._fields_ = [
    ('method_name', SEL),
    ('method_types', String),
    ('method_imp', IMP),
]

struct_objc_method_list.__slots__ = [
    'obsolete',
    'method_count',
    'method_list',
]
struct_objc_method_list._fields_ = [
    ('obsolete', POINTER(struct_objc_method_list)),
    ('method_count', c_int),
    ('method_list', struct_objc_method * 1),
]

struct_objc_cache.__slots__ = [
    'mask',
    'occupied',
    'buckets',
]
struct_objc_cache._fields_ = [
    ('mask', c_uint),
    ('occupied', c_uint),
    ('buckets', Method * 1),
]


class struct_objc_super(Structure):
    pass

struct_objc_super.__slots__ = [
    'receiver',
    '_class',
]
struct_objc_super._fields_ = [
    ('receiver', id),
    ('_class', Class),
]


if hasattr(_libs['objc'], 'objc_msgSend'):
    _func = _libs['objc'].objc_msgSend
    _restype = id
    _argtypes = [id, SEL]
    objc_msgSend = _variadic_function(_func,_restype,_argtypes)


if hasattr(_libs['objc'], 'objc_msgSendSuper'):
    _func = _libs['objc'].objc_msgSendSuper
    _restype = id
    _argtypes = [POINTER(struct_objc_super), SEL]
    objc_msgSendSuper = _variadic_function(_func,_restype,_argtypes)


if hasattr(_libs['objc'], 'objc_msgSend_stret'):
    _func = _libs['objc'].objc_msgSend_stret
    _restype = None
    _argtypes = [POINTER(None), id, SEL]
    objc_msgSend_stret = _variadic_function(_func,_restype,_argtypes)


if hasattr(_libs['objc'], 'objc_msgSendSuper_stret'):
    _func = _libs['objc'].objc_msgSendSuper_stret
    _restype = None
    _argtypes = [POINTER(None), POINTER(struct_objc_super), SEL]
    objc_msgSendSuper_stret = _variadic_function(_func,_restype,_argtypes)


if hasattr(_libs['objc'], 'method_invoke'):
    _func = _libs['objc'].method_invoke
    _restype = id
    _argtypes = [id, Method]
    method_invoke = _variadic_function(_func,_restype,_argtypes)


if hasattr(_libs['objc'], 'method_invoke_stret'):
    _func = _libs['objc'].method_invoke_stret
    _restype = None
    _argtypes = [id, Method]
    method_invoke_stret = _variadic_function(_func,_restype,_argtypes)

marg_list = POINTER(None) 



for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_msgSendv'):
        continue
    objc_msgSendv = _lib.objc_msgSendv
    objc_msgSendv.argtypes = [id, SEL, c_size_t, marg_list]
    objc_msgSendv.restype = id
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_msgSendv_stret'):
        continue
    objc_msgSendv_stret = _lib.objc_msgSendv_stret
    objc_msgSendv_stret.argtypes = [POINTER(None), id, SEL, c_size_t, marg_list]
    objc_msgSendv_stret.restype = None
    break


try:
    marg_prearg_size = 0
except:
    pass


def marg_adjustedOffset(method, offset):
    return (marg_prearg_size + offset)


def marg_setValue(margs, offset, type, value):
    return value

objc_super = struct_objc_super 