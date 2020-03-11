import json
DataEtab=[]
with open(r'C:\Users\izaganami\Data_proj\implantout.json') as fp:
    try:
        for line in fp:
            comment = json.loads(line)
            print(comment['fields']['uai'])
            DataEtab.append(comment['fields']['uai'])
    except(UnicodeDecodeError):
        print("\nLoading 'effectif' Done\n")
