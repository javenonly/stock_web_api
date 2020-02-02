#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import globalvar as gl

gl._init()

# 数据基准日（文件夹）
gl.set_value('var_date', '20200123')
# gl.set_value('stock_data_path', 'C:\\stock_data\\')
gl.set_value('stock_data_path', '/Users/shawn/Documents/stock_web/stock_data/')
gl.set_value('df_all_code_file', 'all_code.csv')