import numpy as np
#import plotly as pl
from zipfile import ZipFile
#import pandas as pd
import os 


print("Proyecto del datathon")

Sfile = "C:/Users/jossa/OneDrive - Universidad de Guanajuato/Documentos/Josue/Demat/Hackathon/Datathon 2022/Data/zips/datos_PDN_all_22_09_2022.zip"
exdir = "C:/Users/jossa/OneDrive - Universidad de Guanajuato/Documentos/Josue/Demat/Hackathon/Datathon 2022/Data/extracted"

with ZipFile(Sfile, 'r') as zip:
    
   zip.printdir()
   print("Ya leyo todos los archivos")
   
   zip.extractall(exdir)
   
dirs1 = exdir + "/s1/s1.zip"

with ZipFile(dirs1, 'r') as zip1:
    zip1.printdir() 
    
    zip1.extractall(exdir + "/s1json")
    
