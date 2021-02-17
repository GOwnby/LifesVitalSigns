import json
import re
from . import learn_data
import os
import itertools

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

def function_write(data, fp, patterns, linesInData):
    for line in fp:
        linesInData += 1
        if not(re.match('#', line)):
            if re.match(patterns[0], line):
                match_year = re.match(patterns[0], line)
                lineEdited = line.replace(str(match_year.group(0)), '')
                lineEdited = lineEdited[7:]
                match_ppb1 = re.match(patterns[1], lineEdited)
                if (str(match_ppb1.group(0)) != 'nan'):
                    lineEdited = lineEdited.replace(str(match_ppb1.group(0)), '')
                    match_ppb2 = re.match(patterns[2], lineEdited)
                    this_year = str(match_year.group(0))
                    this_ppb = str(match_ppb1.group(0)) + str(match_ppb2.group(0))
                    counter = 1
                    while counter <= 12:
                        this_year = this_year + '_' + str(counter)
                        data[this_year] = float(this_ppb)
                        counter =+ 1
    dataObject = [data, linesInData]
    return dataObject
    

def write_CO2():
    data = {}
    pattern_year = r'[0-9][0-9][0-9][0-9]'
    pattern_ppm = r'[0-9][0-9][0-9].[0-9][0-9]'
    try:
        fp = open('data/CO2Data.txt')
        linesInData = 0
        for line in fp:
            linesInData += 1
            if not(re.search('#', line)):
                match_year = re.search(pattern_year, line)
                match_ppm = re.search(pattern_ppm, line)
                if match_year is not None:
                    if match_ppm is not None:
                        this_year = match_year.group(0)
                        this_ppm = match_ppm.group(0)
                        data[int(this_year)] = float(this_ppm)

        fp.close()
        basepath = os.path.dirname(__file__)
        filePath = os.path.abspath(os.path.join(basepath, "..", "LifesVitalSigns/static/static_dirs/js/json/CO2Data.json"))
        outfile = open(filePath, 'w')
        json.dump(data, outfile)
        data = None
        outfile = open('data/CO2DataLines.txt', 'w')
        outfile.write(str(linesInData))
        outfile.close()
    except Exception:
        print("Error writing JSON")


def update_CO2():
    data = {}
    pattern_year = r'[0-9][0-9][0-9][0-9]'
    pattern_ppm = r'[0-9][0-9][0-9].[0-9][0-9]'
    try:
        fp = open('data/CO2DataLines.txt')
        for line in fp:
            linesInData = int(line)
        fp = open('data/CO2Data.txt')
        updatedFile = itertools.islice(fp, linesInData)
        fp.close()
        for line in updatedFile:
            linesInData += 1
            match_year = re.search(pattern_year, line)
            match_ppm = re.search(pattern_ppm, line)
            if match_year is not None:
                if match_ppm is not None:
                    this_year = match_year.group(0)
                    this_ppm = match_ppm.group(0)
                    data[int(this_year)] = float(this_ppm)

        basepath = os.path.dirname(__file__)
        filePath = os.path.abspath(os.path.join(basepath, "..", "LifesVitalSigns/static/static_dirs/js/json/CO2Data.json"))
        outfile = open(filePath, 'a')
        json.dump(data, outfile)
        data = None
        updatedFile = None
        outfile = open('data/CO2DataLines.txt', 'w')
        outfile.write(str(linesInData))
        outfile.close()
    except Exception:
        print('Error updating JSON')


def write_N2O():
    data = {}
    pattern_year = r'[0-9][0-9][0-9][0-9]'
    pattern_ppb1 = r'[n0123456789][a0123456789][n0123456789]'
    pattern_ppb2 = r'.[0-9][0-9][0-9]'
    patterns = [pattern_year, pattern_ppb1, pattern_ppb2]
    try:
        fp = open('data/N2OData.txt')
        linesInData = 0
        dataObject = function_write(data, fp, patterns, linesInData)
        linesInData = dataObject[1]
        fp.close()

        basepath = os.path.dirname(__file__)
        filePath = os.path.abspath(os.path.join(basepath, "..", "LifesVitalSigns/static/static_dirs/js/json/N2OData.json"))
        outfile = open(filePath, 'w')
        json.dump(dataObject[0], outfile)
        learn_data.average_dataset('N2O')
        data = None
        outfile = open('data/N2ODataLines.txt', 'w')
        outfile.write(str(linesInData))
        outfile.close()
    except Exception:
        print("Error retrieving file")


def update_N2O():
    data = {}
    pattern_year = r'[0-9][0-9][0-9][0-9]'
    pattern_ppb1 = r'[n0123456789][a0123456789][n0123456789]'
    pattern_ppb2 = r'.[0-9][0-9][0-9]'
    patterns = [pattern_year, pattern_ppb1, pattern_ppb2]
    try:
        fp = open('data/N2ODataLines.txt')
        for line in fp:
            linesInData = int(line)
        fp = open('data/N2OData.txt')
        updatedFile = itertools.islice(fp, linesInData)
        fp.close()
        dataObject = function_write(data, updatedFile, patterns, linesInData)
        linesInData = dataObject[1]

        basepath = os.path.dirname(__file__)
        filePath = os.path.abspath(os.path.join(basepath, "..", "LifesVitalSigns/static/static_dirs/js/json/N2OData.json"))
        outfile = open(filePath, 'a')
        json.dump(dataObject[0], outfile)
        data = None
        updatedFile = None
        outfile = open('data/N2ODataLines.txt', 'w')
        outfile.write(str(linesInData))
        outfile.close()
    except Exception:
        print('Error updating JSON')


