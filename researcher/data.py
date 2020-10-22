import urllib.request
import os
from . import write_data_final

def root():
    root = os.path.abspath(os.path.join(".", os.pardir))
    return root

def retrieve_CO2():
    rootPath = root()
    url = 'ftp://aftp.cmdl.noaa.gov/products/trends/co2/co2_annmean_mlo.txt'
    open(rootPath + 'researcher/data/CO2Data.txt')
    urllib.request.urlretrieve(url, rootPath + 'researcher/data/CO2Data.txt')
    write_data_final.write_CO2()

def retrieve_N2O():
    rootPath = root()
    url = 'ftp://ftp.cmdl.noaa.gov/hats/n2o/combined/HATS_global_N2O.txt'
    open(rootPath + 'researcher/data/N2OData.txt')
    urllib.request.urlretrieve(url, rootPath + 'researcher/data/N2OData.txt')
    write_data_final.write_N2O()

def retrieve_CH4():
    rootPath = root()
    url = 'ftp://aftp.cmdl.noaa.gov/products/trends/ch4/ch4_annmean_gl.txt'
    open(rootPath + 'researcher/data/CH4Data.txt')
    urllib.request.urlretrieve(url, rootPath + 'researcher/data/CH4Data.txt')
    write_data_final.write_CH4()

def retrieve_CFC11():
    rootPath = root()
    url = 'ftp://ftp.cmdl.noaa.gov/hats/cfcs/cfc11/combined/HATS_global_F11.txt'
    open(rootPath + 'researcher/data/CFC11Data.txt')
    urllib.request.urlretrieve(url, rootPath + 'researcher/data/CFC11Data.txt')
    write_data_final.write_CFC11()

def retrieve_CFC12():
    rootPath = root()
    url = 'ftp://ftp.cmdl.noaa.gov/hats/cfcs/cfc12/combined/HATS_global_F12.txt'
    open(rootPath + 'researcher/data/CFC12Data.txt')
    urllib.request.urlretrieve(url, rootPath + 'researcher/data/CFC12Data.txt')
    write_data_final.write_CFC12()  

def retrieve_Temperature():
    rootPath = root()
    url = 'https://data.giss.nasa.gov/gistemp/graphs/graph_data/Global_Mean_Estimates_based_on_Land_and_Ocean_Data/graph.txt'
    open(rootPath + 'researcher/data/TemperatureData.txt')
    urllib.request.urlretrieve(url, rootPath + 'researcher/data/TemperatureData.txt')
    write_data_final.write_Temperature()

def retrieve_All():
    retrieve_CO2()
    retrieve_N2O()
    retrieve_CH4()
    retrieve_CFC11()
    retrieve_CFC12()