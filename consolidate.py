#!/usr/bin/env python
# In[ ]:
#  coding: utf-8

import os
import glob2 as glob
import argparse
import pandas as pd
import os
import xlrd




def location_finder(search_dir):
    found = []
    
    for root, dirs, files in os.walk(search_dir):
        for filename in files:
            found.append(os.path.join(root, filename)) 
        for dirname in dirs:
            found.append(os.path.join(root, dirname))
    return found

def a_joiner(t_dir,columns_name):
    all_data = pd.DataFrame()
    found = location_finder(t_dir)
#    for f in glob.glob(t_dir,recursive=True):
    for f in found:
        try:
            if 'xls' in str(f):
                df = pd.read_excel(f,header=1,names=columns_name,quotechar='"')
                df2=df.assign(file_name=str(f))
                all_data = pd.concat([all_data,df2])
                print(f)

            elif 'csv' in str(f):
                df = pd.read_csv(f,header=1,names=columns_name,quotechar='"')
                df2=df.assign(file_name=str(f))
                all_data = pd.concat([all_data,df2])
                print(f)
            else:
                pass

        except Exception as e:
            print(e,f)
    return all_data

if __name__=="__main__":
  argparser = argparse.ArgumentParser()
  argparser.add_argument('loc',help = 'Put location name.This location needs to include input and output folder.')
  argparser.add_argument('col',help = 'Put columns_name list in csv file.')
  args = argparser.parse_args()
  loc = args.loc
  col = args.col
  search_dir=loc+'/input/'
  output_dir=loc+'/output/all_data.csv'
  df_all=a_joiner(search_dir,col)
  df_all.to_csv(output_dir,sep=',')

