import mod_api
import mod_func
from mod_def import mod_def

haxdb = None


def init(hdb):
    global haxdb
    haxdb = hdb
    haxdb.mod2db(mod_def)
    mod_func.init(haxdb)
    mod_api.init(haxdb)
    return mod_def


def run():
    mod_func.run()
    mod_api.run()
