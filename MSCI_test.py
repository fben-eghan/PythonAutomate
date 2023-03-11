import os
from datetime import datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd


def calculate_msci_index_level(cad_usd_rate, data_file_path, insignis_file_path_format, tnc_file_path_format,
                                search_texts, date_format='%Y%m%d'):
    # Replace search texts in data file
    with open(data_file_path) as f:
        contents = f.read()
    for search_text, replace_text in search_texts:
        contents = contents.replace(search_text, replace_text)
    with open(data_file_path, "w") as f:
        f.write(contents)

    # Create empty insignis file
    insignis_file_path = insignis_file_path_format.format(datetime.today().strftime(date_format))
    Path(insignis_file_path).touch()

    # Create TNC file
    tnc_file_path = tnc_file_path_format.format((datetime.today() - timedelta(days=1)).strftime(date_format))
    with open('TNC.JOH.PROD.YYYYMMDD-YYYYMMDD.txt', 'r') as f:
        text = f.read()
    newtext = text.replace('"', '').replace(',', '|')
    with open(tnc_file_path, 'w') as f:
        f.write(newtext)

    # Read TNC file into a pandas dataframe
    df = pd.read_csv(tnc_file_path, sep='|', header=None, skiprows=1)

    # Set column names
    df.columns = ['InstrumentCode', 'PortfolioCode', 'Model', 'TNC',
                  'Return Contribution Local', 'Risk Contribution Local',
                  'Return Contribution Base', 'Risk Contribution Base',
                  'LocalAccruedIncome', 'LocalAccruedIncomeValue', 'BaseAccruedIncome',
                  'BaseAccruedIncomeValue', 'LocalMarketValue', 'LocalMarketValueCurrency',
                  'BaseMarketValue', 'BaseMarketValueCurrency', 'FXRate',
                  'MarketValue USD', 'Unknown1', 'Unknown2', 'Unknown3']

        # Remove rows with 'BloombergTicker' as InstrumentCode
        df = df[~df.InstrumentCode.isin(['BloombergTicker'])]

        # Keep only rows with BaseMarketValueCurrency as CAD
        df = df[df.BaseMarketValueCurrency == 'CAD']

        # STEP 9: Convert TNC column to numeric
        df['TNC'] = pd.to_numeric(df['TNC'], errors='coerce')

        # Calculate total TNC
        total_tnc = df.TNC.sum()

        # Calculate MSCI index level
        msci_index_level = cad_usd_rate * total_tnc

        # STEP 10: Write MSCI index level to file and print message
        with open(insignis_file_path, 'w') as f:
            f.write(f'{yesterday_str}   {msci_index_level:.2f}\n')
        print(f'MSCI Index Level is {msci_index_level}')
        print(f'Index file {insignis_file_path} has been generated')
