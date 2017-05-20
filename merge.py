import pickle
import sys

name,groups=sys.argv[1],sys.argv[2:]

result={}

for group_id in groups: result={**result,**pickle.load(open("{}.dat".format(group_id),"rb"))}

pickle.dump(result,open("{}.dat".format(name),"wb"))