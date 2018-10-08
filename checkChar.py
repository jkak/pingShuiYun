#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import codecs

if len(sys.argv) <= 1:
    print("usage: %s jsonFile 看 元" % sys.argv[0])
    sys.exit(1)

with open(sys.argv[1]) as fd:
    cont = json.load(fd)

    for ch in sys.argv[2:]:
        # each char
        print(ch.decode("utf-8"))
        for item in cont[ch.decode("utf-8")]:
            print("   %s %s" % (item[0], item[1]))

