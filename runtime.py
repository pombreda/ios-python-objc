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



class struct_objc_method(Structure):
    pass

Method = POINTER(struct_objc_method) 



class struct_objc_ivar(Structure):
    pass

Ivar = POINTER(struct_objc_ivar) 



class struct_objc_category(Structure):
    pass

Category = POINTER(struct_objc_category) 



class struct_objc_property(Structure):
    pass

objc_property_t = POINTER(struct_objc_property) 



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



class struct_objc_method_description(Structure):
    pass

struct_objc_method_description.__slots__ = [
    'name',
    'types',
]
struct_objc_method_description._fields_ = [
    ('name', SEL),
    ('types', String),
]


class struct_objc_method_description_list(Structure):
    pass

struct_objc_method_description_list.__slots__ = [
    'count',
    'list',
]
struct_objc_method_description_list._fields_ = [
    ('count', c_int),
    ('list', struct_objc_method_description * 1),
]

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


if hasattr(_libs['objc'], 'object_copy'):
    object_copy = _libs['objc'].object_copy
    object_copy.argtypes = [id, c_size_t]
    object_copy.restype = id


if hasattr(_libs['objc'], 'object_dispose'):
    object_dispose = _libs['objc'].object_dispose
    object_dispose.argtypes = [id]
    object_dispose.restype = id


if hasattr(_libs['objc'], 'object_getClass'):
    object_getClass = _libs['objc'].object_getClass
    object_getClass.argtypes = [id]
    object_getClass.restype = Class


if hasattr(_libs['objc'], 'object_setClass'):
    object_setClass = _libs['objc'].object_setClass
    object_setClass.argtypes = [id, Class]
    object_setClass.restype = Class


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


if hasattr(_libs['objc'], 'object_getIvar'):
    object_getIvar = _libs['objc'].object_getIvar
    object_getIvar.argtypes = [id, Ivar]
    object_getIvar.restype = id


if hasattr(_libs['objc'], 'object_setIvar'):
    object_setIvar = _libs['objc'].object_setIvar
    object_setIvar.argtypes = [id, Ivar, id]
    object_setIvar.restype = None


if hasattr(_libs['objc'], 'object_setInstanceVariable'):
    object_setInstanceVariable = _libs['objc'].object_setInstanceVariable
    object_setInstanceVariable.argtypes = [id, String, POINTER(None)]
    object_setInstanceVariable.restype = Ivar


if hasattr(_libs['objc'], 'object_getInstanceVariable'):
    object_getInstanceVariable = _libs['objc'].object_getInstanceVariable
    object_getInstanceVariable.argtypes = [id, String, POINTER(POINTER(None))]
    object_getInstanceVariable.restype = Ivar


if hasattr(_libs['objc'], 'objc_getClass'):
    objc_getClass = _libs['objc'].objc_getClass
    objc_getClass.argtypes = [String]
    objc_getClass.restype = id


if hasattr(_libs['objc'], 'objc_getMetaClass'):
    objc_getMetaClass = _libs['objc'].objc_getMetaClass
    objc_getMetaClass.argtypes = [String]
    objc_getMetaClass.restype = id


if hasattr(_libs['objc'], 'objc_lookUpClass'):
    objc_lookUpClass = _libs['objc'].objc_lookUpClass
    objc_lookUpClass.argtypes = [String]
    objc_lookUpClass.restype = id


if hasattr(_libs['objc'], 'objc_getRequiredClass'):
    objc_getRequiredClass = _libs['objc'].objc_getRequiredClass
    objc_getRequiredClass.argtypes = [String]
    objc_getRequiredClass.restype = id


if hasattr(_libs['objc'], 'objc_getFutureClass'):
    objc_getFutureClass = _libs['objc'].objc_getFutureClass
    objc_getFutureClass.argtypes = [String]
    objc_getFutureClass.restype = Class


if hasattr(_libs['objc'], 'objc_setFutureClass'):
    objc_setFutureClass = _libs['objc'].objc_setFutureClass
    objc_setFutureClass.argtypes = [Class, String]
    objc_setFutureClass.restype = None


if hasattr(_libs['objc'], 'objc_getClassList'):
    objc_getClassList = _libs['objc'].objc_getClassList
    objc_getClassList.argtypes = [POINTER(Class), c_int]
    objc_getClassList.restype = c_int


if hasattr(_libs['objc'], 'objc_getProtocol'):
    objc_getProtocol = _libs['objc'].objc_getProtocol
    objc_getProtocol.argtypes = [String]
    objc_getProtocol.restype = POINTER(Protocol)


