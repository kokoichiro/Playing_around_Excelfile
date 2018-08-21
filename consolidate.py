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

def a_joiner(t_dir):
    all_data = pd.DataFrame()
    found = location_finder(t_dir)
    i = 0
#    for f in glob.glob(t_dir,recursive=True):
    for f in found:

        try:
            if 'xls' in str(f):
            	if i == 0:
            		d=pd.read_excel(f,quotechar='"')
            		columns_name=d.columns
                df = pd.read_excel(f,header=0,names=columns_name,quotechar='"')
                df2=df.assign(file_name=str(f))
                all_data = pd.concat([all_data,df2])
                i += 1

            elif 'csv' in str(f):
            	if i == 0:
            		d=pd.read_csv(f,quotechar='"')
            		columns_name=d.columns
                df = pd.read_csv(f,header=0,names=columns_name,quotechar='"')
                df2=df.assign(file_name=str(f))
                all_data = pd.concat([all_data,df2])
                i += 1
            else:
                pass

        except Exception as e:
            print(e,f)

        all_data = all_data.reset_index(drop=True)
    return all_data

if __name__=="__main__":
  argparser = argparse.ArgumentParser()
  argparser.add_argument('loc',help = 'Put location name.This location must include input and output folder.')
  args = argparser.parse_args()
  loc = args.loc
  search_dir=loc+'/input/'
  output_dir=loc+'/output/all_data.csv'
  df_all=a_joiner(search_dir)
  df_all.to_csv(output_dir,sep=',')

