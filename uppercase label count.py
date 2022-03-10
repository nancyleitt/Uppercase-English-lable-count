
import string
from string import punctuation
from nltk import word_tokenize
import os
import numpy as np
import re
import xlwt
from openpyxl import Workbook
from openpyxl import load_workbook

student_files = [doc for doc in os.listdir(r"C:\Users\86157\Desktop\test") if doc.endswith('.txt')]
print(student_files)

for _file in student_files:
    read_data = open(r"C:\Users\86157\Desktop\test\\"+_file,encoding='utf-8').read()
    a = read_data.split()

    def removePunctuation(read_data):
        '''去掉字符串中标点符号
        '''
    temp = []
    for a in read_data:
      if a not in string.punctuation:
        temp.append(a)
        newText = ''.join(temp)
        add_punc = '，。、【】“”：；（）《》‘’{}？！⑦()、%^>℃：.”“^-——=擅长于的&#@￥'  # 自定义--中文的字符
        all_punc = punctuation + add_punc
        temp_1 = []
        for b in newText:
          if b not in all_punc:
            temp_1.append(b)
        newText_1 = ''.join(temp_1)
        word = word_tokenize(newText_1)

        word_group = {}
        for i in word:
          if word.count(i) >= 1:
            word_group[i] = word.count(i)
    print(word_group)

    print(word_group.get('GM'))
    print(word_group.get('LM'))
    print(word_group.get('FM'))
    print(word_group.get('DM'))

