import numpy as np
import plotly as pl
from zipfile import ZipFile
import pandas as pd
import os 

print("Proyecto del datathon")

#Primero vamos a leer los archivos de zipfile



S1file = "/home/lordangel11/Documentos/Maalik/Data/zips/datos_PDN_all_22_09_2022.zip"
#S2file = "Data/S2datos_PDN_all_22_09_2022.zip"
#S3file = "Data/S3datos_PDN_all_22_09_2022.zip"

with ZipFile(S1file, 'r') as zip:
    
   zip.printdir()
   print("Ya leyo todos los archivos del S1")
    
    