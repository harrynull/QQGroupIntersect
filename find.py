from collections import OrderedDict
import pickle
import sys

target,groups=sys.argv[1],sys.argv[2:]

for group_id in groups:
    r=pickle.load(open("{}.dat".format(group_id),"rb"))
    for uid, nick in r.items():
        if str(uid)==target:
            print("{} found in {}, nickname: {}".format(uid, group_id, nick))
                