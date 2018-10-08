#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import codecs

if len(sys.argv) <= 1:
    print("usage: %s jsonFile" % sys.argv[0])
    sys.exit(1)

with open(sys.argv[1]) as fd:
    cont = json.load(fd)
    print(json.dumps(cont, ensure_ascii=False, indent=4))

