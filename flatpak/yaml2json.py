#!/usr/bin/python
import sys
import json
import yaml

fname = sys.argv[1]

with open(fname, 'r') as f:
    yaml_data = yaml.safe_load(f)

with open(fname.replace('yml', 'json'),'w') as out:
    json.dump(yaml_data, out)
