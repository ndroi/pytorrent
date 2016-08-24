from __builtin__ import Exception
"""
for loadfile
"""
def build_dic(stream):#call after symbol 'd' found
    list=[]
    proxy_build(stream,list)
    dic={}
    for i in range(0,len(list)-1,2):   #convert a list[k1,v1,k2,v2...] to a dic
        dic[list[i]]=list[i+1]
    return dic
def build_list(stream):#call after symbol 'l' found
    list=[]
    proxy_build(stream,list)
    return list
def build_str(stream,str_len):#call after num found
    values=[]
    for i in range(str_len):
        values.append(stream.next())
    return ''.join(values)
def build_num(stream):#call after symbol 'i' found
    num=0
    minus=False
    while True:
        ch=stream.next()
        if ch>='0' and ch<='9':
            num=num*10+int(ch)
        elif ch=='-':
            minus=True
        elif ch=='e':
            break
        else:
            raise Exception("invalid torrent file")
    num=-num if minus else num
    return num
def proxy_build(stream,list): #because build_dic and build_list is simaliar,so I def a proxy-function  
    while True:
        ch=stream.next()
        if ch>='0' and ch<='9':#I think ch==0 is not very valid,but just do this.
            str_len=int(ch)
            while True:
                ch=stream.next()
                if ch==':':
                    break
                elif ch>='0' and ch<='9':
                    str_len=str_len*10+int(ch)
                else:
                    raise Exception("invalid torrent file")
            list.append(build_str(stream,str_len))
        elif ch=='l':
            list.append(build_list(stream))
        elif ch=='i':
            list.append(build_num(stream))
        elif ch=='d':
            list.append(build_dic(stream))
        elif ch=='e':
            break
        else:
            raise Exception("invalid torrent file")

"""
for dumpfile
"""
import types
def dump_dic(stream,dic):
    stream.put("d")
    for k,v in dic.items():
        dump_str(stream,k)
        proxy_dump(stream,v)
    stream.put("e")
def dump_list(stream,list):
    stream.put("l")
    for item in list:
        proxy_dump(stream,item)
    stream.put("e")
def dump_str(stream,mystr):
    stream.put(str(len(mystr))+":")
    stream.put(mystr)
def dump_num(stream,num):
    stream.put("i")
    stream.put(str(num))
    stream.put("e")
def proxy_dump(stream,item):
    if isinstance(item,types.DictionaryType):
        dump_dic(stream,item)
    elif isinstance(item,types.ListType):
        dump_list(stream,item)
    elif isinstance(item,types.StringType):
        dump_str(stream,item)
    elif isinstance(item,types.IntType):
        dump_num(stream,item)
    else:
        raise Exception("dump info error")
"""
byte stream
"""
class Stream:       
    def __init__(self,filename,mode):
        self.file=open(filename,mode)
    def next(self): #for mode r
        return self.file.read(1)
    def put(self,byte): #for mode w
        self.file.write(byte)
    def __del__(self):
        self.file.close()
