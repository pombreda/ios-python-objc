# List all the methods of an Objective-C class.

import objc
from objc import *

def list_methods(cls):
    count = c_uint()
    method_array = objc.class_copyMethodList(cls, byref(count))
    print count.value, 'methods'
    print '------------------'
    names = []
    for i in range(count.value):
        method = pointer(method_array[i])
        sel = pointer(objc.method_getName(method))
        name = objc.sel_getName(sel)
        encoding = objc.method_getTypeEncoding(method)
        return_type = objc.method_copyReturnType(method)
        names.append((name, encoding, return_type))

    names.sort()
    for x, y, z in names: 
        print x, y

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'USAGE: python list_methods.py <Obj-C Class>'
        exit(1)
    
    class_name = sys.argv[1]
    cls = objc.objc_getClass(class_name)

    print class_name, 'instance methods:'
    list_methods(cls)
        
    print
    print class_name, 'class methods:'
    list_methods(objc.object_getClass(cls))
