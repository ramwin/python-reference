#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-01-17 22:07:20

import ass, sys, re

ass_file_path = sys.argv[1]
txt_file_path = sys.argv[2]

def assStypeGrep(text):
    text = ''.join(re.split(r'{[\s\S]*?}',text))
    text = text.replace('\\N','\n')
    return text
def main(doc,stylegrep=False):
    '''a function to change the ass doc object to text'''
    text = ''
    for i in doc.events:
        if stylegrep:
            text += assStypeGrep(i.text) +'\n'
        else:
            text += i.text + '\n'
    return text

if __name__=='__main__':
    doc = ass.parse(open(ass_file_path))
    text = main(doc, stylegrep=True)
    save_file_path = open(txt_file_path,'w')
    save_file_path.write(text)
