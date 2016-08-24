#try to blur(change filename in torrrent file to hash)
#then to avoid some btsoftware check like "Thunder"
import pytorrent
def rename(name):
    pos=name.find(".")
    if pos==-1:
        return str(hash(name))
    return str(hash(name[:pos]))+name[pos:]
def blur(torrent,dumpname):
    info=t.data["info"]
    #name
    name=t.data["info"]["name"]
    t.data["info"]["name"]=rename(name)
    if info.has_key("name.utf-8"):
        name_utf8=t.data["info"]["name.utf-8"]
        t.data["info"]["name.utf-8"]=rename(name_utf8)
    #publisher
    if info.has_key("publisher"):
        t.data["publisher"]="no publisher"
    if info.has_key("publisher.utf-8"):
        t.data["publisher.utf-8"]="no publisher"
    #comment
    if info.has_key("comment"):
        t.data["comment"]="blured by pyTorrent"
    if info.has_key("comment.utf-8"):
        t.data["comment.utf-8"]="blured by pyTorrent"
    #path
    if info.has_key("files"):
        files=t.data["info"]["files"]
        for file in files:
            paths=file["path"]
            for i in range(len(paths)):
                paths[i]=rename(paths[i])
            if info.has_key("path.utf-8"):
                paths=file["path.utf-8"]
            for i in range(len(paths)):
                paths[i]=rename(paths[i])
    t.dump(dumpname)

t=pytorrent.Torrent()
t.load("test.torrent")  #your torrent file
blur(t,"blured.torrent")
    