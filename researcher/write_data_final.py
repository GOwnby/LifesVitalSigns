import json
import re
from . import learn_data


def findStartYear(dataset):
    thisDataset = ''
    if dataset == 'CO2':
        thisDataset = 'CO2Data.json'
    if dataset == 'N2O':
        thisDataset = 'N2OData.json'
    if dataset == 'CH4':
        thisDataset = 'CH4Data.json'
    if dataset == 'CFC11':
        thisDataset = 'CFC11Data.json'
    if dataset == 'CFC12':
        thisDataset = 'CFC12Data.json'
    if dataset == 'Temperature':
        thisDataset = 'TemperatureData.json'

    pattern_year = r'[0-9][0-9][0-9][0-9]'

    match_year = ''

    try:
        fp = open('data/' + thisDataset)
        for line in fp:
            if not(re.search('#', line)):
                match_year = re.match(pattern_year, line)
                return match_year
    except KeyError:
        print("error finding start year")
    return match_year

def findEndYear(dataset):
    thisDataset = ''
    if dataset == 'CO2':
        thisDataset = 'CO2Data.json'
    if dataset == 'N2O':
        thisDataset = 'N2OData.json'
    if dataset == 'CH4':
        thisDataset = 'CH4Data.json'
    if dataset == 'CFC11':
        thisDataset = 'CFC11Data.json'
    if dataset == 'CFC12':
        thisDataset = 'CFC12Data.json'
    if dataset == 'Temperature':
        thisDataset = 'TemperatureData.json'

    pattern_year = r'[0-9][0-9][0-9][0-9]'
    countLines = 0
    try:
        fp = open('data/' + thisDataset)
        for line in fp:
            countLines += 1
    finally:
        thisLine = 0
        fp = open('data/' + thisDataset)
        for line in fp:
            thisLine += 1
            if thisLine == (countLines - 1):
                match_year = re.match(pattern_year, line)
            if thisLine == countLines:
                match_year = re.match(pattern_year, line)
        fp.close()
    return match_year

def findCommonStartYear():
    startYearDataCO2 = findStartYear('CO2')
    startYearDataN2O = findStartYear('N2O')
    startYearDataCH4 = findStartYear('CH4')
    startYearDataCFC11 = findStartYear('CFC11')
    startYearDataCFC12 = findStartYear('CFC12')
    startYearDataTemperature = findStartYear('Temperature')

    lowestCommonYear = startYearDataCO2
    if lowestCommonYear <= startYearDataN2O:
        lowestCommonYear = startYearDataN2O
    if lowestCommonYear <= startYearDataCH4:
        lowestCommonYear = startYearDataCH4
    if lowestCommonYear <= startYearDataCFC11:
        lowestCommonYear = startYearDataCFC11
    if lowestCommonYear <= startYearDataCFC12:
        lowestCommonYear = startYearDataCFC12
    if lowestCommonYear <= startYearDataTemperature:
        lowestCommonYear = startYearDataTemperature

    return lowestCommonYear

def findCommonEndYear():
    endYearDataCO2 = findEndYear('CO2')
    endYearDataN2O = findEndYear('N2O')
    endYearDataCH4 = findEndYear('CH4')
    endYearDataCFC11 = findEndYear('CFC11')
    endYearDataCFC12 = findEndYear('CFC12')
    endYearDataTemperature = findEndYear('Temperature')

    highestCommonYear = endYearDataCO2
    if highestCommonYear >= endYearDataN2O:
        highestCommonYear = endYearDataN2O
    if highestCommonYear >= endYearDataCH4:
        highestCommonYear = endYearDataCH4
    if highestCommonYear >= endYearDataCFC11:
        highestCommonYear = endYearDataCFC11
    if highestCommonYear >= endYearDataCFC12:
        highestCommonYear = endYearDataCFC12
    if highestCommonYear >= endYearDataTemperature:
        highestCommonYear = endYearDataTemperature

    return highestCommonYear

def function_write(data, fp, pattern_year, pattern_ppb1, pattern_ppb2):
    for line in fp:
        if not(re.match('#', line)):
            if re.match(pattern_year, line):
                match_year = re.match(pattern_year, line)
                lineEdited = line.replace(str(match_year.group(0)), '')
                lineEdited = lineEdited[7:]
                match_ppb1 = re.match(pattern_ppb1, lineEdited)
                if (str(match_ppb1.group(0)) != 'nan'):
                    lineEdited = lineEdited.replace(
                        str(match_ppb1.group(0)), '')
                    match_ppb2 = re.match(pattern_ppb2, lineEdited)
                    this_year = str(match_year.group(0))
                    this_ppb = str(match_ppb1.group(0)) + \
                        str(match_ppb2.group(0))
                    counter = 1
                    while counter <= 12:
                        this_year = this_year + '_' + str(counter)
                        data[this_year] = float(this_ppb)
                        counter =+ 1
    

