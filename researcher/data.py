import urllib.request
import os
from . import write_data

def root():
    root = os.path.abspath(os.path.join(".", os.pardir))
    return root

def retrieve_CO2():
    url = 'ftp://aftp.cmdl.noaa.gov/products/trends/co2/co2_annmean_mlo.txt'
    urllib.request.urlretrieve(url, rootPath + '/researcher/data/CO2Data.txt')
    write_data.write_CO2()

def retrieve_N2O():
    url = 'ftp://ftp.cmdl.noaa.gov/hats/n2o/combined/HATS_global_N2O.txt'
    urllib.request.urlretrieve(url, rootPath + '/researcher/data/N2OData.txt')
    write_data.write_N2O()

def retrieve_CH4():
    url = 'ftp://aftp.cmdl.noaa.gov/products/trends/ch4/ch4_annmean_gl.txt'
    urllib.request.urlretrieve(url, rootPath + '/researcher/data/CH4Data.txt')
    write_data.write_CH4()

def retrieve_CFC11():
    url = 'ftp://ftp.cmdl.noaa.gov/hats/cfcs/cfc11/combined/HATS_global_F11.txt'
    urllib.request.urlretrieve(url, rootPath + '/researcher/data/CFC11Data.txt')
    write_data.write_CFC11()

def retrieve_CFC12():
    url = 'ftp://ftp.cmdl.noaa.gov/hats/cfcs/cfc12/combined/HATS_global_F12.txt'
    urllib.request.urlretrieve(url, rootPath + '/researcher/data/CFC12Data.txt')
    write_data.write_CFC12()  

def retrieve_Temperature():
    url = 'https://data.giss.nasa.gov/gistemp/graphs/graph_data/Global_Mean_Estimates_based_on_Land_and_Ocean_Data/graph.txt'
    urllib.request.urlretrieve(url, rootPath + '/researcher/data/TemperatureData.txt')
    write_data.write_Temperature()

def retrieve_All():
    global rootPath
    rootPath = root()
    retrieve_CO2()
    retrieve_N2O()
    retrieve_CH4()
    retrieve_CFC11()
    retrieve_CFC12()