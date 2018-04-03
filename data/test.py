#! /usr/bin/python 
#encoding:gb18030
############################################
#
# Author: 
# E-Mail:@sogou-inc.com
# Create time: 2018 1月 30 15时23分10秒
# version 1.0
#
############################################

import numpy as np
import re
import itertools
from collections import Counter


filename="../data/all.image.bin"
dim=100
w2v = list(open(filename, "r").readlines())
w2v = [s.strip().split("\t") for s in w2v]
w2v = {s[0]:[float(x) for x in s[1:]] for s in w2v if len(s)==101}
for w in w2v:
    print w
idmap = dict()
idmap["<FIL/>"]=0
w2vlst = []
w2vlst.append([0.0]*100)
idmap["<PAD/>"]=1
w2vlst.append([0.0]*100)
ind=2
for k in w2v:
    idmap[k]=ind
    ind = ind + 1
    w2vlst.append(w2v[k])


