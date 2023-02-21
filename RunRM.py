# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 12:16:45 2022

@author: fben-eghan
"""

#HIGLIGHT FROM HERE
from RMtoMSCI import RMtoMSCI
#from RMtoMSCI_NT import RMtoMSCI_NT

#CAD-USD X-RATE Curncy in Bloomberg for BD-1. Update this.
CADUSDRATE = .7433
#STEP 1: For PROD
print(RMtoMSCI(CADUSDRATE))

#STEP 2: For UAT
print(RMtoMSCI_NT(CADUSDRATE))
'''
if report date != t-1, use Ctrl+H on HLD file to replace t-1 with report date
Then run MSCI-ZPO2 with the required filepath and report date
'''
