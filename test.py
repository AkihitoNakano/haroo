# -*- coding: utf-8 -*-
"""
Created on Mon May 29 16:01:46 2017

@author: mysurface
"""
import pandas as pd

date_parser = lambda x: pd.datetime.strptime(x, '%Y-%m-%d')
df = pd.read_csv('test.csv', parse_dates=['ymd'], date_parser=date_parser, index_col=0)

df.reset_index(inplace=True)
df['ymd'] = df['ymd'].apply(lambda x: x.year if x.month > 2 else x.year - 1)
df.set_index(['ymd'], inplace=True)

print(df.groupby(lambda x: x).sum())