if hasattr(_libs['objc'], 'objc_copyProtocolList'):
    objc_copyProtocolList = _libs['objc'].objc_copyProtocolList
    objc_copyProtocolList.argtypes = [POINTER(c_uint)]
    objc_copyProtocolList.restype = POINTER(POINTER(Protocol))


if hasattr(_libs['objc'], 'class_getName'):
    class_getName = _libs['objc'].class_getName
    class_getName.argtypes = [Class]
    if sizeof(c_int) == sizeof(c_void_p):
        class_getName.restype = ReturnString
    else:
        class_getName.restype = String
        class_getName.errcheck = ReturnString


if hasattr(_libs['objc'], 'class_isMetaClass'):
    class_isMetaClass = _libs['objc'].class_isMetaClass
    class_isMetaClass.argtypes = [Class]
    class_isMetaClass.restype = BOOL


if hasattr(_libs['objc'], 'class_getSuperclass'):
    class_getSuperclass = _libs['objc'].class_getSuperclass
    class_getSuperclass.argtypes = [Class]
    class_getSuperclass.restype = Class


if hasattr(_libs['objc'], 'class_setSuperclass'):
    class_setSuperclass = _libs['objc'].class_setSuperclass
    class_setSuperclass.argtypes = [Class, Class]
    class_setSuperclass.restype = Class


if hasattr(_libs['objc'], 'class_getVersion'):
    class_getVersion = _libs['objc'].class_getVersion
    class_getVersion.argtypes = [Class]
    class_getVersion.restype = c_int


if hasattr(_libs['objc'], 'class_setVersion'):
    class_setVersion = _libs['objc'].class_setVersion
    class_setVersion.argtypes = [Class, c_int]
    class_setVersion.restype = None


if hasattr(_libs['objc'], 'class_getInstanceSize'):
    class_getInstanceSize = _libs['objc'].class_getInstanceSize
    class_getInstanceSize.argtypes = [Class]
    class_getInstanceSize.restype = c_size_t


if hasattr(_libs['objc'], 'class_getInstanceVariable'):
    class_getInstanceVariable = _libs['objc'].class_getInstanceVariable
    class_getInstanceVariable.argtypes = [Class, String]
    class_getInstanceVariable.restype = Ivar


if hasattr(_libs['objc'], 'class_getClassVariable'):
    class_getClassVariable = _libs['objc'].class_getClassVariable
    class_getClassVariable.argtypes = [Class, String]
    class_getClassVariable.restype = Ivar


if hasattr(_libs['objc'], 'class_copyIvarList'):
    class_copyIvarList = _libs['objc'].class_copyIvarList
    class_copyIvarList.argtypes = [Class, POINTER(c_uint)]
    class_copyIvarList.restype = POINTER(Ivar)


if hasattr(_libs['objc'], 'class_getInstanceMethod'):
    class_getInstanceMethod = _libs['objc'].class_getInstanceMethod
    class_getInstanceMethod.argtypes = [Class, SEL]
    class_getInstanceMethod.restype = Method


if hasattr(_libs['objc'], 'class_getClassMethod'):
    class_getClassMethod = _libs['objc'].class_getClassMethod
    class_getClassMethod.argtypes = [Class, SEL]
    class_getClassMethod.restype = Method


if hasattr(_libs['objc'], 'class_getMethodImplementation'):
    class_getMethodImplementation = _libs['objc'].class_getMethodImplementation
    class_getMethodImplementation.argtypes = [Class, SEL]
    class_getMethodImplementation.restype = IMP


if hasattr(_libs['objc'], 'class_getMethodImplementation_stret'):
    class_getMethodImplementation_stret = _libs['objc'].class_getMethodImplementation_stret
    class_getMethodImplementation_stret.argtypes = [Class, SEL]
    class_getMethodImplementation_stret.restype = IMP


if hasattr(_libs['objc'], 'class_respondsToSelector'):
    class_respondsToSelector = _libs['objc'].class_respondsToSelector
    class_respondsToSelector.argtypes = [Class, SEL]
    class_respondsToSelector.restype = BOOL


if hasattr(_libs['objc'], 'class_copyMethodList'):
    class_copyMethodList = _libs['objc'].class_copyMethodList
    class_copyMethodList.argtypes = [Class, POINTER(c_uint)]
    class_copyMethodList.restype = POINTER(Method)