def write_CH4():
    data = {}
    pattern_year = r'[0-9][0-9][0-9][0-9]'
    pattern_ppb = r'[0-9][0-9][0-9][0-9].[0-9][0-9]'
    try:
        fp = open('data/CH4Data.txt')
        linesInData = 0
        for line in fp:
            linesInData += 1
            if not(re.search('#', line)):
                match_year = re.search(pattern_year, line)
                match_ppb = re.search(pattern_ppb, line)
                if match_year is not None:
                    if match_ppb is not None:
                        this_year = match_year.group(0)
                        this_ppb = match_ppb.group(0)
                        data[int(this_year)] = float(this_ppb)

        fp.close()
        basepath = os.path.dirname(__file__)
        filePath = os.path.abspath(os.path.join(basepath, "..", "LifesVitalSigns/static/static_dirs/js/json/CH4Data.json"))
        outfile = open(filePath, 'w')    
        json.dump(data, outfile)
        data = None
        outfile = open('data/CO2DataLines.txt', 'w')
        outfile.write(str(linesInData))
        outfile.close()
    except Exception:
        print("Error retrieving file")


def update_CH4():
    data = {}
    pattern_year = r'[0-9][0-9][0-9][0-9]'
    pattern_ppb = r'[0-9][0-9][0-9][0-9].[0-9][0-9]'
    try:
        fp = open('data/CH4DataLines.txt')
        for line in fp:
            linesInData = int(line)
        fp = open('data/CH4Data.txt')
        updatedFile = itertools.islice(fp, linesInData)
        fp.close()
        for line in updatedFile:
            linesInData += 1
            match_year = re.search(pattern_year, line)
            match_ppb = re.search(pattern_ppb, line)
            if match_year is not None:
                if match_ppb is not None:
                    this_year = match_year.group(0)
                    this_ppb = match_ppb.group(0)
                    data[int(this_year)] = float(this_ppb)

        basepath = os.path.dirname(__file__)
        filePath = os.path.abspath(os.path.join(basepath, "..", "LifesVitalSigns/static/static_dirs/js/json/CH4Data.json"))
        outfile = open(filePath, 'a')
        json.dump(data, outfile)
        data = None
        updatedFile = None
        outfile = open('data/CH4DataLines.txt', 'w')
        outfile.write(str(linesInData))
        outfile.close()
    except Exception:
        print('Error updating JSON')


def write_CFC11():
    data = {}
    pattern_year = r'[0-9][0-9][0-9][0-9]'
    pattern_ppt1 = r'[n0123456789][a0123456789][n0123456789]'
    pattern_ppt2 = r'.[0-9][0-9][0-9]'
    patterns = [pattern_year, pattern_ppt1, pattern_ppt2]
    try:
        fp = open('data/CFC11Data.txt')
        linesInData = 0
        dataObject = function_write(data, fp, patterns, linesInData)
        linesInData = dataObject[1]
        fp.close()

        basepath = os.path.dirname(__file__)
        filePath = os.path.abspath(os.path.join(basepath, "..", "LifesVitalSigns/static/static_dirs/js/json/CFC11Data.json"))
        outfile = open(filePath, 'w')   
        json.dump(dataObject[0], outfile)
        learn_data.average_dataset('CFC11')
        data = None
        outfile = open('data/CFC11DataLines.txt', 'w')
        outfile.write(str(linesInData))
        outfile.close()
    except Exception:
        print("Error retrieving file")


def update_CFC11():
    data = {}
    pattern_year = r'[0-9][0-9][0-9][0-9]'
    pattern_ppt1 = r'[n0123456789][a0123456789][n0123456789]'
    pattern_ppt2 = r'.[0-9][0-9][0-9]'
    patterns = [pattern_year, pattern_ppt1, pattern_ppt2]
    try:
        fp = open('data/CFC11DataLines.txt')
        for line in fp:
            linesInData = int(line)
        fp = open('data/CFC11Data.txt')
        updatedFile = itertools.islice(fp, linesInData)
        fp.close()
        
        dataObject = function_write(data, updatedFile, patterns, linesInData)
        linesInData = dataObject[1]

        basepath = os.path.dirname(__file__)
        filePath = os.path.abspath(os.path.join(basepath, "..", "LifesVitalSigns/static/static_dirs/js/json/CFC11Data.json"))
        outfile = open(filePath, 'a')
        json.dump(dataObject[0], outfile)
        data = None
        updatedFile = None
        outfile = open('data/CFC11DataLines.txt', 'w')
        outfile.write(str(linesInData))
        outfile.close()
    except Exception:
        print('Error updating JSON')


