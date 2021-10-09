#!/usr/bin/python3

from operator import itemgetter
import sys


curr_word = None
curr_cnt = 0
word = None


for line in sys.stdin:
    
    line = line.strip()
    
    word, count = line.split()
    
    try:
        count = int(count)
    except:
        continue
        
    if curr_word == word:
        curr_cnt += count
    else:
        if curr_word:
            print(curr_word, curr_cnt)
            
        curr_cnt = count
        curr_word = word
        
if curr_word == word:
    print(curr_word, curr_cnt)
