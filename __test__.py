#

# Synthesis testbench of Market Analysis Framework Package (MXPY)

#   Market Analysis Tools(MXT):
#       Standardized Tool Wrapper meeting MX analytic needs

#   Market Agent Platform(DAP):
#       Utilizes Market analysis tools
#       Delivers policy evaluation signal to MSA
#

#   Broker API Wrapper(BAW):
#       Secure reliable portfolio management SW
#       Remote Confirmatory Protocol; 2FA
#       Delivers Broker Informatics

#   Multi-Srategic Adjudicator(MSA):
#       Manages asset allocation to competing agents
#       Agents span SR
#

#

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from MXT.ewma import *
from MXT.random import *
from PLT.plt import *
from MXT.window import *
from MXT.signals import *

fs      = 300
N_R     = 30
sf,sA   = (100,3)

ng      = normal_gen(       0,  1                               )
itg     = impulse_train_gen(1,  10                              )
sg      = sin_gen(          sf, sA,             fs              )
eg      = ewma_gen(         sg,.5                               )
wg      = window_gen(       sg, N_R                             )
pg      = plt_gen(          wg, 'Normal Series'                 )
hg      = hist_gen(         pg, 20,             'Hist Normal'   )
w2g     = window2_gen(      wg, 20,             N_R             )
Rg      = Rxx_gen(          w2g                                 )
p2g     = plt2_gen(         Rg, 'Rxx plt'                       )


for h in p2g:
    _=h






















#
