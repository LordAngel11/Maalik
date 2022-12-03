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
    
#Ahora lo que vamos a hacer es un path de los json... 
#Baja California Sur 
print("Archivos Json")



#Lo que vamos a hacer ahora es un recorrido por todas las carpetas de estados de la republica:

rootdir = "/home/lordangel11/Documentos/Maalik/Data/extracted/s1json"
states = []

for subdir, dirs, files in os.walk(rootdir):
    print(subdir) 
    #jSON = [pos_json for pos_json in dirs if pos_json.endswith('.json')] #Es un diccionario de json.
    #print(jSON)
    for file in files:
        print(os.path.join(subdir, file))
        #print("archivo")
        

#...
#path_BCS = '/home/lordangel11/Documentos/Maalik/Data/extracted/s1json/BajaCaliforniaSur'
#json_BCS = [pos_json for pos_json in os.listdir(path_BCS) if pos_json.endswith('.json')]   #Este es un diccionario de Jsons
#print(json_BCS)

#dataframe de BCS

#

#Df = []
#for i in range(len(json_BCS)):
    
    


#Chiapas
#Chihuahua
#EdoMex
#Guanajuato
#INAI
#Puebla
#QuintanaRoo
#SanLuisPotosi
#Aguascalientes
#Jalisco
#Tabasco 
#Tlaxcala
#Zacatecas.