def write_CFC12():
    data = {}
    pattern_year = r'[0-9][0-9][0-9][0-9]'
    pattern_ppt1 = r'[n0123456789][a0123456789][n0123456789]'
    pattern_ppt2 = r'.[0-9][0-9][0-9]'
    patterns = [pattern_year, pattern_ppt1, pattern_ppt2]
    try:
        fp = open('data/CFC12Data.txt')
        linesInData = 0
        dataObject = function_write(data, fp, patterns, linesInData)
        linesInData = dataObject[1]
        fp.close()

        basepath = os.path.dirname(__file__)
        filePath = os.path.abspath(os.path.join(basepath, "..", "LifesVitalSigns/static/static_dirs/js/json/CFC12Data.json"))
        outfile = open(filePath, 'w')  
        json.dump(dataObject[0], outfile)
        learn_data.average_dataset('CFC12')
        data = None
        outfile = open('data/CFC11DataLines.txt', 'w')
        outfile.write(str(linesInData))
        outfile.close()
    except Exception:
        print("Error retrieving file")

def update_CFC12():
    data = {}
    pattern_year = r'[0-9][0-9][0-9][0-9]'
    pattern_ppt1 = r'[n0123456789][a0123456789][n0123456789]'
    pattern_ppt2 = r'.[0-9][0-9][0-9]'
    patterns = [pattern_year, pattern_ppt1, pattern_ppt2]
    try:
        fp = open('data/CFC12DataLines.txt')
        for line in fp:
            linesInData = int(line)
        fp = open('data/CFC12Data.txt')
        updatedFile = itertools.islice(fp, linesInData)
        fp.close()
        
        dataObject = function_write(data, updatedFile, patterns, linesInData)
        linesInData = dataObject[1]

        basepath = os.path.dirname(__file__)
        filePath = os.path.abspath(os.path.join(basepath, "..", "LifesVitalSigns/static/static_dirs/js/json/CFC12Data.json"))
        outfile = open(filePath, 'a')
        json.dump(dataObject[0], outfile)
        data = None
        updatedFile = None
        outfile = open('data/CFC12DataLines.txt', 'w')
        outfile.write(str(linesInData))
        outfile.close()
    except Exception:
        print('Error updating JSON')

def write_Temperature():
    data = {}
    pattern_year = r'[0-9][0-9][0-9][0-9]'
    pattern_temp = r'[-]?[0-9][.][0-9][0-9]'
    try:
        fp = open('data/TemperatureData.txt')
        linesInData = 0
        for line in fp:
            linesInData += 1
            match_year = re.search(pattern_year, line)
            match_temp = re.search(pattern_temp, line)
            if match_year is not None:
                if match_temp is not None:
                    this_year = match_year.group(0)
                    this_temp = match_temp.group(0)
                    data[int(this_year)] = float(this_temp)

        fp.close()
        basepath = os.path.dirname(__file__)
        filePath = os.path.abspath(os.path.join(basepath, "..", "LifesVitalSigns/static/static_dirs/js/json/TemperatureData.json"))
        outfile = open(filePath, 'w')      
        json.dump(data, outfile)
        data = None
        outfile = open('data/CFC12DataLines.txt', 'w')
        outfile.write(str(linesInData))
        outfile.close()
    except Exception:
        print("Error retrieving file")


def update_Temperature():
    data = {}
    pattern_year = r'[0-9][0-9][0-9][0-9]'
    pattern_temp = r'[-]?[0-9][.][0-9][0-9]'
    try:
        fp = open('data/CFC12DataLines.txt')
        for line in fp:
            linesInData = int(line)
        fp = open('data/CFC12Data.txt')
        updatedFile = itertools.islice(fp, linesInData)
        fp.close()
        
        for line in updatedFile:
            linesInData += 1
            match_year = re.search(pattern_year, line)
            match_temp = re.search(pattern_temp, line)
            if match_year is not None:
                if match_temp is not None:
                    this_year = match_year.group(0)
                    this_temp = match_temp.group(0)
                    data[int(this_year)] = float(this_temp)

        basepath = os.path.dirname(__file__)
        filePath = os.path.abspath(os.path.join(basepath, "..", "LifesVitalSigns/static/static_dirs/js/json/CFC12Data.json"))
        outfile = open(filePath, 'a')
        json.dump(data, outfile)
        data = None
        updatedFile = None
        outfile = open('data/CFC12DataLines.txt', 'w')
        outfile.write(str(linesInData))
        outfile.close()
    except Exception:
        print('Error updating JSON')


def update_All():
    update_CO2()
    update_N2O()
    update_CH4()
    update_CFC11()
    update_CFC12()
    update_Temperature()

def write_All():
    basepath = os.path.dirname(__file__)
    path = os.path.abspath(os.path.join(basepath, "..", "LifesVitalSigns/static/static_dirs/js/json"))
    if not os.path.exists(path):
        os.makedirs(path)
    write_CO2()
    write_N2O()
    write_CH4()
    write_CFC11()
    write_CFC12()
    write_Temperature()