if hasattr(_libs['objc'], 'class_conformsToProtocol'):
    class_conformsToProtocol = _libs['objc'].class_conformsToProtocol
    class_conformsToProtocol.argtypes = [Class, POINTER(Protocol)]
    class_conformsToProtocol.restype = BOOL


if hasattr(_libs['objc'], 'class_copyProtocolList'):
    class_copyProtocolList = _libs['objc'].class_copyProtocolList
    class_copyProtocolList.argtypes = [Class, POINTER(c_uint)]
    class_copyProtocolList.restype = POINTER(POINTER(Protocol))


if hasattr(_libs['objc'], 'class_getProperty'):
    class_getProperty = _libs['objc'].class_getProperty
    class_getProperty.argtypes = [Class, String]
    class_getProperty.restype = objc_property_t


if hasattr(_libs['objc'], 'class_copyPropertyList'):
    class_copyPropertyList = _libs['objc'].class_copyPropertyList
    class_copyPropertyList.argtypes = [Class, POINTER(c_uint)]
    class_copyPropertyList.restype = POINTER(objc_property_t)


if hasattr(_libs['objc'], 'class_getIvarLayout'):
    class_getIvarLayout = _libs['objc'].class_getIvarLayout
    class_getIvarLayout.argtypes = [Class]
    if sizeof(c_int) == sizeof(c_void_p):
        class_getIvarLayout.restype = ReturnString
    else:
        class_getIvarLayout.restype = String
        class_getIvarLayout.errcheck = ReturnString


if hasattr(_libs['objc'], 'class_getWeakIvarLayout'):
    class_getWeakIvarLayout = _libs['objc'].class_getWeakIvarLayout
    class_getWeakIvarLayout.argtypes = [Class]
    if sizeof(c_int) == sizeof(c_void_p):
        class_getWeakIvarLayout.restype = ReturnString
    else:
        class_getWeakIvarLayout.restype = String
        class_getWeakIvarLayout.errcheck = ReturnString


if hasattr(_libs['objc'], 'class_createInstance'):
    class_createInstance = _libs['objc'].class_createInstance
    class_createInstance.argtypes = [Class, c_size_t]
    class_createInstance.restype = id


if hasattr(_libs['objc'], 'objc_allocateClassPair'):
    objc_allocateClassPair = _libs['objc'].objc_allocateClassPair
    objc_allocateClassPair.argtypes = [Class, String, c_size_t]
    objc_allocateClassPair.restype = Class


if hasattr(_libs['objc'], 'objc_registerClassPair'):
    objc_registerClassPair = _libs['objc'].objc_registerClassPair
    objc_registerClassPair.argtypes = [Class]
    objc_registerClassPair.restype = None


if hasattr(_libs['objc'], 'objc_duplicateClass'):
    objc_duplicateClass = _libs['objc'].objc_duplicateClass
    objc_duplicateClass.argtypes = [Class, String, c_size_t]
    objc_duplicateClass.restype = Class


if hasattr(_libs['objc'], 'objc_disposeClassPair'):
    objc_disposeClassPair = _libs['objc'].objc_disposeClassPair
    objc_disposeClassPair.argtypes = [Class]
    objc_disposeClassPair.restype = None


if hasattr(_libs['objc'], 'class_addMethod'):
    class_addMethod = _libs['objc'].class_addMethod
    class_addMethod.argtypes = [Class, SEL, IMP, String]
    class_addMethod.restype = BOOL


if hasattr(_libs['objc'], 'class_replaceMethod'):
    class_replaceMethod = _libs['objc'].class_replaceMethod
    class_replaceMethod.argtypes = [Class, SEL, IMP, String]
    class_replaceMethod.restype = IMP


if hasattr(_libs['objc'], 'class_addIvar'):
    class_addIvar = _libs['objc'].class_addIvar
    class_addIvar.argtypes = [Class, String, c_size_t, c_uint8, String]
    class_addIvar.restype = BOOL


if hasattr(_libs['objc'], 'class_addProtocol'):
    class_addProtocol = _libs['objc'].class_addProtocol
    class_addProtocol.argtypes = [Class, POINTER(Protocol)]
    class_addProtocol.restype = BOOL


if hasattr(_libs['objc'], 'class_setIvarLayout'):
    class_setIvarLayout = _libs['objc'].class_setIvarLayout
    class_setIvarLayout.argtypes = [Class, String]
    class_setIvarLayout.restype = None


