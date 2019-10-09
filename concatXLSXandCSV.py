#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:11:45 2019

@author: Moacyr Rodrigues Neto
"""


import sys
import pandas as pd

if len(sys.argv) != 5:
    print("\n {} <PATH> <RESULT FILE NAME> <FILE1> <FILE2>\n".format(sys.argv[0]))
    sys.exit()

path_name = str(sys.argv[1])
if not path_name.endswith('/'):
    path_name += '/'
output_file_name = path_name + str(sys.argv[2])
file_name1 = str(sys.argv[3])
file_name2 = str(sys.argv[4])


def createDataFrames(path, file1, file2):
    file_name_1 = path + file1
    file_name_2 = path + file2
    
    if file1.lower().endswith('.xlsx'):
        df_1 = pd.read_excel(file_name_1)
    elif file1.lower().endswith('.csv'):
        df_1 = pd.read_csv(file_name_1)
    
    if file2.lower().endswith('.xlsx'):
        df_2 = pd.read_excel(file_name_2)
    elif file2.lower().endswith('.csv'):
        df_2 = pd.read_csv(file_name_2)
    
    return concatenatedDataFrames(df_1, df_2)
    

def concatenatedDataFrames(*args):
    frames = args
    return pd.concat(frames)


def generateOutputFile(output_file, data):
    output_file += '.xlsx'
    data.to_excel(output_file, index=False)


concatslsx = createDataFrames(path_name, file_name1, file_name2)

generateOutputFile(output_file_name, concatslsx)

sys.exit()
