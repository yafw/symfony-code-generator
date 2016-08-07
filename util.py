#!/bin/python3

import os

def firstToUpper(name):
    # return new string with uppercase first letter
    return "%s%s" % (name[0].upper(), name[1:])

def readFile(path):
    with open(path, 'r') as f:
        content = f.read()
    return content

def createFile(path, content):
    path = "%s/%s" % (findSrc(), path)
    with open(path, 'w') as f:
        f.write(content)

def findSrc():
    current_dir = os.getcwd()
    while True:
        if 'src' in os.listdir(current_dir):
            return current_dir
        current_dir = '/'.join(current_dir.split('/')[:-1])

def createDirs(path):
    left_part = findSrc()
    right_part = path.split('/')[:-1]
    for directory in right_part:
        left_part = "%s/%s" % (left_part, directory)
        try:
            os.mkdir(left_part)
        except:
            continue
