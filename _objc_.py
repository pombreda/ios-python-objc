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


class struct_objc_selector(Structure):
    pass

SEL = POINTER(struct_objc_selector) 


IMP = CFUNCTYPE(UNCHECKED(id), id, SEL) 


BOOL = c_char 



if hasattr(_libs['objc'], 'sel_getName'):
    sel_getName = _libs['objc'].sel_getName
    sel_getName.argtypes = [SEL]
    if sizeof(c_int) == sizeof(c_void_p):
        sel_getName.restype = ReturnString
    else:
        sel_getName.restype = String
        sel_getName.errcheck = ReturnString


if hasattr(_libs['objc'], 'sel_registerName'):
    sel_registerName = _libs['objc'].sel_registerName
    sel_registerName.argtypes = [String]
    sel_registerName.restype = SEL


if hasattr(_libs['objc'], 'object_getClassName'):
    object_getClassName = _libs['objc'].object_getClassName
    object_getClassName.argtypes = [id]
    if sizeof(c_int) == sizeof(c_void_p):
        object_getClassName.restype = ReturnString
    else:
        object_getClassName.restype = String
        object_getClassName.errcheck = ReturnString


if hasattr(_libs['objc'], 'object_getIndexedIvars'):
    object_getIndexedIvars = _libs['objc'].object_getIndexedIvars
    object_getIndexedIvars.argtypes = [id]
    object_getIndexedIvars.restype = POINTER(None)

arith_t = c_int 


uarith_t = c_uint 



if hasattr(_libs['objc'], 'sel_isMapped'):
    sel_isMapped = _libs['objc'].sel_isMapped
    sel_isMapped.argtypes = [SEL]
    sel_isMapped.restype = BOOL


if hasattr(_libs['objc'], 'sel_getUid'):
    sel_getUid = _libs['objc'].sel_getUid
    sel_getUid.argtypes = [String]
    sel_getUid.restype = SEL

STR = String 



try:
    __DARWIN_NULL = None
except:
    pass


try:
    YES = 1
except:
    pass


try:
    NO = 0
except:
    pass


try:
    Nil = __DARWIN_NULL
except:
    pass


try:
    nil = __DARWIN_NULL
except:
    pass


try:
    ARITH_SHIFT = 16
except:
    pass


def ISSELECTOR(sel):
    return (sel_isMapped (sel))


def SELNAME(sel):
    return (sel_getName (sel))


def SELUID(str):
    return (sel_getUid (str))


def NAMEOF(obj):
    return (object_getClassName (obj))


def IV(obj):
    return (object_getIndexedIvars (obj))

objc_class = struct_objc_class 


objc_object = struct_objc_object 


objc_selector = struct_objc_selector 