from utils import *
"""
a class to parser torrent file.
it can get info from the file,
and dump to a new file.
if you find any bugs or have any advice,please email
androiosymbian@hotmail.com.
I will fix it.
"""
class Torrent:
    def __init__(self):
        self.data={}
    def load(self,filename):
        self.stream=Stream(filename,"rb")
        if self.stream.next()=='d':
            self.data=build_dic(self.stream)
        else:
            raise Exception("invalid torrent file")
    def dump(self,filename):
        self.stream=Stream(filename,"wb")
        dump_dic(self.stream,self.data)

