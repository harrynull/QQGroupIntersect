from collections import OrderedDict
import pickle
import sys

groups=sys.argv[1:]
id2name=pickle.load(open("id.dat","rb"))

members_results={}

for group_id in groups: members_results[group_id]=pickle.load(open("{}.dat".format(group_id),"rb"))

result={}
uid_name={}
# get the intersection
for gid, group in members_results.items():
    for uid, nick in group.items():
        uid_name[uid]=nick
        list=result.get(uid, [])
        list.append((gid, id2name[int(gid)].replace("&nbsp;"," ") if gid.isdigit() and int(gid) in id2name else "N/A"))
        result[uid]=list
        
sorted_result=OrderedDict(sorted(result.items(), key=lambda t: len(t[1]), reverse=True))
# output the intersection
for uid, list in sorted_result.items():
    if len(list)>1:
        print("(%d) %s(%s): %s"%(len(list),uid_name[uid],uid,", ".join(["{}({})".format(id,name) if name!="N/A" else id for id,name in list])))