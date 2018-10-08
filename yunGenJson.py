#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import os, sys
reload(sys)
sys.setdefaultencoding('utf-8')
import codecs
import json

def checkFile(argv):
    if len(argv) != 2:
        print("usage: %s file" % argv[0])
        sys.exit(-1)
    name = argv[1]
    if not os.path.exists(name):
        print("source file: %s not exist!" % name)
        sys.exit(-2)
    return name

def readFile(inFile):
    ''' fles contents:
          十三元平=+言园源原...;  空行； 其它...;
          僻字行(可能有多行)...;
    '''
    with open(inFile) as fd:
        originDic = {}
        for line in fd.readlines():
            line = line.strip()
            if line.startswith(u'其它') or len(line) == 0:
                continue

            # use "+" for split, "=" for header falg
            lineList = line.split(u'+', 1)
            if lineList[0].endswith(u'='):
                headers = lineList[0][:-1]
                originDic[headers] = lineList[1]
            else:
                originDic[headers] += lineList[0]
    return originDic

def genDict(oriDic):
    ''' eg: "十三元平": "言园源原喧轩翻繁元垣猿援[引也]萱 '''
    yunDic = {}
    for (header, conts) in oriDic.items():
        (yun, sheng) = (header[:-1], header[-1])

        #print(cont.decode("utf-8"))
        print("-- origin: %s" % conts)
        cLen = len(conts)
        idx, start = 0, -1
        while idx < cLen:
            note = ''
            if idx+1 < cLen and conts[idx+1] == u'[':
                start = idx+2   # read for read notes
                while conts[start] != u']':
                    note += conts[start]
                    start += 1
                print("%d: %s<%s> " % (idx, conts[idx], note))
            else:
                print("%d: %s " % (idx, conts[idx])),

            # write to dict
            if conts[idx] not in yunDic:
                yunDic[conts[idx]] = []
            yunDic[conts[idx]].append([sheng, yun, note])
            if idx < start:
                idx = start + 1
            else:
                idx += 1
        print()
    return yunDic


if __name__ == '__main__':
    fName = checkFile(sys.argv)
    oriDic = readFile(fName)
    with open("./data/oriYunDict.json", 'w+') as fd:
        fd.write(json.dumps(oriDic, ensure_ascii=False, indent=4))

    baseDic = genDict(oriDic)
    with open("./data/baseCharDict.json", 'w+') as fd:
        fd.write(json.dumps(baseDic, ensure_ascii=False))

