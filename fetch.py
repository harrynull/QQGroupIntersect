import requests
import pickle
import json
import time
import sys
from collections import OrderedDict
URL_GET_MEMBERS="http://qun.qq.com/cgi-bin/qun_mgr/search_group_members"
URL_GET_GROUPS="http://qun.qq.com/cgi-bin/qun_mgr/get_group_list"

def qq_request(url, cookies, payload):

    # generate the csrf token
    csrf_token = 5381
    for c in cookies["skey"]: csrf_token += (csrf_token << 5) + ord(c)
    payload['bkn']=2147483647&csrf_token

    # post request
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    return requests.post(url,data=payload,headers=headers,cookies=cookies).text
    
def get_groups(cookies):
    result_list=[]
    
    try:
        raw_result=qq_request(URL_GET_GROUPS,cookies,{})
        groups_json=json.loads(raw_result)
        
        if "create" in groups_json:
            for group in groups_json["create"]: result_list.append(group["gc"])
        if "manage" in groups_json:
            for group in groups_json["manage"]: result_list.append(group["gc"])
        if "join" in groups_json:
            for group in groups_json["join"]: result_list.append(group["gc"])
    except:
        print("Failed to get groups. Received:", raw_result)
        return []
        
    return result_list
    
def get_group_members(group_id, cookies):
    
    try:
        raw_result=qq_request(URL_GET_MEMBERS,cookies,{'gc':group_id,'st':0,'end':2000})
        members_json=json.loads(raw_result)
        count_group_members=members_json["search_count"]
    except:
        print("Failed to get group members. Received:", raw_result)
        return {}
        
    result={}
    for mem in members_json["mems"]:
        result[mem["uin"]]=mem["nick"]
    
    # check count
    assert(count_group_members==len(result))
    return result

cookies={'uin':sys.argv[1], 'skey':sys.argv[2], 'p_skey':sys.argv[3]}
groups=get_groups(cookies)
print("Groups: "+" ".join([str(g) for g in groups]))

for group_id in groups:
    print(group_id,end="\r")
    pickle.dump(get_group_members(group_id, cookies), open("{}.dat".format(group_id),"wb"))
    time.sleep(0.5)
