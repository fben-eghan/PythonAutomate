# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 15:43:26 2022

@author: fben-eghan
"""

import BAU_Filer

#File FOFs from X drive to Q drive
#BAU_Filer.FOFStoDexia()

#Files cash upload file
#BAU_Filer.CashFiler()

#Removes old pricing files
BAU_Filer.PxRemover()

#Back up key files
BAU_Filer.Backup()

#Backup the Pricing and FX files for E2E Testing
BAU_Filer.E2Ebak()

"""
WAIT UNTIL REPORTS FINISH RUNNING
"""
#Files BAU reports. Ready to FTP
BAU_Filer.Rpt_Filer()

#Files NT test reports. Ready to FTP
#BAU_Filer.Rpt_FilerNT()