if hasattr(_libs['objc'], 'class_setWeakIvarLayout'):
    class_setWeakIvarLayout = _libs['objc'].class_setWeakIvarLayout
    class_setWeakIvarLayout.argtypes = [Class, String]
    class_setWeakIvarLayout.restype = None


if hasattr(_libs['objc'], 'method_getName'):
    method_getName = _libs['objc'].method_getName
    method_getName.argtypes = [Method]
    method_getName.restype = SEL


if hasattr(_libs['objc'], 'method_getImplementation'):
    method_getImplementation = _libs['objc'].method_getImplementation
    method_getImplementation.argtypes = [Method]
    method_getImplementation.restype = IMP


if hasattr(_libs['objc'], 'method_getTypeEncoding'):
    method_getTypeEncoding = _libs['objc'].method_getTypeEncoding
    method_getTypeEncoding.argtypes = [Method]
    if sizeof(c_int) == sizeof(c_void_p):
        method_getTypeEncoding.restype = ReturnString
    else:
        method_getTypeEncoding.restype = String
        method_getTypeEncoding.errcheck = ReturnString


if hasattr(_libs['objc'], 'method_getNumberOfArguments'):
    method_getNumberOfArguments = _libs['objc'].method_getNumberOfArguments
    method_getNumberOfArguments.argtypes = [Method]
    method_getNumberOfArguments.restype = c_uint


if hasattr(_libs['objc'], 'method_copyReturnType'):
    method_copyReturnType = _libs['objc'].method_copyReturnType
    method_copyReturnType.argtypes = [Method]
    if sizeof(c_int) == sizeof(c_void_p):
        method_copyReturnType.restype = ReturnString
    else:
        method_copyReturnType.restype = String
        method_copyReturnType.errcheck = ReturnString


if hasattr(_libs['objc'], 'method_copyArgumentType'):
    method_copyArgumentType = _libs['objc'].method_copyArgumentType
    method_copyArgumentType.argtypes = [Method, c_uint]
    if sizeof(c_int) == sizeof(c_void_p):
        method_copyArgumentType.restype = ReturnString
    else:
        method_copyArgumentType.restype = String
        method_copyArgumentType.errcheck = ReturnString


if hasattr(_libs['objc'], 'method_getReturnType'):
    method_getReturnType = _libs['objc'].method_getReturnType
    method_getReturnType.argtypes = [Method, String, c_size_t]
    method_getReturnType.restype = None


if hasattr(_libs['objc'], 'method_getArgumentType'):
    method_getArgumentType = _libs['objc'].method_getArgumentType
    method_getArgumentType.argtypes = [Method, c_uint, String, c_size_t]
    method_getArgumentType.restype = None


if hasattr(_libs['objc'], 'method_getDescription'):
    method_getDescription = _libs['objc'].method_getDescription
    method_getDescription.argtypes = [Method]
    method_getDescription.restype = POINTER(struct_objc_method_description)


if hasattr(_libs['objc'], 'method_setImplementation'):
    method_setImplementation = _libs['objc'].method_setImplementation
    method_setImplementation.argtypes = [Method, IMP]
    method_setImplementation.restype = IMP


if hasattr(_libs['objc'], 'method_exchangeImplementations'):
    method_exchangeImplementations = _libs['objc'].method_exchangeImplementations
    method_exchangeImplementations.argtypes = [Method, Method]
    method_exchangeImplementations.restype = None


if hasattr(_libs['objc'], 'ivar_getName'):
    ivar_getName = _libs['objc'].ivar_getName
    ivar_getName.argtypes = [Ivar]
    if sizeof(c_int) == sizeof(c_void_p):
        ivar_getName.restype = ReturnString
    else:
        ivar_getName.restype = String
        ivar_getName.errcheck = ReturnString


if hasattr(_libs['objc'], 'ivar_getTypeEncoding'):
    ivar_getTypeEncoding = _libs['objc'].ivar_getTypeEncoding
    ivar_getTypeEncoding.argtypes = [Ivar]
    if sizeof(c_int) == sizeof(c_void_p):
        ivar_getTypeEncoding.restype = ReturnString
    else:
        ivar_getTypeEncoding.restype = String
        ivar_getTypeEncoding.errcheck = ReturnString


if hasattr(_libs['objc'], 'ivar_getOffset'):
    ivar_getOffset = _libs['objc'].ivar_getOffset
    ivar_getOffset.argtypes = [Ivar]
    ivar_getOffset.restype = c_ptrdiff_t


