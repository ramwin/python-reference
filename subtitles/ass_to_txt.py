#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-01-17 22:07:20

import ass
import sys

ass_file_path = sys.argv[1]
txt_file_path = sys.argv[2]
def filter(text):
    
    
def main(doc,stylegrep=False):
    '''a function to change the ass doc object to text'''
    text = ''
    for i in doc.events:
        if not stylegrep:
            text = text +  i.text + '\n'
        else:
            text = text + filter(i.text) + '\n'
    return text

if __name__=='__main__':
    doc = ass.parse(open(ass_file_path))
    text = main(doc, stylegrep=False)
    save_file_path = open(txt_file_path,'w')
    print(type(text))
    save_file_path.write(text)
    save_file_path.close()
