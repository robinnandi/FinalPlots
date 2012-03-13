import types
import sys
import copy

class PSet(object):
    _dict={}
    def __init__(self,**kwargs):
        self._dict={}
        for key in kwargs:
            if kwargs[key] is not None:
                self._dict[key]=kwargs[key]

    def __setattr__(self,name,value):
        if not name.startswith("_"):
           if not name in self._dict:
               sys.stderr.write(header_eq+"\n")
               sys.stderr.write("WARNING: Binding variable in PSet ('%s') that is not in base definition.\n" % name)
               sys.stderr.write("Note that this may well be an error in your script!\n")
               sys.stderr.write(header_eq+"\n")
           self._dict[name]=value
        else:
            self.__dict__[name]=value

    def _quiet_set(self,name,value):
        self._dict[name]=value

    def __getattr__(self,name):
        if name in self._dict:
            return self._dict[name]
        else:
            raise AttributeError

    def __contains__(self,item):
        return (item in self._dict)

    def _flatten(self):
        flat={}
        for (key,val) in self._dict.iteritems():
            if val.__class__.__name__== PSet.__name__:
                for (k,v) in val._flatten().iteritems():
                    flat[key+"."+k]=v
            else:
                flat[key]=val
        return flat

    def ps(self):
        pset=ParameterSet()
        for (k,v) in self._flatten().iteritems():
            if v.__class__.__name__=="float":
                pset.AddDouble(k,v)
            elif v.__class__.__name__=="int":
                pset.AddInt(k,v)
            elif v.__class__.__name__=="str":
                pset.AddString(k,v)
            elif v.__class__.__name__=="bool":
                pset.AddBool(k,v)
        return pset

    def print_out(self):
        for (k,v) in  self._flatten().iteritems():
            print "%s = %s" % (k,v)

    def copy(self):
        return copy.deepcopy(self)