if hasattr(_libs['objc'], 'property_getName'):
    property_getName = _libs['objc'].property_getName
    property_getName.argtypes = [objc_property_t]
    if sizeof(c_int) == sizeof(c_void_p):
        property_getName.restype = ReturnString
    else:
        property_getName.restype = String
        property_getName.errcheck = ReturnString


if hasattr(_libs['objc'], 'property_getAttributes'):
    property_getAttributes = _libs['objc'].property_getAttributes
    property_getAttributes.argtypes = [objc_property_t]
    if sizeof(c_int) == sizeof(c_void_p):
        property_getAttributes.restype = ReturnString
    else:
        property_getAttributes.restype = String
        property_getAttributes.errcheck = ReturnString


if hasattr(_libs['objc'], 'protocol_conformsToProtocol'):
    protocol_conformsToProtocol = _libs['objc'].protocol_conformsToProtocol
    protocol_conformsToProtocol.argtypes = [POINTER(Protocol), POINTER(Protocol)]
    protocol_conformsToProtocol.restype = BOOL


if hasattr(_libs['objc'], 'protocol_isEqual'):
    protocol_isEqual = _libs['objc'].protocol_isEqual
    protocol_isEqual.argtypes = [POINTER(Protocol), POINTER(Protocol)]
    protocol_isEqual.restype = BOOL


if hasattr(_libs['objc'], 'protocol_getName'):
    protocol_getName = _libs['objc'].protocol_getName
    protocol_getName.argtypes = [POINTER(Protocol)]
    if sizeof(c_int) == sizeof(c_void_p):
        protocol_getName.restype = ReturnString
    else:
        protocol_getName.restype = String
        protocol_getName.errcheck = ReturnString


if hasattr(_libs['objc'], 'protocol_getMethodDescription'):
    protocol_getMethodDescription = _libs['objc'].protocol_getMethodDescription
    protocol_getMethodDescription.argtypes = [POINTER(Protocol), SEL, BOOL, BOOL]
    protocol_getMethodDescription.restype = struct_objc_method_description


if hasattr(_libs['objc'], 'protocol_copyMethodDescriptionList'):
    protocol_copyMethodDescriptionList = _libs['objc'].protocol_copyMethodDescriptionList
    protocol_copyMethodDescriptionList.argtypes = [POINTER(Protocol), BOOL, BOOL, POINTER(c_uint)]
    protocol_copyMethodDescriptionList.restype = POINTER(struct_objc_method_description)


if hasattr(_libs['objc'], 'protocol_getProperty'):
    protocol_getProperty = _libs['objc'].protocol_getProperty
    protocol_getProperty.argtypes = [POINTER(Protocol), String, BOOL, BOOL]
    protocol_getProperty.restype = objc_property_t


if hasattr(_libs['objc'], 'protocol_copyPropertyList'):
    protocol_copyPropertyList = _libs['objc'].protocol_copyPropertyList
    protocol_copyPropertyList.argtypes = [POINTER(Protocol), POINTER(c_uint)]
    protocol_copyPropertyList.restype = POINTER(objc_property_t)


if hasattr(_libs['objc'], 'protocol_copyProtocolList'):
    protocol_copyProtocolList = _libs['objc'].protocol_copyProtocolList
    protocol_copyProtocolList.argtypes = [POINTER(Protocol), POINTER(c_uint)]
    protocol_copyProtocolList.restype = POINTER(POINTER(Protocol))


if hasattr(_libs['objc'], 'objc_copyImageNames'):
    objc_copyImageNames = _libs['objc'].objc_copyImageNames
    objc_copyImageNames.argtypes = [POINTER(c_uint)]
    objc_copyImageNames.restype = POINTER(POINTER(c_char))


if hasattr(_libs['objc'], 'class_getImageName'):
    class_getImageName = _libs['objc'].class_getImageName
    class_getImageName.argtypes = [Class]
    if sizeof(c_int) == sizeof(c_void_p):
        class_getImageName.restype = ReturnString
    else:
        class_getImageName.restype = String
        class_getImageName.errcheck = ReturnString


if hasattr(_libs['objc'], 'objc_copyClassNamesForImage'):
    objc_copyClassNamesForImage = _libs['objc'].objc_copyClassNamesForImage
    objc_copyClassNamesForImage.argtypes = [String, POINTER(c_uint)]
    objc_copyClassNamesForImage.restype = POINTER(POINTER(c_char))


