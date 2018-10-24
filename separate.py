#!/usr/bin/env python
# In[ ]:
#  coding: utf-8

import os
import glob2 as glob
import argparse
import pandas as pd
import os
import xlrd

#location finder looks for the all files under 'search_dir'. Return all files list.
def location_finder(search_dir):
    found = []
    for root, dirs, files in os.walk(search_dir):
        for filename in files:
            found.append(os.path.join(root, filename)) 
        for dirname in dirs:
            found.append(os.path.join(root, dirname))
    return found

#a_joiner open all excels and csv files and consolidate them into one pandas data frame.
def a_splitter(t_dir,num_split):
    all_data = pd.DataFrame()
    f = t_dir
    
#    for f in glob.glob(t_dir,recursive=True):


    try:
        #if filename includes 'xls', we use read_excel. 
        if 'xls' in str(f):
            #get schema when the iteration is first one.
                d=pd.read_excel(f,quotechar='"')
            	columns_name=d.columns
            df = pd.read_excel(f,header=0,names=columns_name,quotechar='"')
            

            
            #if filename includes 'csv', we use read_excel.
        elif 'csv' in str(f):
            #get schema when the iteration is first one
            if i == 0:
            	d=pd.read_csv(f,quotechar='"')
            	columns_name=d.columns
            df = pd.read_csv(f,header=0,names=columns_name,quotechar='"')
            else:
                pass

        except Exception as e:
            print(e,f)
    sp=int(len(df)/num_split)

    for i in range(num_split):
        filename=loc+'/output/split_data_'+str(i)+'.csv'
        if i < num_split-1:       
            df_p = df.loc[sp*i:sp*(i+1)-1,:]
            
        if i ==  num_split -1:
            df_p = df.loc[sp*i:len(df)-1,:]
        df_p.to_csv(output_dir,sep=',')


if __name__=="__main__":
  argparser = argparse.ArgumentParser()
  argparser.add_argument('filename',help = 'Put file name.This location must include input and output folder.')
  argparser.add_argument('num_split',help = 'Put location name.This location must include input and output folder.')
  args = argparser.parse_args()
  search_dir = args.filename
  num_split=args.num_split
  a_splitter(search_dir,num_split)
  
