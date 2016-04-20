# coding: utf-8
import re
srt_file_name = './S08E20.srt'
txt_file_name = './S08E20.txt'
srt = open(srt_file_name,'r')
sub_text_list = re.split('\s*[0-9]*[\r]*\n[0-9:,]*\s*-->\s*[0-9:,]*\s*',srt.read())
print(len(sub_text_list))
file = open(txt_file_name,'w')
file.write('\n'.join(sub_text_list))
