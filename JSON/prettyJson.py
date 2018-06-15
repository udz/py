import os
import json
import pprint

# Print CWD
cwd = os.getcwd()
#print("Current Working Directory is" + cwd)

file = open('JSON/testoutput.txt','w') 

with open('JSON/data.json') as f:
    data = json.load(f)
pprint.pprint(data,file)

file.close()