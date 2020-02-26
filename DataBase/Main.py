import pydbgen
from pydbgen import pydbgen
from tableschema import Table
from faker import Faker
import rhinoscript as rs
import json

filter = "JSON file (*.json)|*.json|All Files (*.*)|*.*||"
filename = rs.OpenFileName("DataBase\etablissements-denseignement-superieur.json", filter)

#Read JSON data into the datastore variable
if filename:
    with open(filename, 'r') as f:
        datastore = json.load(f)

#Use the new datastore datastructure
print(datastore["lon"])

Names=[]
fake=Faker("fr_FR")
for i in range(0,200):
    name=fake.name()
    if name not in Names:
        Names.append(name)
    print(name)

GenDB=pydbgen.pydb();

Loc=[]
for i in range(0,200):
    loc=fake.local_latlng(country_code='FR', coords_only=False)
    if loc not in Loc:
        Loc.append(loc)
    print(loc)

print(fake.address())

