# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 16:36:50 2019

@author: sayala
"""

import analysis

frontGTIrow=[53.01720526, 55.32772694, 55.78247445, 55.69094834, 55.62417481, 55.59217422]
backGTIrow=[8.550246348, 4.626045218, 4.406054333, 6.141527447, 9.211464402, 12.87567548]

portraitorlandscape='landscape'
sensorsy=6
                       
cellCenterPVM, stdpl, cellsx, cellsy = setupforPVMismatch(portraitorlandscape=portraitorlandscape, sensorsy=sensorsy)
print(portraitorlandscape, cellsx, cellsy)
stdpl


PowerAveraged, PowerDetailed = calculateVFPVMismatch(cellCenterPVM, stdpl, cellsx, cellsy, sensorsy, frontGTIrow, backGTIrow)

print(round(PowerAveraged,2), round(PowerDetailed,2))
print("Looking for:", 13.14, 12.856)


cellCenterBIoriginal.append((i*numsensors/6.0+(i+1)*numsensors/6.0)/2)
