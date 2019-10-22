'''
Assistant functions for use by data_maker.py
Contains functions for clearing duplicate files, undoing last save made by the user,
coutning the toal files of each label and finding the final label number for each label.
Duplicates are found and removed by comparing their md5 checksums.
'''

import hashlib
import os
from collections import defaultdict


def md5(fName):
    hash_md5 = hashlib.md5()
    with open(fName, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def clear_dupes(filePath):
    stored = []
    for fileName in os.listdir(filePath):
        hash_md5 = md5(filePath + fileName)

        if hash_md5 not in stored:
            stored.append(hash_md5)
        else:
            os.remove(filePath + fileName)


def undo(fileStack):
    for fileName in fileStack:
        try:
            os.remove(fileName)
        except:
            break


def countFiles(filePath):
    count = defaultdict(int)
    for fileName in os.listdir(filePath):
        count[fileName.split('_')[0]] += 1
    # print(count)
    return count


def findFinalNumber(filePath):
    count = defaultdict(int)
    for fileName in os.listdir(filePath):
        num = int(fileName.split('_')[1].split('.')[0])
        if num > count[fileName.split('_')[0]]:
            count[fileName.split('_')[0]] = num
    # print(count)
    return count
