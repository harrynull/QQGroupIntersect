import requests
import json
import time
import sys
from collections import OrderedDict
URL="http://qun.qq.com/cgi-bin/qun_mgr/search_group_members"

def get_group_members(group_id,cookies):
    # generate the csrf token
    csrf_token = 5381
    for c in cookies["skey"]: csrf_token += (csrf_token << 5) + ord(c)
    
    # post request
    data={'gc':group_id,'st':0,'end':2000,'bkn':2147483647&csrf_token}
    request_result=requests.post(URL,data=data,cookies=cookies).text
    members_json=json.loads(request_result)
    count_group_members=members_json["search_count"]
    result={}
    for mem in members_json["mems"]:
        result[mem["uin"]]=mem["nick"]
    
    # check count
    assert(count_group_members==len(result))
    return result

cookies={'uin':sys.argv[1], 'skey':sys.argv[2]}
group_ids=sys.argv[3:]
members_results={}

for group_id in group_ids:
    members_results[group_id]=get_group_members(group_id, cookies)
    time.sleep(1)

result={}
uid_name={}
# get the intersection
for gid, group in members_results.items():
    for uid, nick in group.items():
        uid_name[uid]=nick
        list=result.get(uid, [])
        list.append(gid)
        result[uid]=list
        
sorted_result=OrderedDict(sorted(result.items(), key=lambda t: len(t[1]), reverse=True))
# output the intersection
for uid, list in sorted_result.items():
    if len(list)>1:
        print("(%d) %s(%s): %s"%(len(list),uid_name[uid],uid,",".join(list)))