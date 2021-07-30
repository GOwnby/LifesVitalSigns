import urllib.request
import os
import time


def retrieve_CO2():
    url = 'ftp://aftp.cmdl.noaa.gov/products/trends/co2/co2_annmean_mlo.txt'
    dataFile = open('data/CO2Data.txt', 'w')
    urllib.request.urlretrieve(url, 'data/CO2Data.txt')
    dataFile.close()

def retrieve_N2O():
    url = 'ftp://ftp.cmdl.noaa.gov/hats/n2o/combined/HATS_global_N2O.txt'
    dataFile = open('data/N2OData.txt', 'w')
    urllib.request.urlretrieve(url, 'data/N2OData.txt')
    dataFile.close()

def retrieve_CH4():
    url = 'ftp://aftp.cmdl.noaa.gov/products/trends/ch4/ch4_annmean_gl.txt'
    dataFile = open('data/CH4Data.txt', 'w')
    urllib.request.urlretrieve(url, 'data/CH4Data.txt')
    dataFile.close()

def retrieve_CFC11():
    url = 'ftp://ftp.cmdl.noaa.gov/hats/cfcs/cfc11/combined/HATS_global_F11.txt'
    dataFile = open('data/CFC11Data.txt', 'w')
    urllib.request.urlretrieve(url, 'data/CFC11Data.txt')
    dataFile.close()

def retrieve_CFC12():
    url = 'ftp://ftp.cmdl.noaa.gov/hats/cfcs/cfc12/combined/HATS_global_F12.txt'
    dataFile = open('data/CFC12Data.txt', 'w')
    urllib.request.urlretrieve(url, 'data/CFC12Data.txt')
    dataFile.close()

def retrieve_Temperature():
    url = 'https://data.giss.nasa.gov/gistemp/graphs/graph_data/Global_Mean_Estimates_based_on_Land_and_Ocean_Data/graph.txt'
    dataFile = open('data/TemperatureData.txt', 'w')
    urllib.request.urlretrieve(url, 'data/TemperatureData.txt')
    dataFile.close()


def retrieve_All():
    if not os.path.exists('data'):
        os.makedirs('data')
    retrieve_CO2()
    time.sleep(5)
    retrieve_N2O()
    time.sleep(5)
    retrieve_CH4()
    time.sleep(5)
    retrieve_CFC11()
    time.sleep(5)
    retrieve_CFC12()
    time.sleep(5)
    retrieve_Temperature()