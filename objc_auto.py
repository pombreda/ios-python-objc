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


BOOL = c_char 


enum_anon_3 = c_int 


OBJC_RATIO_COLLECTION = (0 << 0) 


OBJC_GENERATIONAL_COLLECTION = (1 << 0) 


OBJC_FULL_COLLECTION = (2 << 0) 


OBJC_EXHAUSTIVE_COLLECTION = (3 << 0) 


OBJC_COLLECT_IF_NEEDED = (1 << 3)


OBJC_WAIT_UNTIL_DONE = (1 << 4) 



for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_collect'):
        continue
    objc_collect = _lib.objc_collect
    objc_collect.argtypes = [c_ulong]
    objc_collect.restype = None
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_collectingEnabled'):
        continue
    objc_collectingEnabled = _lib.objc_collectingEnabled
    objc_collectingEnabled.argtypes = []
    objc_collectingEnabled.restype = BOOL
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_setCollectionThreshold'):
        continue
    objc_setCollectionThreshold = _lib.objc_setCollectionThreshold
    objc_setCollectionThreshold.argtypes = [c_size_t]
    objc_setCollectionThreshold.restype = None
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_setCollectionRatio'):
        continue
    objc_setCollectionRatio = _lib.objc_setCollectionRatio
    objc_setCollectionRatio.argtypes = [c_size_t]
    objc_setCollectionRatio.restype = None
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_startCollectorThread'):
        continue
    objc_startCollectorThread = _lib.objc_startCollectorThread
    objc_startCollectorThread.argtypes = []
    objc_startCollectorThread.restype = None
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_atomicCompareAndSwapGlobal'):
        continue
    objc_atomicCompareAndSwapGlobal = _lib.objc_atomicCompareAndSwapGlobal
    objc_atomicCompareAndSwapGlobal.argtypes = [id, id, POINTER(id)]
    objc_atomicCompareAndSwapGlobal.restype = BOOL
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_atomicCompareAndSwapGlobalBarrier'):
        continue
    objc_atomicCompareAndSwapGlobalBarrier = _lib.objc_atomicCompareAndSwapGlobalBarrier
    objc_atomicCompareAndSwapGlobalBarrier.argtypes = [id, id, POINTER(id)]
    objc_atomicCompareAndSwapGlobalBarrier.restype = BOOL
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_atomicCompareAndSwapInstanceVariable'):
        continue
    objc_atomicCompareAndSwapInstanceVariable = _lib.objc_atomicCompareAndSwapInstanceVariable
    objc_atomicCompareAndSwapInstanceVariable.argtypes = [id, id, POINTER(id)]
    objc_atomicCompareAndSwapInstanceVariable.restype = BOOL
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_atomicCompareAndSwapInstanceVariableBarrier'):
        continue
    objc_atomicCompareAndSwapInstanceVariableBarrier = _lib.objc_atomicCompareAndSwapInstanceVariableBarrier
    objc_atomicCompareAndSwapInstanceVariableBarrier.argtypes = [id, id, POINTER(id)]
    objc_atomicCompareAndSwapInstanceVariableBarrier.restype = BOOL
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_assign_strongCast'):
        continue
    objc_assign_strongCast = _lib.objc_assign_strongCast
    objc_assign_strongCast.argtypes = [id, POINTER(id)]
    objc_assign_strongCast.restype = id
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_assign_global'):
        continue
    objc_assign_global = _lib.objc_assign_global
    objc_assign_global.argtypes = [id, POINTER(id)]
    objc_assign_global.restype = id
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_assign_ivar'):
        continue
    objc_assign_ivar = _lib.objc_assign_ivar
    objc_assign_ivar.argtypes = [id, id, c_ptrdiff_t]
    objc_assign_ivar.restype = id
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_memmove_collectable'):
        continue
    objc_memmove_collectable = _lib.objc_memmove_collectable
    objc_memmove_collectable.argtypes = [POINTER(None), POINTER(None), c_size_t]
    objc_memmove_collectable.restype = POINTER(None)
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_read_weak'):
        continue
    objc_read_weak = _lib.objc_read_weak
    objc_read_weak.argtypes = [POINTER(id)]
    objc_read_weak.restype = id
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_assign_weak'):
        continue
    objc_assign_weak = _lib.objc_assign_weak
    objc_assign_weak.argtypes = [id, POINTER(id)]
    objc_assign_weak.restype = id
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_finalizeOnMainThread'):
        continue
    objc_finalizeOnMainThread = _lib.objc_finalizeOnMainThread
    objc_finalizeOnMainThread.argtypes = [Class]
    objc_finalizeOnMainThread.restype = None
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_is_finalized'):
        continue
    objc_is_finalized = _lib.objc_is_finalized
    objc_is_finalized.argtypes = [POINTER(None)]
    objc_is_finalized.restype = BOOL
    break

enum_anon_4 = c_int 


OBJC_CLEAR_RESIDENT_STACK = (1 << 0) 



for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_clear_stack'):
        continue
    objc_clear_stack = _lib.objc_clear_stack
    objc_clear_stack.argtypes = [c_ulong]
    objc_clear_stack.restype = None
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_collecting_enabled'):
        continue
    objc_collecting_enabled = _lib.objc_collecting_enabled
    objc_collecting_enabled.argtypes = []
    objc_collecting_enabled.restype = BOOL
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_start_collector_thread'):
        continue
    objc_start_collector_thread = _lib.objc_start_collector_thread
    objc_start_collector_thread.argtypes = []
    objc_start_collector_thread.restype = None
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_allocate_object'):
        continue
    objc_allocate_object = _lib.objc_allocate_object
    objc_allocate_object.argtypes = [Class, c_int]
    objc_allocate_object.restype = id
    break

enum_anon_5 = c_int 


OBJC_GENERATIONAL = (1 << 0) 



for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_collect_if_needed'):
        continue
    objc_collect_if_needed = _lib.objc_collect_if_needed
    objc_collect_if_needed.argtypes = [c_ulong]
    objc_collect_if_needed.restype = None
    break


try:
    OBJC_NO_GC = 1
except:
    pass