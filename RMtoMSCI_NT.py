# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 15:22:53 2022

@author: fben-eghan
"""
def RMtoMSCI_NT(CADUSDRATE):    
#CAD-USD X-RATE Curncy in Bloomberg for BD-1 as function argument  
    
    #CAD-USD X-RATE Curncy in Bloomberg for BD-1 as function argument    
    import pandas as pd
    # Importing FileInput from fileinput module
    from fileinput import FileInput
      
    # Creating a function to
    # replace the text
    def replacetext(search_text, replace_text):
      
        # Opening file using FileInput
        with FileInput(r'F:\Portia\HLD.JOH.PROD.YYYYMMDD-YYYYMMDD_NT.txt', inplace=True) as f:
      
            # Iterating over every and changing
            # the search_text with replace_text
            # using the replace function
            for line in f:
                print(line.replace(search_text,
                                   replace_text), end='')
      
        # Return "Text replaced" string
        return "Text replaced"
     
        
    # Previous business day in YYYYMMDD format
    lb2 = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%Y%m%d')
    
    # Creating a variable and storing
    # the text that we want to search
    search_text = r'"{}","","USD","Equity"'.format(lb2) 
      
    # Creating a variable and storing
    # the text that we want to update
    replace_text = r'"{}","0.000000000001","USD","Equity"'.format(lb2) 
      
    # Calling the replacetext function
    # and printing the returned statement
    print(replacetext(search_text, replace_text))
    
    search_text = r'"{}","","GBP","Equity"'.format(lb2) 
      
    # Creating a variable and storing
    # the text that we want to update
    replace_text = r'"{}","0.000000000001","GBP","Equity"'.format(lb2) 
      
    # Calling the replacetext function
    # and printing the returned statement
    print(replacetext(search_text, replace_text))
    
    search_text = r'"{}","","RUR","Equity"'.format(lb2) 
      
    # Creating a variable and storing
    # the text that we want to update
    replace_text = r'"{}","0.000000000001","RUR","Equity"'.format(lb2) 
      
    # Calling the replacetext function
    # and printing the returned statement
    print(replacetext(search_text, replace_text))
    
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
    
    ### STEP 1
    def getList(j):
        l = []
        for key in j:
            l.append(key)
        return(l)
    
    
    ### STEP 2 TO CREATE BLANK INSIGNIS FILE
    titledate = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%Y%m%d')
    title = titledate+'-'+titledate
    open(r'F:\Portia\JOH_INSIGNIS.UAT.{}.cntl'.format(title), 'a').close()
    
        
    
    ### STEP 3 Run -RiskMetricsTNC for one previous business day
    bd_T1 = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%d-%m-%y')
    
    newtext = []
    test = open(r'F:\Portia\TNC.JOH.PROD.YYYYMMDD-YYYYMMDD_NT.txt').readlines()
    
    for line in test:
        line1 = line.replace('\"', '')
        newtext.append(line1.replace(',', '|'))
    
    titledate = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%Y%m%d')
    title = titledate+'-'+titledate
    
    with open(r'F:\Portia\TNC.JOH.UAT.{}.txt'.format(title), 'w') as output:
        for item in newtext:
            output.write(item)  
        
    os.remove(r'F:\Portia\TNC.JOH.PROD.YYYYMMDD-YYYYMMDD_NT.txt')
    
    
    
    ### STEP 4
    bd_T1 = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%d-%m-%y')
    date = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%Y%m%d')
    
    
    newtext = []
    test = open(r'F:\Portia\HLD.JOH.PROD.YYYYMMDD-YYYYMMDD_NT.txt').readlines()
    firstline = test[0]
    
    #firstline.replace('Contract for D', 'Contract for Difference') !!!!add this in a loop to check values when Robbie trades CFDs!!!!
    firstline = firstline.replace('BaseAccruedIncome',' BaseAccruedIncomeValue')
    firstline = firstline.replace('LocalAccruedIncome', 'LocalAccruedIncomeValue')
    firstline = firstline.replace('BaseMarketValueCurr', 'BaseMarketValueCurrency')
    firstline = firstline.replace('LocalMarketValueCur', 'LocalMarketValueCurrency')
    firstline = firstline.replace('\"', '')
    firstline = firstline.replace(',', '|')
    
       
    newtext.append(firstline)
    
    cashdict = {}
    cashcheck = {}
    for ind in range(1, len(test)):
        if len(cashdict.keys()) == 0: 
            if test[ind].split(',')[6][1:-1] != 'Cash':
                line1 = test[ind].replace('\"', '')
                newtext.append(line1.replace(',', '|'))
    
            elif test[ind].split(',')[6][1:-1] == 'Cash':
                try:
                    cashdict[test[ind].split(',')[1][1:-1]]
                except Exception:
                    cashdict[test[ind].split(',')[1][1:-1]] = [(test[ind].split(',')[3], test[ind].split(',')[19])]
                else:
                    cashdict[test[ind].split(',')[1][1:-1]].append((test[ind].split(',')[3], test[ind].split(',')[19]))
    
       
        elif getList(cashdict.keys())[-1] == test[ind].split(',')[1][1:-1]:
            if test[ind].split(',')[6][1:-1] != 'Cash':
                line1 = test[ind].replace('\"', '')
                newtext.append(line1.replace(',', '|'))
    
            elif  test[ind].split(',')[6][1:-1] == 'Cash':
                try:
                    cashdict[test[ind].split(',')[1][1:-1]]
                except Exception:
                    cashdict[test[ind].split(',')[1][1:-1]] = [(test[ind].split(',')[3], test[ind].split(',')[19])]
                else:
                    cashdict[test[ind].split(',')[1][1:-1]].append((test[ind].split(',')[3], test[ind].split(',')[19]))
    
            
        elif getList(cashdict.keys())[-1] != test[ind].split(',')[1][1:-1]:
            try:
                cashcheck[test[ind].split(',')[1][1:-1]]
            except Exception:
                
                cashamt = []
                for i in cashdict[getList(cashdict.keys())[-1]]:
                    cashamt.append(np.float(i[1]))
                
                if  getList(cashdict.keys())[-1] != 'SEICIEF':
                    line1 = '{}|{}|{}|{}|Cash||Cash|CASH {}|{}|LOCALID|{}|||||0||0|0.00|{}||0.00|{}||{}|{}|{}|1.|{}|Cash||||||\n'.format(
                                                                                                    date, getList(cashdict.keys())[-1], getList(cashdict.keys())[-1],
                                                                                                    cashdict[getList(cashdict.keys())[-1]][0][0][1:-1], 
                                                                                                    cashdict[getList(cashdict.keys())[-1]][0][0][1:-1],
                                                                                                    cashdict[getList(cashdict.keys())[-1]][0][0][1:-1],
                                                                                                    cashdict[getList(cashdict.keys())[-1]][0][0][1:-1],
                                                                                                    np.sum(cashamt), np.sum(cashamt), cashdict[getList(cashdict.keys())[-1]][0][0][1:-1],
                                                                                                    cashdict[getList(cashdict.keys())[-1]][0][0][1:-1], date,
                                                                                                    cashdict[getList(cashdict.keys())[-1]][0][0][1:-1])
                    newtext.append(line1)
                    cashcheck[test[ind].split(',')[1][1:-1]] = 1
                
                elif getList(cashdict.keys())[-1] == 'SEICIEF':
                    line1 = '{}|{}|{}|{}|Cash||Cash|CASH USD|USD|LOCALID|USD|||||0||0|0.00|{}||0.00|{}||CAD|USD|{}|1.|USD|Cash||||||\n'.format(
                                                                                                    date, 
                                                                                                    getList(cashdict.keys())[-1], 
                                                                                                    getList(cashdict.keys())[-1], 
                                                                     
                                                                                                    cashdict[getList(cashdict.keys())[-1]][0][0][1:-1],
                                                                                                    np.sum(cashamt), 
                                                                                                    np.sum(cashamt)*CADUSDRATE, 
                                                                                                    date)
                                                                                                   
                    newtext.append(line1)
                    cashcheck[test[ind].split(',')[1][1:-1]] = 1
            
            else:
                pass
            
            
            if test[ind].split(',')[6][1:-1] != 'Cash':
                line1 = test[ind].replace('\"', '')
                newtext.append(line1.replace(',', '|'))
    
            elif  test[ind].split(',')[6][1:-1] == 'Cash':
                try:
                    cashdict[test[ind].split(',')[1][1:-1]]
                except Exception:
                    cashdict[test[ind].split(',')[1][1:-1]] = [(test[ind].split(',')[3], test[ind].split(',')[19])] #might be 22
                else:
                    cashdict[test[ind].split(',')[1][1:-1]].append((test[ind].split(',')[3], test[ind].split(',')[19]))
        
    cashamt = []
    for i in cashdict[getList(cashdict.keys())[-1]]:
        cashamt.append(np.float(i[1]))
    
    line1 = '{}|{}|{}|{}|Cash||Cash|CASH {}|{}|LOCALID|{}|||||0||0|0.00|{}||0.00|{}||{}|{}|{}|1.|{}|Cash||||||\n'.format(
                                                                                    date, getList(cashdict.keys())[-1], getList(cashdict.keys())[-1],
                                                                                    cashdict[getList(cashdict.keys())[-1]][0][0][1:-1], 
                                                                                    cashdict[getList(cashdict.keys())[-1]][0][0][1:-1],
                                                                                    cashdict[getList(cashdict.keys())[-1]][0][0][1:-1],
                                                                                    cashdict[getList(cashdict.keys())[-1]][0][0][1:-1],
                                                                                    np.sum(cashamt), np.sum(cashamt), cashdict[getList(cashdict.keys())[-1]][0][0][1:-1],
                                                                                    cashdict[getList(cashdict.keys())[-1]][0][0][1:-1], date,
                                                                                    cashdict[getList(cashdict.keys())[-1]][0][0][1:-1])
    newtext.append(line1)
    
            
    
                        
    titledate = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%Y%m%d')
    title = titledate+'-'+titledate
    
    with open(r'F:\Portia\HLD.JOH.UAT.{}.txt'.format(title), 'w') as output:
        for item in newtext:
            output.write(item)
            
    os.remove(r'F:\Portia\HLD.JOH.PROD.YYYYMMDD-YYYYMMDD_NT.txt')
    
    
    
    
    
    
    
    
    ### STEP 5
    #THIS CREATES A NEW FOLDER FOR BD-1 AND MOVES THE REQUIRED FILES APART FROM HOLDINGS
    #PASTE HOLDINGS OUTPUT FROM RISK HERE
    lb2 = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%Y%m%d')
    lb3 = (pd.datetime.today() - pd.tseries.offsets.BDay(2)).date().strftime('%Y%m%d')
    
    newpath = r'F:\Portia\NT\Parallel\Downstream_E2E\RiskMetrics\{}'.format(lb2) 
    os.makedirs(newpath)
    move(r'F:\Portia\TNC.JOH.UAT.{}-{}.txt'.format(lb2, lb2), newpath)
    move(r'F:\Portia\HLD.JOH.UAT.{}-{}.txt'.format(lb2, lb2), newpath) 
    move(r'F:\Portia\JOH_INSIGNIS.UAT.{}-{}.cntl'.format(lb2, lb2), newpath)
    
    oldpath = r'F:\Portia\NT\Parallel\Downstream_E2E\RiskMetrics\{}'.format(lb3)
    copy2(oldpath+'\JOH.UAT.{}.meta.xml'.format(lb3), newpath)
    copy2(oldpath+'\JOH.UAT.{}.repcntl'.format(lb3), newpath)
    copy2(oldpath+'\PTR.JOH.UAT.{}-{}.txt'.format(lb3, lb3), newpath)
    
    os.rename(newpath+'\JOH.UAT.{}.meta.xml'.format(lb3), newpath+'\JOH.UAT.{}.meta.xml'.format(lb2))
    os.rename(newpath+'\JOH.UAT.{}.repcntl'.format(lb3), newpath+'\JOH.UAT.{}.repcntl'.format(lb2))
    os.rename(newpath+'\PTR.JOH.UAT.{}-{}.txt'.format(lb3, lb3), newpath+'\PTR.JOH.UAT.{}-{}.txt'.format(lb2, lb2))
        
    return "Ready to FTP to MSCI UAT"

