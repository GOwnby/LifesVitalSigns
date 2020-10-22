import urllib.request
import os
from . import write_data_final


def retrieve_CO2():
    url = 'ftp://aftp.cmdl.noaa.gov/products/trends/co2/co2_annmean_mlo.txt'
    open('data/CO2Data.txt', 'w')
    urllib.request.urlretrieve(url, 'data/CO2Data.txt')
    write_data_final.write_CO2()

def retrieve_N2O():
    url = 'ftp://ftp.cmdl.noaa.gov/hats/n2o/combined/HATS_global_N2O.txt'
    open('data/N2OData.txt', 'w')
    urllib.request.urlretrieve(url, 'data/N2OData.txt')
    write_data_final.write_N2O()

def retrieve_CH4():
    url = 'ftp://aftp.cmdl.noaa.gov/products/trends/ch4/ch4_annmean_gl.txt'
    open('data/CH4Data.txt', 'w')
    urllib.request.urlretrieve(url, 'data/CH4Data.txt')
    write_data_final.write_CH4()

def retrieve_CFC11():
    url = 'ftp://ftp.cmdl.noaa.gov/hats/cfcs/cfc11/combined/HATS_global_F11.txt'
    open('data/CFC11Data.txt', 'w')
    urllib.request.urlretrieve(url, 'data/CFC11Data.txt')
    write_data_final.write_CFC11()

def retrieve_CFC12():
    url = 'ftp://ftp.cmdl.noaa.gov/hats/cfcs/cfc12/combined/HATS_global_F12.txt'
    open('data/CFC12Data.txt', 'w')
    urllib.request.urlretrieve(url, 'data/CFC12Data.txt')
    write_data_final.write_CFC12()  

def retrieve_Temperature():
    url = 'https://data.giss.nasa.gov/gistemp/graphs/graph_data/Global_Mean_Estimates_based_on_Land_and_Ocean_Data/graph.txt'
    open('data/TemperatureData.txt', 'w')
    urllib.request.urlretrieve(url, 'data/TemperatureData.txt')
    write_data_final.write_Temperature()

def retrieve_All():
    if not os.path.exists('data'):
        os.makedirs('data')
    retrieve_CO2()
    retrieve_N2O()
    retrieve_CH4()
    retrieve_CFC11()
    retrieve_CFC12()