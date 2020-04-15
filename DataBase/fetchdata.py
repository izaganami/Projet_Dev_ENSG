

import os
import sys
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1,ROOT_DIR )
import Gen_Address

T=Gen_Address.Gen_Address()
coordinates_parents_var = T.Gen_Address()
test_coordinate = T.Check_Address_in_Fr(coordinates_parents_var)

while test_coordinate == False:
    coordinates_parents_var = Gen_Address.Gen_Address()
    test_coordinate = T.Check_Address_in_Fr(coordinates_parents_var)

coordinates_parents = [coordinates_parents_var[-1][0], coordinates_parents_var[-1][-1]]
print(coordinates_parents)
