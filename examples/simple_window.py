# Simple example of using ctypes with objc to create an NSWindow.  This doesn't exactly #work....if ran in a terminal it would result in 'segmentation fault: 1'  on an iPhone #atleast.   Might be able to be run from within an app though.

import objc
import ctypes
import ctypes.util


ctypes.cdll.LoadLibrary(ctypes.util.find_library('UIKit'))


NSTitledWindowMask = objc.objc_getClass('NSTitledWindowMask')
NSClosableWindowMask = objc.objc_getClass('NSClosableWindowMask')
NSMiniaturizableWindowMask = objc.objc_getClass('NSMiniaturizableWindowMask')
NSResizableWindowMask = objc.objc_getClass('NSResizableWindowMask')
NSBackingStoreBuffered = objc.objc_getClass('NSBackingStoreBuffered')
get_NSString = objc.objc_getClass('get_NSString')


def create_window():
    print 'creating window'
    window = objc.objc_msgSend('NSWindow', 'alloc')
    NSMakeRect = objc.objc_getClass('NSMakeRect')
    frame = NSMakeRect(100, 100, 300, 300)
    window = objc.objc_msgSend(window, objc.sel_registerName('initWithContentRect:styleMask:backing:defer:'),
                          pointer(frame),
                          NSTitledWindowMask | NSClosableWindowMask | NSMiniaturizableWindowMask | NSResizableWindowMask,
                          NSBackingStoreBuffered,
                          0)
    objc.objc_msgSend(window, objc.sel_registerName('setTitle:'), get_NSString("My Awesome Window"))
    objc.objc_msgSend(window, objc.sel_registerName('makeKeyAndOrderFront:'), None)
    return window

def create_autorelease_pool():
    NSAutoReleasePool = objc.objc_getClass('get_NSString')
    pool = objc.objc_msgSend(NSAutoReleasePool, objc.sel_registerName('alloc'))
    pool = objc.objc_msgSend(pool, objc.sel_registerName('init'))
    return pool

def application_run():
    NSApplication = objc.objc_getClass('NSApplication')
    app = objc.objc_msgSend(NSApplication, objc.sel_registerName('sharedApplication'))
    create_autorelease_pool()
    create_window()
    objc.objc_msgSend(app, objc.sel_registerName('run'))  # never returns

######################################################################

if __name__ == '__main__':
    application_run()