def write_CO2():
    data = {}
    pattern_year = r'[0-9][0-9][0-9][0-9]'
    pattern_ppm = r'[0-9][0-9][0-9].[0-9][0-9]'
    try:
        fp = open('data/CO2Data.txt')
        for line in fp:
            if not(re.search('#', line)):
                match_year = re.search(pattern_year, line)
                match_ppm = re.search(pattern_ppm, line)
                if match_year is not None:
                    if match_ppm is not None:
                        this_year = match_year.group(0)
                        this_ppm = match_ppm.group(0)
                        data[int(this_year)] = float(this_ppm)

        fp.close()
        outfile = open('../LifesVitalSigns/static/static_dirs/js/json/CO2Data.json', 'w')
        json.dump(data, outfile)
    except AttributeError:
        print("Error retrieving file")

def write_N2O():
    data = {}
    pattern_year = r'[0-9][0-9][0-9][0-9]'
    pattern_ppb1 = r'[n0123456789][a0123456789][n0123456789]'
    pattern_ppb2 = r'.[0-9][0-9][0-9]'
    try:
        fp = open('data/N2OData.txt')
        function_write(data,fp,pattern_year,pattern_ppb1,pattern_ppb2)

        fp.close()
        outfile = open('../LifesVitalSigns/static/static_dirs/js/json/N2OData.json', 'w')
        json.dump(data, outfile)
        learn_data.average_dataset('N2O')
    except AttributeError:
        print("Error retrieving file")


def write_CH4():
    data = {}
    pattern_year = r'[0-9][0-9][0-9][0-9]'
    pattern_ppb = r'[0-9][0-9][0-9][0-9].[0-9][0-9]'
    try:
        fp = open('data/CH4Data.txt')
        for line in fp:
            if not(re.search('#', line)):
                match_year = re.search(pattern_year, line)
                match_ppb = re.search(pattern_ppb, line)
                if match_year is not None:
                    if match_ppb is not None:
                        this_year = match_year.group(0)
                        this_ppb = match_ppb.group(0)
                        data[int(this_year)] = float(this_ppb)

        fp.close()
        outfile = open('../LifesVitalSigns/static/static_dirs/js/json/CH4Data.json', 'w')       
        json.dump(data, outfile)
    except AttributeError:
        print("Error retrieving file")


def write_CFC11():
    data = {}
    pattern_year = r'[0-9][0-9][0-9][0-9]'
    pattern_ppt1 = r'[n0123456789][a0123456789][n0123456789]'
    pattern_ppt2 = r'.[0-9][0-9][0-9]'
    try:
        fp = open('data/CFC11Data.txt')
        function_write(data,fp,pattern_year,pattern_ppt1,pattern_ppt2)

        fp.close()
        outfile = open('../LifesVitalSigns/static/static_dirs/js/json/CFC11Data.json', 'w')      
        json.dump(data, outfile)
        learn_data.average_dataset('CFC11')
    except AttributeError:
        print("Error retrieving file")


def write_CFC12():
    data = {}
    pattern_year = r'[0-9][0-9][0-9][0-9]'
    pattern_ppt1 = r'[n0123456789][a0123456789][n0123456789]'
    pattern_ppt2 = r'.[0-9][0-9][0-9]'
    try:
        fp = open('data/CFC12Data.txt')
        function_write(data,fp,pattern_year,pattern_ppt1,pattern_ppt2)

        fp.close()
        outfile = open('../LifesVitalSigns/static/static_dirs/js/json/CFC12Data.json', 'w')   
        json.dump(data, outfile)
        learn_data.average_dataset('CFC12')
    except AttributeError:
        print("Error retrieving file")


def write_Temperature():
    data = {}
    pattern_year = r'[0-9][0-9][0-9][0-9]'
    pattern_temp = r'[-]?[0-9][.][0-9][0-9]'
    try:
        fp = open('data/TemperatureData.txt')
        for line in fp:
            match_year = re.search(pattern_year, line)
            match_temp = re.search(pattern_temp, line)
            if match_year is not None:
                if match_temp is not None:
                    this_year = match_year.group(0)
                    this_temp = match_temp.group(0)
                    data[int(this_year)] = float(this_temp)

        fp.close()
        outfile = open('../LifesVitalSigns/static/static_dirs/js/json/TemperatureData.json', 'w')      
        json.dump(data, outfile)
    except AttributeError:
        print("Error retrieving file")

def write_All():
    write_CO2()
    write_N2O()
    write_CH4()
    write_CFC11()
    write_CFC12()
    write_Temperature()