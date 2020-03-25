import json
import re
import random

DataEtab=[]
with open(r'Data_proj/implantout.json') as fp:
    try:
        for line in fp:
            comment = json.loads(line)
            print(comment['fields']['coordonnees'])
            DataEtab.append(comment)
    except(UnicodeDecodeError,KeyError):
        print("\nLoading 'effectif' Done\n")
        print(len(DataEtab))

with open(r'Data_proj\residout.json',encoding='utf-8') as fp:
    for line in fp:
        try:
            resid = json.loads(line)
            regex = r"\d+ (ch|Ch|t|T|st|St|lit|L|ST)"
            matches = re.finditer(regex,resid["fields"]["infos"], re.MULTILINE)
            tot=0
            for a,b in enumerate(matches, start=1):
                tot+=b.start()
                print("Places:{}".format(b.start()))
            if(tot==0):
                tot=random.randint(80,500)
                print("Randonly generated")
            print("Tot:{}".format(tot))

        except(KeyError):
            continue
    print("\nLoading 'resid' Done\n")


