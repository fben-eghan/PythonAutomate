# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 16:21:21 2022

@author: fben-eghan
"""

#HIGLIGHT FROM HERE 
import re
from os import remove
from shutil import move
import os
import win32com.shell.shell as shell
import win32event
import win32com
from win32com import client
import subprocess
import time
import pandas as pd
import numpy as np
from datetime import date
from shutil import copyfile, copy2
import datetime
import shutil

#Files away the output from RiskMetrics

lb2 = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%Y%m%d')
lb3 = (pd.datetime.today() - pd.tseries.offsets.BDay(2)).date().strftime('%Y%m%d')
y = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).year
m = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%B')

rm1 = r'F:\Risk\Market Risk\Liquidity\Systems\Process setup\FTP Reports - Prod\{}\{}\{}'.format(y, m, lb2)
rm2 = r'F:\Risk\Market Risk\Liquidity\Systems\Process setup\Input_Output Files\{}\{}\{}'.format(y, m, lb2)

os.makedirs(rm1)
os.makedirs(rm2)

newpath = r'F:\Portia\RiskMetricsProd\{}'.format(lb2)

copy2(newpath+'\JOH.{}.IssueDetail.zip'.format(lb2), rm1)
copy2(newpath+'\JOH.{}.IssueDetail.zip.cntl'.format(lb2), rm1)
copy2(newpath+'\JOH.{}.LiquidityMetrics_Diagnostic_ESMA.zip.cntl'.format(lb2), rm1)
copy2(newpath+'\JOH.{}.LiquidityMetrics_Diagnostic_ESMA.zip'.format(lb2), rm1)
copy2(newpath+'\JOH.{}.LiquidityMetrics_Dashboard_ESMA.zip.cntl'.format(lb2), rm1)
copy2(newpath+'\JOH.{}.LiquidityMetrics_Dashboard_ESMA.zip'.format(lb2), rm1)
copy2(newpath+'\JOH.{}.LiquidityMetrics3_Diagnostic.zip.cntl'.format(lb2), rm1)
copy2(newpath+'\JOH.{}.LiquidityMetrics3_Diagnostic.zip'.format(lb2), rm1)
copy2(newpath+'\JOH.{}.LiquidityMetrics3_Summary.zip.cntl'.format(lb2), rm1)
copy2(newpath+'\JOH.{}.LiquidityMetrics3_Summary.zip'.format(lb2), rm1)

copy2(newpath+'\JOH.{}.output.rml'.format(lb2), rm2)
copy2(newpath+'\JOH.{}.positionDetail.csv'.format(lb2), rm2)
copy2(newpath+'\TNC.JOH.{}-{}.txt'.format(lb2, lb2), rm2) 
copy2(newpath+'\HLD.JOH.{}-{}.txt'.format(lb2, lb2), rm2) 
copy2(newpath+'\JOH_INSIGNIS.{}-{}.cntl'.format(lb2, lb2), rm2)
copy2(newpath+'\JOH.{}.meta.xml'.format(lb2), rm2)
copy2(newpath+'\JOH.{}.repcntl'.format(lb2), rm2)
copy2(newpath+'\PTR.JOH.{}-{}.txt'.format(lb2, lb2), rm2)

print('RM outputs reports filed')
