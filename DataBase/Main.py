import json
Eff=[]
with open(r'C:\Users\izaganami\Data_proj\effectifout.json') as fp:
    for line in fp:
        comment = json.loads(line)
        Eff.append(comment['fields']['etablissement'])
print("\nLoading 'effectif' Done\n")

Cord=[]
with open(r'C:\Users\izaganami\Data_proj\cordetabout.json') as fp:
    for line in fp:
        comment = json.loads(line)
        Cord.append(comment['fields']['code_uai'])


print("\nLoading 'cords' Done\n")
Intersect=[]
for i in range(len(Eff)):
    if(Eff[i] in Cord):
        Intersect.append(Eff[i])
print("{}/{}/{}/ \n".format(len(Eff),len(Cord),len(Intersect)))
