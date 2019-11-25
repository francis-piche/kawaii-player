#!/usr/bin/python
import sys
import yaml

fname = sys.argv[1]

with open(fname, 'r') as f:
    json_data = yaml.safe_load(f)

with open(fname.replace('json', 'yml'),'w') as out:
    out.writelines(("---\n",))
    yaml.dump(json_data, out, default_flow_style=False)
    out.writelines(("...\n",))
