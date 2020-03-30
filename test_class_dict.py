# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 11:01:54 2018

@author: XT21586
"""
import pprint, pickle

class Mapping(dict):
   def __init__(self,*arg,**kw):
      super(Mapping, self).__init__(*arg, **kw)

'''
class Mapping(dict):

    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):
        return self.__dict__[key]

    def __repr__(self):
        return repr(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __delitem__(self, key):
        del self.__dict__[key]

    def clear(self):
        return self.__dict__.clear()

    def copy(self):
        return self.__dict__.copy()

    def has_key(self, k):
        return k in self.__dict__

    def update(self, *args, **kwargs):
        return self.__dict__.update(*args, **kwargs)

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def items(self):
        return self.__dict__.items()

    def pop(self, *args):
        return self.__dict__.pop(*args)

    def __cmp__(self, dict_):
        return self.__cmp__(self.__dict__, dict_)

    def __contains__(self, item):
        return item in self.__dict__

    def __iter__(self):
        return iter(self.__dict__)

    def __unicode__(self):
        return unicode(repr(self.__dict__))
'''

def loadall(filename):
    with open(filename, "rb") as f:
        while True:
            try:
                yield pickle.load(f)
            except EOFError:
                break




okeep = []


o = Mapping()
o.foo = "bar"
o['lumberjack'] = 'foo'
o.update({'a': 'b'}, c=44)
print ('lumberjack' in o)
print (o)
o.update({'a': 'b1'}, c=444)        
o['t2'] = {'t2k':'t2d'}
o['t3'] = [{'t3k':'t3d'},{'t3ak':'t3ad'}]
okeep.append(o)

o1 = Mapping()
o1.foo = "bar"
o1['lumberjack'] = 'foo'
o1.update({'a': 'b'}, c=44)
print ('lumberjack' in o1)
print (o1)
o1.update({'a': 'b1'}, c=444)        
o1['t2'] = {'t2k':'t2d'}
o1['t3'] = [{'t3k':'t3d'},{'t3ak':'t3ad'},{'t3bk':'t3bd'}]
okeep.append(o1)   

path1 = "C:\\Users\\XT21586\\Documents\\document\\Data Stage\\export1\\data_mapping\\"
outfilename1 = path1 + "pickle1.pk1"
output = open(outfilename1, 'wb')

[pickle.dump(ox, output) for ox in okeep]

#pickle.dump(o, output)
output.close()


infilename1 = path1 + "pickle1.pk1"

for obj in loadall(infilename1):
    # process object
    # for the demo we just print
    pprint.pprint(obj)



#pkl_file = open(infilename1, 'rb')

#lobj = []
#for obj in loadall(infilename1):
#    lobj.append(obj)

#data1 = pickle.load(pkl_file)
#print (data1)
#pprint.pprint(data1)

#for li in lobj:
#    pprint.pprint(li)    



#pkl_file.close()
