import sys
import json

data = json.load(sys.stdin)
menu = data["menu"]
items = menu["items"]
#isum = 0
#json.dumps(items)

def parse_json(items):
    isum = 0
    for i in items:
        try:
            lid = i["id"]
            l = None
            #print(i)
            if "label" in i:
            #    #li = json.loads(lid, parse_int=int)
                isum += lid
                #print("found label: ", i, i["id"], i["label"])
        except TypeError:
           pass
    print(isum)


parse_json(items)