if hasattr(_libs['objc'], 'sel_getName'):
    sel_getName = _libs['objc'].sel_getName
    sel_getName.argtypes = [SEL]
    if sizeof(c_int) == sizeof(c_void_p):
        sel_getName.restype = ReturnString
    else:
        sel_getName.restype = String
        sel_getName.errcheck = ReturnString


if hasattr(_libs['objc'], 'sel_getUid'):
    sel_getUid = _libs['objc'].sel_getUid
    sel_getUid.argtypes = [String]
    sel_getUid.restype = SEL


if hasattr(_libs['objc'], 'sel_registerName'):
    sel_registerName = _libs['objc'].sel_registerName
    sel_registerName.argtypes = [String]
    sel_registerName.restype = SEL


if hasattr(_libs['objc'], 'sel_isEqual'):
    sel_isEqual = _libs['objc'].sel_isEqual
    sel_isEqual.argtypes = [SEL, SEL]
    sel_isEqual.restype = BOOL


if hasattr(_libs['objc'], 'objc_enumerationMutation'):
    objc_enumerationMutation = _libs['objc'].objc_enumerationMutation
    objc_enumerationMutation.argtypes = [id]
    objc_enumerationMutation.restype = None


if hasattr(_libs['objc'], 'objc_setEnumerationMutationHandler'):
    objc_setEnumerationMutationHandler = _libs['objc'].objc_setEnumerationMutationHandler
    objc_setEnumerationMutationHandler.argtypes = [CFUNCTYPE(UNCHECKED(None), id)]
    objc_setEnumerationMutationHandler.restype = None


if hasattr(_libs['objc'], 'objc_setForwardHandler'):
    objc_setForwardHandler = _libs['objc'].objc_setForwardHandler
    objc_setForwardHandler.argtypes = [POINTER(None), POINTER(None)]
    objc_setForwardHandler.restype = None

struct_objc_category.__slots__ = [
    'category_name',
    'class_name',
    'instance_methods',
    'class_methods',
    'protocols',
]
struct_objc_category._fields_ = [
    ('category_name', String),
    ('class_name', String),
    ('instance_methods', POINTER(struct_objc_method_list)),
    ('class_methods', POINTER(struct_objc_method_list)),
    ('protocols', POINTER(struct_objc_protocol_list)),
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


class struct_objc_symtab(Structure):
    pass

Symtab = POINTER(struct_objc_symtab) 


struct_objc_symtab.__slots__ = [
    'sel_ref_cnt',
    'refs',
    'cls_def_cnt',
    'cat_def_cnt',
    'defs',
]
struct_objc_symtab._fields_ = [
    ('sel_ref_cnt', c_ulong),
    ('refs', POINTER(SEL)),
    ('cls_def_cnt', c_ushort),
    ('cat_def_cnt', c_ushort),
    ('defs', POINTER(None) * 1),
]

Cache = POINTER(struct_objc_cache) 


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


class struct_objc_module(Structure):
    pass

Module = POINTER(struct_objc_module) 


struct_objc_module.__slots__ = [
    'version',
    'size',
    'name',
    'symtab',
]
struct_objc_module._fields_ = [
    ('version', c_ulong),
    ('size', c_ulong),
    ('name', String),
    ('symtab', Symtab),
]


if hasattr(_libs['objc'], 'sel_isMapped'):
    sel_isMapped = _libs['objc'].sel_isMapped
    sel_isMapped.argtypes = [SEL]
    sel_isMapped.restype = BOOL


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'object_copyFromZone'):
        continue
    object_copyFromZone = _lib.object_copyFromZone
    object_copyFromZone.argtypes = [id, c_size_t, POINTER(None)]
    object_copyFromZone.restype = id
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'object_realloc'):
        continue
    object_realloc = _lib.object_realloc
    object_realloc.argtypes = [id, c_size_t]
    object_realloc.restype = id
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'object_reallocFromZone'):
        continue
    object_reallocFromZone = _lib.object_reallocFromZone
    object_reallocFromZone.argtypes = [id, c_size_t, POINTER(None)]
    object_reallocFromZone.restype = id
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_getClasses'):
        continue
    objc_getClasses = _lib.objc_getClasses
    objc_getClasses.argtypes = []
    objc_getClasses.restype = POINTER(None)
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_addClass'):
        continue
    objc_addClass = _lib.objc_addClass
    objc_addClass.argtypes = [Class]
    objc_addClass.restype = None
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_setClassHandler'):
        continue
    objc_setClassHandler = _lib.objc_setClassHandler
    objc_setClassHandler.argtypes = [CFUNCTYPE(UNCHECKED(c_int), String)]
    objc_setClassHandler.restype = None
    break


