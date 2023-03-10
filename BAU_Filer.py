# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 11:53:10 2022
    
@author: fben-eghan
"""
def FOFStoDexia():
    #HIGLIGHT FROM HERE 
    import re
    from shutil import move
    from os import remove
    import os
    import subprocess
    import time
    import pandas as pd
    import numpy as np
    from datetime import date
    from shutil import copyfile, copy2
    import datetime
    import shutil
    import glob
    
    lb_ = (pd.datetime.today() - pd.tseries.offsets.BDay(0)).date().strftime('%d%m%y')
    lb1 = (pd.datetime.today() - pd.tseries.offsets.BDay(0)).date().strftime('%Y%m%d')
    lb2 = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%Y%m%d')
    lb = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%m-%d-%y')
    lb3 = (pd.datetime.today() - pd.tseries.offsets.BDay(2)).date().strftime('%Y%m%d')
    y = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).year
    m = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%B')
    m_ = (pd.datetime.today() - pd.tseries.offsets.BDay(0)).date().strftime('%B')
    
    #Files away the used FOF files
    src_folder = r'X:\Portia'
    pattern1 = src_folder + r'\\XC21P163VALPOS1*'
    dst_folder = r'Q:\Dexia\{}'.format(lb)
    
    for file in glob.iglob(pattern1, recursive=True):
        # extract file name form file path
        file_name = os.path.basename(file)
        move(file, dst_folder)
        print('Moved:', file)
        
    pattern2 = src_folder + r'\\ASSETS*'
    
    for file in glob.iglob(pattern2, recursive=True):
        # extract file name form file path
        file_name = os.path.basename(file)
        move(file, dst_folder)
        print('Moved:', file)
        
    src_folder2 = r'X:\History'
    pattern3 = src_folder2 + r'\\{}*'.format(lb1)
    
    for file in glob.iglob(pattern3, recursive=True):
        # extract file name form file path
        file_name = os.path.basename(file)
        move(file, dst_folder)
        print('Moved:', file)

        
    #Files away the cash upload files
def CashFiler():        
    import re
    from shutil import move
    from os import remove
    import os
    import subprocess
    import time
    import pandas as pd
    import numpy as np
    from datetime import date
    from shutil import copyfile, copy2
    import datetime
    import shutil
    import glob
    
    lb_ = (pd.datetime.today() - pd.tseries.offsets.BDay(0)).date().strftime('%d%m%y')
    lb1 = (pd.datetime.today() - pd.tseries.offsets.BDay(0)).date().strftime('%Y%m%d')
    lb2 = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%Y%m%d')
    lb = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%m-%d-%y')
    lb3 = (pd.datetime.today() - pd.tseries.offsets.BDay(2)).date().strftime('%Y%m%d')
    y = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).year
    m = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%B')
    m_ = (pd.datetime.today() - pd.tseries.offsets.BDay(0)).date().strftime('%B')
    
    os.rename(r'F:\Portia\f2906icsh.gw10.inc', r'F:\Portia\f2906icsh.csv')
    os.rename(r'Q:\Rec\f2906icsh.gw10.inc', r'Q:\Rec\f2906icsh{}.gw10.inc'.format(lb_))
    move(r'Q:\Rec\f2906icsh{}.gw10.inc'.format(lb_), r'Q:\Rec\{}'.format(m_))
    print('Filed:', r'Q:\Rec\f2906icsh{}.gw10.inc'.format(lb_))
    
    
    #Removes old pricing files
def PxRemover():        
    import re
    from shutil import move
    from os import remove
    import os
    import subprocess
    import time
    import pandas as pd
    import numpy as np
    from datetime import date
    from shutil import copyfile, copy2
    import datetime
    import shutil
    import glob
    
    lb_ = (pd.datetime.today() - pd.tseries.offsets.BDay(0)).date().strftime('%d%m%y')
    lb1 = (pd.datetime.today() - pd.tseries.offsets.BDay(0)).date().strftime('%Y%m%d')
    lb2 = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%Y%m%d')
    lb = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%m-%d-%y')
    lb3 = (pd.datetime.today() - pd.tseries.offsets.BDay(2)).date().strftime('%Y%m%d')
    y = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).year
    m = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%B')
    m_ = (pd.datetime.today() - pd.tseries.offsets.BDay(0)).date().strftime('%B')

    
    remove(r'F:\Portia\FTP\mpx.txt')
    remove(r'F:\Portia\FTP\mpx2.txt')
    print(r'Removed mpx txt files')
    
    remove(r'F:\Portia\FTP\dailypricesreturn2.txt')
    remove(r'F:\Portia\FTP\fwdsdailyreturn.txt')
    remove(r'F:\Portia\FTP\corpcoupons.txt')
    remove(r'F:\Portia\FTP\fxdailyreturn.txt')
    print(r'Removed 4 price sourcing files')


def Backup():
    import re
    from shutil import move
    from os import remove
    import os
    import subprocess
    import time
    import pandas as pd
    import numpy as np
    from datetime import date
    from shutil import copyfile, copy2
    import datetime
    import shutil
    import glob
    
    lb_ = (pd.datetime.today() - pd.tseries.offsets.BDay(0)).date().strftime('%d%m%y')
    lb1 = (pd.datetime.today() - pd.tseries.offsets.BDay(0)).date().strftime('%Y%m%d')
    lb2 = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%Y%m%d')
    lb = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%m-%d-%y')
    lb3 = (pd.datetime.today() - pd.tseries.offsets.BDay(2)).date().strftime('%Y%m%d')
    y = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).year
    m = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%B')
    m_ = (pd.datetime.today() - pd.tseries.offsets.BDay(0)).date().strftime('%B')
    
    feln = r'F:\IT\!! NEW IT\Data Admin\Data Administrators\Felix Notes'
    
    copy2(r'F:\Portia\FTP\ManualPrices.xlsx', r'H:')
    copy2(r'F:\Portia\FTP\ManualPrices.xlsx', feln)
    print(r'ManualPrices.xlsx backed up')  
    
    copy2(r'Q:\Rec\Cash Rec {}.xlsx'.format(y), r'H:')
    copy2(r'Q:\Rec\Cash Rec {}.xlsx'.format(y), feln)
    print(r'Cash Rec {}.xlsx backed up'.format(y))
    
    
def E2Ebak():
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
    
    #These are the directories for the Import files
    ask = r'F:\Portia\FTP\BloombergAskPrices.txt'
    mid = r'F:\Portia\FTP\BloombergMidPrices.txt'
    fwd = r'F:\Portia\FTP\BloombergFWDs.txt'
    vs = r'F:\Portia\FTP\BloombergVotingShares.txt'
    sos = r'F:\Portia\FTP\BloombergSharesOS.txt'
    corp = r'F:\Portia\FTP\BloombergCorpPrices.txt'
    bid = r'F:\Portia\FTP\BloombergBidPrices.txt'
    fx = r'F:\Portia\FTP\BloombergFXs.txt'
    close = r'F:\Portia\FTP\BloombergPrices.txt'
    
    mpx = r'F:\Portia\FTP\mpx.prn'
    mpx2 = r'F:\Portia\FTP\mpx2.prn'
    lip = r'F:\Portia\Currencies.prn'
    
    #Backup the Pricing and FX files for E2E Testing
    lb2 = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%Y%m%d')
    y = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).year
    m = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%B')
    
    spiv1 = r'F:\Portia\NT\Parallel\Backups\{}\{}\{}\SPIV1'.format(y, m, lb2)
    mbak = r'F:\Portia\NT\Parallel\Backups\{}\{}\{}'.format(y, m, lb2)
    
    os.makedirs(spiv1)
    
    copy2(ask, spiv1)
    copy2(mid, spiv1)
    copy2(fwd, spiv1)
    copy2(vs, spiv1)
    copy2(sos, spiv1)
    copy2(corp, spiv1)
    copy2(bid, spiv1)
    copy2(fx, spiv1)
    copy2(close, spiv1)
    
    copy2(mpx, mbak)
    copy2(mpx2, mbak)
    copy2(lip, mbak)    
    
    print('SPIV1, fx and mpx files backed up')
    
    
    #2
    #Files and renames reports
def Rpt_Filer():    
    import re
    from shutil import move
    from os import remove
    import os
    import subprocess
    import time
    import pandas as pd
    import numpy as np
    from datetime import date
    from shutil import copyfile, copy2
    import datetime
    import shutil
    import glob
    
    lb_ = (pd.datetime.today() - pd.tseries.offsets.BDay(0)).date().strftime('%d%m%y')
    lb1 = (pd.datetime.today() - pd.tseries.offsets.BDay(0)).date().strftime('%Y%m%d')
    lb2 = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%Y%m%d')
    lb = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%m-%d-%y')
    lb3 = (pd.datetime.today() - pd.tseries.offsets.BDay(2)).date().strftime('%Y%m%d')
    y = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).year
    m = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%B')
    m_ = (pd.datetime.today() - pd.tseries.offsets.BDay(0)).date().strftime('%B')
    
    calibre = r'F:\Portia\Calibre\{}\{}'.format(m, lb2)
    factset = r'F:\Portia\FactSet\{}\{}'.format(m, lb2)
    
    move(r'F:\Portia\Russell APC Holding.csv', r'F:\IT\RUSSELLAPC\Russell APC Holding.csv')

    os.makedirs(calibre)
    os.rename(r'F:\Portia\portsnap_[date]_JOHCM.csv', r'F:\Portia\portsnap_{}_JOHCM.csv'.format(lb2))
    os.rename(r'F:\Portia\refval__[date]_JOHCM.csv', r'F:\Portia\refval__{}_JOHCM.csv'.format(lb2))
    move(r'F:\Portia\portsnap_{}_JOHCM.csv'.format(lb2), calibre)
    move(r'F:\Portia\refval__{}_JOHCM.csv'.format(lb2), calibre)
    
    os.makedirs(factset)
    os.rename(r'F:\Portia\JOHAM_T1_YYYYMMDD.txt', r'F:\Portia\JOHAM_T1_{}.txt'.format(lb2))
    os.rename(r'F:\Portia\JOHAM_T2_YYYYMMDD.txt', r'F:\Portia\JOHAM_T2_{}.txt'.format(lb3))
    os.rename(r'F:\Portia\joham_fx_YYYYMMDD.txt', r'F:\Portia\joham_fx_{}.txt'.format(lb2))
    os.rename(r'F:\Portia\_factset_fwd_T1_YYYYMMDD.txt', r'F:\Portia\_factset_fwd_T1_{}.txt'.format(lb2))
    os.rename(r'F:\Portia\_factset_fwd_T2_YYYYMMDD.txt', r'F:\Portia\_factset_fwd_T2_{}.txt'.format(lb3))
    os.rename(r'F:\Portia\_factset_hld_v2_T1_YYYYMMDD.txt', r'F:\Portia\_factset_hld_v2_T1_{}.txt'.format(lb2))
    os.rename(r'F:\Portia\_factset_hld_v2_T2_YYYYMMDD.txt', r'F:\Portia\_factset_hld_v2_T2_{}.txt'.format(lb3))
    move(r'F:\Portia\JOHAM_T2_{}.txt'.format(lb3), factset)
    move(r'F:\Portia\JOHAM_T1_{}.txt'.format(lb2), factset)
    move(r'F:\Portia\joham_fx_{}.txt'.format(lb2), factset)
    move(r'F:\Portia\_factset_fwd_T1_{}.txt'.format(lb2), factset)
    move(r'F:\Portia\_factset_fwd_T2_{}.txt'.format(lb3), factset)
    move(r'F:\Portia\_factset_hld_v2_T1_{}.txt'.format(lb2), factset)
    move(r'F:\Portia\_factset_hld_v2_T2_{}.txt'.format(lb3), factset)
    print('BAU reports filed')
    '''
    oldzero = r'F:\Portia\FactSet\{}\{}\zero_px_YYYYMMDD.csv'.format(m, lb2)
    newzero = r'F:\Portia\FactSet\{}\{}\zero_px_{}.csv'.format(m, lb2, lb2)
    copy2(r'F:\Portia\FactSet\zero_px_YYYYMMDD.csv', factset)
    
    from fileinput import FileInput
    def FactSetZeroPx(search_text, replace_text, dirs):
      
        # Opening file using FileInput
        with FileInput(dirs, inplace=True) as f:
      
            # Iterating over every and changing
            # the search_text with replace_text
            # using the replace function
            for line in f:
                print(line.replace(search_text,
                                   replace_text), end='')
      
        # Return "Text replaced" string
        return r'{}: {} to {}'.format(dirs[8:], search_text, replace_text)
    
    print(FactSetZeroPx(r'YYYYMMDD', lb2, factset+'\zero_px_YYYYMMDD.csv'))
    os.rename(oldzero, newzero)
'''
    
    
    #3
    ##NT STUFF
def Rpt_FilerNT():

    import re
    from shutil import move
    from os import remove
    import os
    import subprocess
    import time
    import pandas as pd
    import numpy as np
    from datetime import date
    from shutil import copyfile, copy2
    import datetime
    import shutil
    import glob
    
    lb_ = (pd.datetime.today() - pd.tseries.offsets.BDay(0)).date().strftime('%d%m%y')
    lb1 = (pd.datetime.today() - pd.tseries.offsets.BDay(0)).date().strftime('%Y%m%d')
    lb2 = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%Y%m%d')
    lb = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%m-%d-%y')
    lb3 = (pd.datetime.today() - pd.tseries.offsets.BDay(2)).date().strftime('%Y%m%d')
    y = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).year
    m = (pd.datetime.today() - pd.tseries.offsets.BDay(1)).date().strftime('%B')
    m_ = (pd.datetime.today() - pd.tseries.offsets.BDay(0)).date().strftime('%B')    
    
    calibrent = r'F:\Portia\NT\Parallel\Downstream_E2E\Calibre\{}\{}'.format(m, lb2)
    factsetnt = r'F:\Portia\NT\Parallel\Downstream_E2E\FactSet\{}\{}'.format(m, lb2)

    os.makedirs(calibrent)
    os.rename(r'F:\Portia\portsnap_[date]_JOHCM_NT.csv', r'F:\Portia\portsnap_{}_JOHCM_NT.csv'.format(lb2))
    os.rename(r'F:\Portia\refval__[date]_JOHCM_NT.csv', r'F:\Portia\refval__{}_JOHCM_NT.csv'.format(lb2))
    move(r'F:\Portia\portsnap_{}_JOHCM_NT.csv'.format(lb2), calibrent)
    move(r'F:\Portia\refval__{}_JOHCM_NT.csv'.format(lb2), calibrent)

    os.makedirs(factsetnt)
    os.rename(r'F:\Portia\JOHAM_NT_T1_YYYYMMDD.txt', r'F:\Portia\JOHAM_NT_T1_{}.txt'.format(lb2))
    os.rename(r'F:\Portia\JOHAM_NT_T2_YYYYMMDD.txt', r'F:\Portia\JOHAM_NT_T2_{}.txt'.format(lb3))
    os.rename(r'F:\Portia\joham_fx_NT_YYYYMMDD.txt', r'F:\Portia\joham_fx_NT_{}.txt'.format(lb2))
    os.rename(r'F:\Portia\_factset_fwd_NT_T1_YYYYMMDD.txt', r'F:\Portia\_factset_fwd_NT_T1_{}.txt'.format(lb2))
    os.rename(r'F:\Portia\_factset_fwd_NT_T2_YYYYMMDD.txt', r'F:\Portia\_factset_fwd_NT_T2_{}.txt'.format(lb3))
    os.rename(r'F:\Portia\_factset_hld_NT_T1_YYYYMMDD.txt', r'F:\Portia\_factset_hld_NT_T1_{}.txt'.format(lb2))
    os.rename(r'F:\Portia\_factset_hld_NT_T2_YYYYMMDD.txt', r'F:\Portia\_factset_hld_NT_T2_{}.txt'.format(lb3))
    move(r'F:\Portia\JOHAM_NT_T2_{}.txt'.format(lb3), factsetnt)
    move(r'F:\Portia\JOHAM_NT_T1_{}.txt'.format(lb2), factsetnt)
    move(r'F:\Portia\joham_fx_NT_{}.txt'.format(lb2), factsetnt)
    move(r'F:\Portia\_factset_fwd_NT_T1_{}.txt'.format(lb2), factsetnt)
    move(r'F:\Portia\_factset_fwd_NT_T2_{}.txt'.format(lb3), factsetnt)
    move(r'F:\Portia\_factset_hld_NT_T1_{}.txt'.format(lb2), factsetnt)
    move(r'F:\Portia\_factset_hld_NT_T2_{}.txt'.format(lb3), factsetnt)
    print('NT reports filed')  
'''    
    oldzeront = r'F:\Portia\FactSet\{}\{}\zero_px_YYYYMMDD.csv'.format(m, lb2)
    newzeront = r'F:\Portia\FactSet\{}\{}\zero_px_{}.csv'.format(m, lb2, lb2)
    copy2(r'F:\Portia\FactSet\zero_px_YYYYMMDD.csv', factsetnt)
    
    from fileinput import FileInput
    def FactSetZeroPx(search_text, replace_text, dirs):
      
        # Opening file using FileInput
        with FileInput(dirs, inplace=True) as f:
      
            # Iterating over every and changing
            # the search_text with replace_text
            # using the replace function
            for line in f:
                print(line.replace(search_text,
                                   replace_text), end='')
      
        # Return "Text replaced" string
        return r'{}: {} to {}'.format(dirs[8:], search_text, replace_text)
    
    print(FactSetZeroPx(r'YYYYMMDD', lb2, factsetnt+'\zero_px_YYYYMMDD.csv'))
    os.rename(oldzeront, newzeront)'''

    
        
  
        
        
        
        
        