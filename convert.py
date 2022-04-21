#!/usr/bin/env python3

import yaml
import json

obj = yaml.safe_load(open("sample.yaml", "r").read())
obj["$schema"] = "./concourse-pipeline.schema.json"
open("sample.json", "w").write(json.dumps(obj, indent=2))
