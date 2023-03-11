# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 12:07:16 2022
    
@author: fben-eghan
"""

import os
import subprocess
from datetime import date
from shutil import copyfile, copy2, move

import numpy as np
import pandas as pd
import re


def RMtoMSCI(CADUSDRATE):
    # STEP 1: Remove unused imports

    # STEP 2: Simplify replacetext function

    def replacetext(file_path, search_text, replace_text):
        # Open file in read mode
        with open(file_path, "r") as f:
            # Read contents of file
            contents = f.read()
        # Replace search_text with replace_text in contents
        new_contents = contents.replace(search_text, replace_text)
        # Open file in write mode and write new_contents to it
        with open(file_path, "w") as f:
            f.write(new_contents)
        # Return "Text replaced" string
        return "Text replaced"

    # STEP 3: Use f-strings for readability and avoid magic numbers

    # Define file paths
    data_file_path = r"F:\Portia\HLD.JOH.PROD.YYYYMMDD-YYYYMMDD.txt"
    insignis_file_path = f"JOH_INSIGNIS.{pd.datetime.today().strftime('%Y%m%d')}.cntl"
    tnc_file_path = f"TNC.JOH.{(pd.datetime.today() - pd.tseries.offsets.BDay(1)).strftime('%Y%m%d')}.txt"

    # Define search and replace texts
    search_texts = [
        (f'"{yesterday}","","USD","Equity"', f'"{yesterday}","0.000000000001","USD","Equity"'),
        (f'"{yesterday}","","GBP","Equity"', f'"{yesterday}","0.000000000001","GBP","Equity"'),
        (f'"{yesterday}","","RUR","Equity"', f'"{yesterday}","0.000000000001","RUR","Equity"')
    ]

    # STEP 4: Replace search_texts in data_file_path

    # Iterate over search_texts and call replacetext function for each item
    for search_text, replace_text in search_texts:
        print(replacetext(data_file_path, search_text, replace_text))

    # STEP 5: Remove unused imports and update date calculation

    # Previous business day in YYYYMMDD format
    yesterday = (pd.datetime.now() - pd.tseries.offsets.BDay(1)).strftime('%Y%m%d')

    # STEP 6: Create blank insignis file

    open(insignis_file_path, 'a').close()

    # STEP 7: Run RiskMetricsTNC for one previous business day

    yesterday_str = (pd.datetime.now() - pd.tseries.offsets.BDay(1)).strftime('%d-%m-%y')

    with open('TNC.JOH.PROD.YYYYMMDD-YYYYMMDD.txt', 'r') as f:
        text = f.read()

    newtext = text.replace('"', '').replace(',', '|')

    with open(tnc_file_path, 'w') as f:
        f.write(newtext)

    os.remove('TNC.JOH.PROD.YYYYMMDD-YYYYMMDD.txt')

    # STEP 8
    tnc_file = f"TNC.JOH.{date}.txt"
    df = pd.read_csv(tnc_file, sep='|', header=None, skiprows=1)

    df.columns = ['InstrumentCode', 'PortfolioCode', 'Model', 'TNC',
                  'Return Contribution Local', 'Risk Contribution Local',
                  'Return Contribution Base', 'Risk Contribution Base',
                  'LocalAccruedIncome', 'LocalAccruedIncomeValue', 'BaseAccruedIncome',
                  'BaseAccruedIncomeValue', 'LocalMarketValue', 'LocalMarketValueCurrency',
                  'BaseMarketValue', 'BaseMarketValueCurrency', 'FXRate',
                  'MarketValue USD', 'Unknown1', 'Unknown2', 'Unknown3']

    df = df[~df.InstrumentCode.isin(['BloombergTicker'])]

    df = df[df.BaseMarketValueCurrency == 'CAD']

    # STEP 9
    df['TNC'] = pd.to_numeric(df['TNC'], errors='coerce')

    total_tnc = df.TNC.sum()

    msci_index_level = CADUSDRATE * total_tnc

    # STEP 10
    print(f'MSCI Index Level is {msci_index_level}')

    with open('JOH_INSIGNIS.XYZ.txt', 'w') as f:
        f.write(f'{bd_T1}   {msci_index_level:.2f}\n')

    print('Index file JOH_INSIGNIS.XYZ.txt has been generated')