if hasattr(_libs['objc'], 'objc_setMultithreaded'):
    objc_setMultithreaded = _libs['objc'].objc_setMultithreaded
    objc_setMultithreaded.argtypes = [BOOL]
    objc_setMultithreaded.restype = None


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'class_createInstanceFromZone'):
        continue
    class_createInstanceFromZone = _lib.class_createInstanceFromZone
    class_createInstanceFromZone.argtypes = [Class, c_size_t, POINTER(None)]
    class_createInstanceFromZone.restype = id
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'class_addMethods'):
        continue
    class_addMethods = _lib.class_addMethods
    class_addMethods.argtypes = [Class, POINTER(struct_objc_method_list)]
    class_addMethods.restype = None
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'class_removeMethods'):
        continue
    class_removeMethods = _lib.class_removeMethods
    class_removeMethods.argtypes = [Class, POINTER(struct_objc_method_list)]
    class_removeMethods.restype = None
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'class_poseAs'):
        continue
    class_poseAs = _lib.class_poseAs
    class_poseAs.argtypes = [Class, Class]
    class_poseAs.restype = Class
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'method_getSizeOfArguments'):
        continue
    method_getSizeOfArguments = _lib.method_getSizeOfArguments
    method_getSizeOfArguments.argtypes = [Method]
    method_getSizeOfArguments.restype = c_uint
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'method_getArgumentInfo'):
        continue
    method_getArgumentInfo = _lib.method_getArgumentInfo
    method_getArgumentInfo.argtypes = [POINTER(struct_objc_method), c_int, POINTER(POINTER(c_char)), POINTER(c_int)]
    method_getArgumentInfo.restype = c_uint
    break


if hasattr(_libs['objc'], 'class_respondsToMethod'):
    class_respondsToMethod = _libs['objc'].class_respondsToMethod
    class_respondsToMethod.argtypes = [Class, SEL]
    class_respondsToMethod.restype = BOOL


if hasattr(_libs['objc'], 'class_lookupMethod'):
    class_lookupMethod = _libs['objc'].class_lookupMethod
    class_lookupMethod.argtypes = [Class, SEL]
    class_lookupMethod.restype = IMP


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'objc_getOrigClass'):
        continue
    objc_getOrigClass = _lib.objc_getOrigClass
    objc_getOrigClass.argtypes = [String]
    objc_getOrigClass.restype = Class
    break


for _lib in _libs.itervalues():
    if not hasattr(_lib, 'class_nextMethodList'):
        continue
    class_nextMethodList = _lib.class_nextMethodList
    class_nextMethodList.argtypes = [Class, POINTER(POINTER(None))]
    class_nextMethodList.restype = POINTER(struct_objc_method_list)
    break


for _lib in _libs.values():
    try:
        _alloc = (POINTER(CFUNCTYPE(UNCHECKED(id), Class, c_size_t))).in_dll(_lib, '_alloc')
        break
    except:
        pass


for _lib in _libs.values():
    try:
        _copy = (POINTER(CFUNCTYPE(UNCHECKED(id), id, c_size_t))).in_dll(_lib, '_copy')
        break
    except:
        pass


for _lib in _libs.values():
    try:
        _realloc = (POINTER(CFUNCTYPE(UNCHECKED(id), id, c_size_t))).in_dll(_lib, '_realloc')
        break
    except:
        pass


for _lib in _libs.values():
    try:
        _dealloc = (POINTER(CFUNCTYPE(UNCHECKED(id), id))).in_dll(_lib, '_dealloc')
        break
    except:
        pass


for _lib in _libs.values():
    try:
        _zoneAlloc = (POINTER(CFUNCTYPE(UNCHECKED(id), Class, c_size_t, POINTER(None)))).in_dll(_lib, '_zoneAlloc')
        break
    except:
        pass


for _lib in _libs.values():
    try:
        _zoneRealloc = (POINTER(CFUNCTYPE(UNCHECKED(id), id, c_size_t, POINTER(None)))).in_dll(_lib, '_zoneRealloc')
        break
    except:
        pass


for _lib in _libs.values():
    try:
        _zoneCopy = (POINTER(CFUNCTYPE(UNCHECKED(id), id, c_size_t, POINTER(None)))).in_dll(_lib, '_zoneCopy')
        break
    except:
        pass


