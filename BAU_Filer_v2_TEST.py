
def PxRemover():        
    import os

    files_to_remove = [
        r'F:\Portia\FTP\mpx.txt',
        r'F:\Portia\FTP\mpx2.txt',
        r'F:\Portia\FTP\dailypricesreturn2.txt',
        r'F:\Portia\FTP\fwdsdailyreturn.txt',
        r'F:\Portia\FTP\corpcoupons.txt',
        r'F:\Portia\FTP\fxdailyreturn.txt'
    ]

    for file_path in files_to_remove:
        try:
            os.remove(file_path)
            print(f'Removed {file_path}')
        except FileNotFoundError:
            pass


def backup():
    import os
    import shutil
    from datetime import date
    import pandas as pd
    feln = r'F:\IT\!! NEW IT\Data Admin\Data Administrators\Felix Notes'
    y = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).year
    
    files_to_backup = [
        r'F:\Portia\FTP\ManualPrices.xlsx',
        r'Q:\Rec\Cash Rec {}.xlsx'.format(y)
    ]

    for file_path in files_to_backup:
        try:
            shutil.copy2(file_path, r'H:')
            shutil.copy2(file_path, feln)
            print(f'{os.path.basename(file_path)} backed up')
        except FileNotFoundError:
            pass
        


def E2Ebak():
    import os
    import shutil
    import pandas as pd
    from datetime import date
    from shutil import copy2
    # These are the directories for the Import files
    files = [
        'BloombergAskPrices.txt',
        'BloombergMidPrices.txt',
        'BloombergFWDs.txt',
        'BloombergVotingShares.txt',
        'BloombergSharesOS.txt',
        'BloombergCorpPrices.txt',
        'BloombergBidPrices.txt',
        'BloombergFXs.txt',
        'BloombergPrices.txt'
    ]
    mpx = 'mpx.prn'
    mpx2 = 'mpx2.prn'
    lip = 'Currencies.prn'

    # Backup the Pricing and FX files for E2E Testing
    lb2 = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%Y%m%d')
    y = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).year
    m = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%B')

    spiv1 = os.path.join('F:\Portia\NT\Parallel\Backups', str(y), m, lb2, 'SPIV1')
    mbak = os.path.join('F:\Portia\NT\Parallel\Backups', str(y), m, lb2)

    os.makedirs(spiv1)

    for file in files:
        source = os.path.join('F:\Portia\FTP', file)
        copy2(source, spiv1)

    copy2(mpx, mbak)
    copy2(mpx2, mbak)
    copy2(lip, mbak)

    print('SPIV1, fx and mpx files backed up')

import os
import shutil
from datetime import date
from fileinput import FileInput

def Rpt_Filer():
    today = date.today()
    lb1 = today.strftime('%Y%m%d')
    lb2 = (today - pd.tseries.offsets.BDay(1)).strftime('%Y%m%d')
    lb3 = (today - pd.tseries.offsets.BDay(2)).strftime('%Y%m%d')
    m = today.strftime('%B')
    calibre = os.path.join(r'F:\Portia\Calibre', m, lb2)
    factset = os.path.join(r'F:\Portia\FactSet', m, lb2)
    
    shutil.move(r'F:\Portia\Russell APC Holding.csv', r'F:\IT\RUSSELLAPC\Russell APC Holding.csv')

    os.makedirs(calibre, exist_ok=True)
    os.makedirs(factset, exist_ok=True)

    for filename, newname in [
        ('portsnap_[date]_JOHCM.csv', f'portsnap_{lb2}_JOHCM.csv'),
        ('refval__[date]_JOHCM.csv', f'refval__{lb2}_JOHCM.csv'),
        ('JOHAM_T1_YYYYMMDD.txt', f'JOHAM_T1_{lb2}.txt'),
        ('JOHAM_T2_YYYYMMDD.txt', f'JOHAM_T2_{lb3}.txt'),
        ('joham_fx_YYYYMMDD.txt', f'joham_fx_{lb2}.txt'),
        ('_factset_fwd_T1_YYYYMMDD.txt', f'_factset_fwd_T1_{lb2}.txt'),
        ('_factset_fwd_T2_YYYYMMDD.txt', f'_factset_fwd_T2_{lb3}.txt'),
        ('_factset_hld_v2_T1_YYYYMMDD.txt', f'_factset_hld_v2_T1_{lb2}.txt'),
        ('_factset_hld_v2_T2_YYYYMMDD.txt', f'_factset_hld_v2_T2_{lb3}.txt')
    ]:
        os.rename(os.path.join(r'F:\Portia', filename), os.path.join(r'F:\Portia', newname))
        shutil.move(os.path.join(r'F:\Portia', newname), calibre if 'JOHCM' in newname else factset)
    
    print('BAU reports filed')

    shutil.copy2(r'F:\Portia\FactSet\zero_px_YYYYMMDD.csv', factset)
    with FileInput(os.path.join(factset, 'zero_px_YYYYMMDD.csv'), inplace=True) as f:
        for line in f:
            print(line.replace('YYYYMMDD', lb2), end='')

    print('FactSetZeroPx done')

  
        
        
        
        
        
