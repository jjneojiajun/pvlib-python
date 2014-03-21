# Autogenerated with SMOP version 0.23
# /usr/local/bin/smop pvl_sapmcelltemp.m -o python/pvl_sapmcelltemp.py
import numpy as np
import pandas as pd
import pvl_tools
'''
def pvl_DNVSnow(**kwargs):
    Expect={'DataFrame':'df',
        'SurfTilt':('num','x>=0'),
        'SurfAz':('num','x>=0'),
        'AOI':('matelement','num','array','x>=0'),
        'DNI':('matelement','num','array','x>=0'),
        'In_Plane_SkyDiffuse':('matelement','num','array','x>=0'),
        'GR':('matelement','num','array','x>=0'),
        }
'''

N=snowevents(month,yr)

snow=acc(month,yr)/2.54 #Convert snow accumulaiton to inches 
Se=.5*snow*(1+1/N)
#N- Snow events in a month
#snow- snow accumulation in a month
#R- Row length
#H- Drop to ground
#P- Piled snow angle, 40 degrees

gamma=1.00
GIT=1-0.51*exp(-gamma)
RH=Year_irr.monthaveRH(month)
Tair=Year_irr.monthavetemp(month)+273 #convert to kelvin
POA=Year_irr.POA(month) 

Loss(month,tind)=5.7E4*Se*cosd(tilt(tind))**2*GIT*RH/Tair**2/POA**.67

lossparameter(month,tind)=Se*cosd(tilt(tind))**2*GIT*RH/Tair**2/POA**.67

