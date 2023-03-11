"""
File: rm_to_path.py
Description: This script copies files from a source folder and pastes them into two destination folders.
"""

import subprocess
from datetime import date
from pathlib import Path
from shutil import copy2

import pandas as pd


def main():
    """Entry point of the script."""
    try:
        # Define folder paths
        today = date.today()
        last_business_day = (pd.to_datetime(today) - pd.tseries.offsets.BDay(1)).date()
        last_business_day_str = last_business_day.strftime("%Y%m%d")
        year = last_business_day.year
        month = last_business_day.strftime("%B")
        rm_folder = Path(f"F:/Portia/RiskMetricsProd/{last_business_day_str}")
        rm_reports_folder = Path(f"F:/Risk/Market Risk/Liquidity/Systems/Process setup/FTP Reports - Prod/{year}/{month}/{last_business_day_str}")
        rm_input_output_folder = Path(f"F:/Risk/Market Risk/Liquidity/Systems/Process setup/Input_Output Files/{year}/{month}/{last_business_day_str}")
        
        # Create folders if they do not exist
        for folder in [rm_reports_folder, rm_input_output_folder]:
            folder.mkdir(parents=True, exist_ok=True)
            
        # Copy files
        for file in [
            "JOH.{}.IssueDetail.zip",
            "JOH.{}.IssueDetail.zip.cntl",
            "JOH.{}.LiquidityMetrics_Diagnostic_ESMA.zip",
            "JOH.{}.LiquidityMetrics_Diagnostic_ESMA.zip.cntl",
            "JOH.{}.LiquidityMetrics_Dashboard_ESMA.zip",
            "JOH.{}.LiquidityMetrics_Dashboard_ESMA.zip.cntl",
            "JOH.{}.LiquidityMetrics3_Diagnostic.zip",
            "JOH.{}.LiquidityMetrics3_Diagnostic.zip.cntl",
            "JOH.{}.LiquidityMetrics3_Summary.zip",
            "JOH.{}.LiquidityMetrics3_Summary.zip.cntl",
        ]:
            copy2(rm_folder / file.format(last_business_day_str), rm_reports_folder)
            
        for file in [
            "JOH.{}.output.rml",
            "JOH.{}.positionDetail.csv",
            "TNC.JOH.{}-{}.txt",
            "HLD.JOH.{}-{}.txt",
            "JOH_INSIGNIS.{}-{}.cntl",
            "JOH.{}.meta.xml",
            "JOH.{}.repcntl",
            "PTR.JOH.{}-{}.txt",
        ]:
            copy2(rm_folder / file.format(last_business_day_str, last_business_day_str), rm_input_output_folder)

        print("RM outputs reports filed")
    except Exception as e:
        print
