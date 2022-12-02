import numpy as np
import plotly as pl
from zipfile import ZipFile
import pandas as pd
import os 
import json

print("Proyecto del datathon")

#Primero vamos a leer los archivos de zipfile

Sfile = "/home/lordangel11/Documentos/Maalik/Data/zips/datos_PDN_all_22_09_2022.zip"
#S2file = "Data/S2datos_PDN_all_22_09_2022.zip"
#S3file = "Data/S3datos_PDN_all_22_09_2022.zip"

exdir = "/home/lordangel11/Documentos/Maalik/Data/extracted"

with ZipFile(Sfile, 'r') as zip:
    
   zip.printdir()
   print("Ya leyo todos los archivos")
   
   zip.extractall(exdir)
   
dirs1 = exdir + "/s1/s1.zip"

with ZipFile(dirs1, 'r') as zip1:
    zip1.printdir() 
    
    zip1.extractall(exdir + "/s1json")