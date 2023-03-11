# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 12:07:16 2022
    
@author: fben-eghan
"""
def RMtoMSCI(CADUSDRATE):
#CAD-USD X-RATE Curncy in Bloomberg for BD-1 as function argument    
    import pandas as pd
    # Importing FileInput from fileinput module
    from fileinput import FileInput
      
    # Creating a function to
    # replace the text
    def replacetext(search_text, replace_text):
      
        # Opening file using FileInput
        with FileInput(r'F:\Portia\HLD.JOH.PROD.YYYYMMDD-YYYYMMDD.txt', inplace=True) as f:
      
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
    
    # Define the list of search and replace text
    text_list = [
        (f'"{lb2}","","USD","Equity"', f'"{lb2}","0.000000000001","USD","Equity"'),
        (f'"{lb2}","","GBP","Equity"', f'"{lb2}","0.000000000001","GBP","Equity"'),
        (f'"{lb2}","","RUR","Equity"', f'"{lb2}","0.000000000001","RUR","Equity"')
    ]

    # Iterate over the list and call the replacetext function for each item
    for search_text, replace_text in text_list:
        print(replacetext(search_text, replace_text))

    
        #HIGLIGHT FROM HERE 
    import re
    import os
    import subprocess
    from datetime import date
    from shutil import copyfile, copy2, move

    import numpy as np
    import pandas as pd


    ### STEP 1
    def get_keys_dict(d):
        return [key for key in d]


    ### STEP 2 TO CREATE BLANK INSIGNIS FILE
    today = pd.datetime.today().date()
    yesterday = (today - pd.tseries.offsets.BDay(1)).strftime('%Y%m%d')
    title = f"JOH_INSIGNIS.{yesterday}.cntl"
    open(title, 'a').close()


    ### STEP 3 Run RiskMetricsTNC for one previous business day
    yesterday_str = (today - pd.tseries.offsets.BDay(1)).strftime('%d-%m-%y')

    with open('TNC.JOH.PROD.YYYYMMDD-YYYYMMDD.txt', 'r') as f:
        text = f.readlines()

    newtext = [line.replace('"', '').replace(',', '|') for line in text]

    title = f"TNC.JOH.{yesterday}.txt"
    with open(title, 'w') as f:
        f.writelines(newtext)  

    os.remove('TNC.JOH.PROD.YYYYMMDD-YYYYMMDD.txt')

    
    
    
    import pandas as pd
    import numpy as np

    # STEP 4
    bd_T1 = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%d-%m-%y')
    date = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%Y%m%d')

    new_lines = []
    with open(r'F:\Portia\HLD.JOH.PROD.YYYYMMDD-YYYYMMDD.txt') as file:
        lines = file.readlines()
        first_line = lines[0]
        first_line = first_line.replace('BaseAccruedIncome', 'BaseAccruedIncomeValue')
        first_line = first_line.replace('LocalAccruedIncome', 'LocalAccruedIncomeValue')
        first_line = first_line.replace('BaseMarketValueCurr', 'BaseMarketValueCurrency')
        first_line = first_line.replace('LocalMarketValueCur', 'LocalMarketValueCurrency')
        first_line = first_line.replace('\"', '')
        first_line = first_line.replace(',', '|')
        new_lines.append(first_line)

        cash_dict = {}
        cash_check = {}
        for line in lines[1:]:
            fields = line.split(',')
            if len(cash_dict) == 0: 
                if fields[6][1:-1] != 'Cash':
                    new_line = line.replace('\"', '')
                    new_line = new_line.replace(',', '|')
                    new_lines.append(new_line)
                else:
                    cash_dict[fields[1][1:-1]] = [(fields[3], fields[19])]
            elif list(cash_dict.keys())[-1] == fields[1][1:-1]:
                if fields[6][1:-1] != 'Cash':
                    new_line = line.replace('\"', '')
                    new_line = new_line.replace(',', '|')
                    new_lines.append(new_line)
                else:
                    cash_dict[fields[1][1:-1]].append((fields[3], fields[19]))
            elif list(cash_dict.keys())[-1] != fields[1][1:-1]:
                if fields[1][1:-1] not in cash_check:
                    cashamt = [np.float(i[1]) for i in cash_dict[list(cash_dict.keys())[-1]]]
                    if list(cash_dict.keys())[-1] != 'SEICIEF':
                        new_line = '{}|{}|{}|{}|Cash||Cash|CASH {}|{}|LOCALID|{}|||||0||0|0.00|{}||0.00|{}||{}|{}

    
    
    
   
    
    

            ### STEP 5
        import os
        import shutil
        from pathlib import Path
        import pandas as pd

        def create_folder():
            lb2 = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%Y%m%d')
            lb3 = (pd.datetime.today() - pd.tseries.offsets.BDay(2)).date().strftime('%Y%m%d')

            newpath = Path(r'F:\Portia\RiskMetricsProd') / lb2
            newpath.mkdir(parents=True, exist_ok=True)
            shutil.move(r'F:\Portia\TNC.JOH.{}-{}.txt'.format(lb2, lb2), newpath)
            shutil.move(r'F:\Portia\HLD.JOH.{}-{}.txt'.format(lb2, lb2), newpath)
            shutil.move(r'F:\Portia\JOH_INSIGNIS.{}-{}.cntl'.format(lb2, lb2), newpath)

            oldpath = Path(r'F:\Portia\RiskMetricsProd') / lb3
            shutil.copy2(oldpath / f'JOH.{lb3}.meta.xml', newpath)
            shutil.copy2(oldpath / f'JOH.{lb3}.repcntl', newpath)
            shutil.copy2(oldpath / f'PTR.JOH.{lb3}-{lb3}.txt', newpath)

            os.rename(newpath / f'JOH.{lb3}.meta.xml', newpath / f'JOH.{lb2}.meta.xml')
            os.rename(newpath / f'JOH.{lb3}.repcntl', newpath / f'JOH.{lb2}.repcntl')
            os.rename(newpath / f'PTR.JOH.{lb3}-{lb3}.txt', newpath / f'PTR.JOH.{lb2}-{lb2}.txt')

            return "Ready to FTP to MSCI"

