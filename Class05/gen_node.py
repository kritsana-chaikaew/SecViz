import pandas as pd
import json
import sys
import os.path

if len(sys.argv) != 2:
    exit()

file_in = sys.argv[1]
if not os.path.isfile(file_in):
    exit()


f = open(file_in, 'r')
data = pd.read_csv(f, sep=',', header=None)

nodes = []

for row in data.values:
    nodes.append({'name':row[1], 'value':row[0]})

print(json.dumps(nodes, indent=4, sort_keys=True))
