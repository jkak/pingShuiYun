#!/bin/bash

dir=$(cd $(dirname $0); pwd)
cd $dir

if [ $# -ne 1 ];then
    echo "usage $0 [start|stop|status]"
    exit 1
fi

if [ "$1"  == "start" ];then
    nohup python yunServer.py data/baseCharDict.json 1>>out 2>>err &
    echo "started..."
elif [ "$1"  == "stop" ];then
    ps axu | grep yunServer.py | grep -v grep  | awk '{print $2}' | xargs kill -9
    echo "stoped..."
elif [ "$1" == "status" ];then
    ps axu | grep yunServer.py | grep -v grep
    if [ "$?" -eq 0 ];then
        echo -e "\nstarted...\n"
    else
        echo -e "\nstoped...\n"
    fi
fi