for _lib in _libs.values():
    try:
        _error = (POINTER(CFUNCTYPE(UNCHECKED(None), id, String, c_void_p))).in_dll(_lib, '_error')
        break
    except:
        pass


try:
    _C_ID = '@'
except:
    pass


try:
    _C_CLASS = '#'
except:
    pass


try:
    _C_SEL = ':'
except:
    pass


try:
    _C_CHR = 'c'
except:
    pass


try:
    _C_UCHR = 'C'
except:
    pass


try:
    _C_SHT = 's'
except:
    pass


try:
    _C_USHT = 'S'
except:
    pass


try:
    _C_INT = 'i'
except:
    pass


try:
    _C_UINT = 'I'
except:
    pass


try:
    _C_LNG = 'l'
except:
    pass


try:
    _C_ULNG = 'L'
except:
    pass


try:
    _C_LNG_LNG = 'q'
except:
    pass


try:
    _C_ULNG_LNG = 'Q'
except:
    pass


try:
    _C_FLT = 'f'
except:
    pass


try:
    _C_DBL = 'd'
except:
    pass


try:
    _C_BFLD = 'b'
except:
    pass


try:
    _C_BOOL = 'B'
except:
    pass


try:
    _C_VOID = 'v'
except:
    pass


try:
    _C_UNDEF = '?'
except:
    pass


try:
    _C_PTR = '^'
except:
    pass


try:
    _C_CHARPTR = '*'
except:
    pass


try:
    _C_ATOM = '%'
except:
    pass


try:
    _C_ARY_B = '['
except:
    pass


try:
    _C_ARY_E = ']'
except:
    pass


try:
    _C_UNION_B = '('
except:
    pass


try:
    _C_UNION_E = ')'
except:
    pass


try:
    _C_STRUCT_B = '{'
except:
    pass


try:
    _C_STRUCT_E = '}'
except:
    pass


try:
    _C_VECTOR = '!'
except:
    pass


try:
    _C_CONST = 'r'
except:
    pass


def CLS_GETINFO(cls, infomask):
    return (((cls.contents.info).value) & infomask)


def CLS_SETINFO(cls, infomask):
    return ((cls.contents.info) | infomask)


try:
    CLS_CLASS = 1
except:
    pass


try:
    CLS_META = 2
except:
    pass


try:
    CLS_INITIALIZED = 4
except:
    pass


try:
    CLS_POSING = 8
except:
    pass


try:
    CLS_MAPPED = 16
except:
    pass


try:
    CLS_FLUSH_CACHE = 32
except:
    pass


try:
    CLS_GROW_CACHE = 64
except:
    pass


try:
    CLS_NEED_BIND = 128
except:
    pass


try:
    CLS_METHOD_ARRAY = 256
except:
    pass


try:
    CLS_JAVA_HYBRID = 512
except:
    pass


try:
    CLS_JAVA_CLASS = 1024
except:
    pass


try:
    CLS_INITIALIZING = 2048
except:
    pass


try:
    CLS_FROM_BUNDLE = 4096
except:
    pass


try:
    CLS_HAS_CXX_STRUCTORS = 8192
except:
    pass


try:
    CLS_NO_METHOD_ARRAY = 16384
except:
    pass


try:
    CLS_HAS_LOAD_METHOD = 32768
except:
    pass


try:
    CLS_CONSTRUCTING = 65536
except:
    pass


try:
    CLS_EXT = 131072
except:
    pass


def CACHE_BUCKET_NAME(B):
    return (B.contents.method_name)


def CACHE_BUCKET_IMP(B):
    return (B.contents.method_imp)


def CACHE_BUCKET_VALID(B):
    return B


def CACHE_HASH(sel, mask):
    return ((sel >> 2) & mask)


try:
    OBSOLETE_OBJC_GETCLASSES = 1
except:
    pass


try:
    OBJC_NEXT_METHOD_LIST = 1
except:
    pass

objc_class = struct_objc_class 


objc_method = struct_objc_method 


objc_ivar = struct_objc_ivar 


objc_category = struct_objc_category 


objc_property = struct_objc_property 


objc_ivar_list = struct_objc_ivar_list 


objc_method_list = struct_objc_method_list 


objc_cache = struct_objc_cache 


objc_protocol_list = struct_objc_protocol_list 


objc_method_description = struct_objc_method_description 


objc_method_description_list = struct_objc_method_description_list 


objc_symtab = struct_objc_symtab 


objc_module = struct_objc_module 