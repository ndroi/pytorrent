import pytorrent
t=pytorrent.Torrent()
t.load("test.torrent")  #your torrent file
print t.data["info"]["name"].decode("utf-8")
files=t.data["info"]["files"]
for item in files:
    print item["path"][0].decode("utf-8")
t.data["info"]["name"]="my_name" #change info. some software may read ["info"]["name.utf-8"]
t.dump("dump.torrent")  #the new torrent file

