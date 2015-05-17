# -*- coding: utf-8 -*-
"""
Created on Tue Dec 30 20:23:51 2014

@author: anantsalame
"""

import string
import sys
import re
word_counts = {}

for line in sys.stdin:
    data = line.strip().split(" ")    
    for i in data:
        #logging.info(i)
        i=re.sub("[#!@$%^&*()_+-=,.:']",'',i)
        i = i.lower()
        if(i in word_counts):
            word_counts[i] = word_counts[i]+1
        else:
            word_counts[i]=1
        #logging.info(word_counts)
print(word_counts)