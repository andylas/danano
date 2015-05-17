# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 20:59:38 2014

@author: anantsalame
"""

filenames=['/Users/anantsalame/udacity/file1','/Users/anantsalame/udacity/file2','/Users/anantsalame/udacity/file3']
output_file="/Users/anantsalame/udacity/combined_file.txt"
with open(output_file, 'w') as master_file:
       master_file.write('C/A,UNIT,SCP,DATEn,TIMEn,DESCn,ENTRIESn,EXITSn\n')
       for filename in filenames:
           new_file = True
           with open(filename,'r') as slave_file:
               #slave_file.read()
               for line in slave_file:
                   if(new_file == True):
                       new_file = False
                       continue
                   else:
                       print(line)
                       #master_file.write(','.join(row))
                       master_file.write(line)
                   