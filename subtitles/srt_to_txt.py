#!/usr/bin/env python3
# coding: utf-8
# Xiang Wang @ 2016-01-17 22:07:20
import sys, re, srt

sub_file_path = sys.argv[1]
print('字幕文件名: %s'%(sub_file_path))
if len(sys.argv) == 3:
    txt_file_path = sys.argv[2]
elif len(sys.argv) == 2:
    txt_file_path = sub_file_path.replace('.srt','.txt')
print('输出文件: %s'%(txt_file_path))
    
    
def main(srt_text):
    return '\n'.join(map(lambda x: x.content, srt.parse(srt_text)))

if __name__=='__main__':
    srt_text = open(sub_file_path,'r').read()
    text = main(srt_text)
    save_file_path = open(txt_file_path,'w')
    save_file_path.write(text)
    save_file_path.close()
