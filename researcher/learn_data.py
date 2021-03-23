import json
import datetime
import math
import os
from . import write_data_final

thisDataset = ''

def currentYear():
    currentYear = datetime.datetime.now().year
    return currentYear

def learn_all():
    average_dataset('N2O')
    average_dataset('CFC11')
    average_dataset('CFC12')


    basicProjection('CO2')
    basicProjection('N2O')
    basicProjection('CH4')
    basicProjection('CFC11')
    basicProjection('CFC12')
    basicProjection('Temperature')


    projectTemperature()

def average_dataset(dataset):
    thisYear = currentYear()

    global thisDataset
    if dataset == 'N2O':
        thisDataset = 'N2OData.json'
    if dataset == 'CFC11':
        thisDataset = 'CFC11Data.json'
    if dataset == 'CFC12':
        thisDataset = 'CFC12Data.json'

    basepath = os.getcwd()
    filePath = os.path.abspath(os.path.join(basepath, '..', 'LifesVitalSigns/static/static_dirs/js/json/' + thisDataset))

    data = open(filePath)
    data = json.load(data)
    newData = {}
    beginYear = 1977
    entryIndice = 0
    while beginYear <= thisYear:
        month = 0
        thisSum = 0.0
        while month < 12:
            month +=  1
            try:
                entry = float(data[entryIndice])
                thisSum = thisSum + entry
                entryIndice += 1
            except Exception:
                if month > 1:
                    month = month - 1
                break
        average = thisSum / float(month)
        newData[beginYear] = average
        beginYear = beginYear + 1
    outfile = open(filePath, 'w')
    json.dump(newData, outfile)
    outfile.close()
    data = None
    newData = None

# Unused Calculations, most recent rate of change is used to project future atmospheric composition as opposed to average rate of change
# to reflect changing energy consumption and pollution within this era

# Takes the average rate of change of a dataset over the past 10 years
#def rateOfChange_dataset(dataset):
#    thisDataset = ''
#    if dataset == 'CO2':
#        thisDataset = 'CO2Data.json'
#    if dataset == 'N2O':
#        thisDataset = 'N2OData.json'
#    if dataset == 'CH4':
#        thisDataset = 'CH4Data.json'
#    if dataset == 'CFC11':
#        thisDataset = 'CFC11Data.json'
#    if dataset == 'CFC12':
#        thisDataset = 'CFC12Data.json'
#    if dataset == 'Temperature':
#        thisDataset = 'TemperatureData.json'
#        
#    with open('/home/zer0/Desktop/Github/LVSDjango/LifesVitalSigns/LifesVitalSigns/static/static_dirs/js/json/' + thisDataset) as json_file:
#        data = json.load(json_file)
#
#        changeSet = {}
#        currentYear = currentYear()
#        startYear = currentYear - 10
#
#        while startYear <= currentYear:
#            try:
#                changeSet[startYear] = data[startYear] - data[startYear - 1]
#            startYear = startYear + 1
#        
#        startYear = currentYear - 10
#        sumSet = 0
#        count = 0
#        while startYear <= currentYear:
#            try:
#                sumSet = sumSet + changeSet[startYear]
#            else:
#                count = count + 1
#            startYear = startYear + 1
#        averageChange = float(sumSet) / float(count)
#
#        changeOfChangeSet = {}
#        currentYear = currentYear()
#        startYear = currentYear - 10
#
#        while startYear <= currentYear:
#            try:
#               changeOfChangeSet[startYear] = changeSet[startYear + 1] - changeSet[startYear]
#            startYear = startYear + 1
#
#        startYear = currentYear - 10
#        sumSet = 0
#        count = 0
#        while startYear <= currentYear:
#            try:
#                sumSet = sumSet + changeOfChangeSet[startYear]
#            else:
#                count = count + 1
#            startYear = startYear + 1
#        averageChangeOfChange = float(sumSet) / float(count)
#
#    changes = {'averageRateOfChange' : averageChange , 'averageRateOfChangeOfRateOfChange' : averageChangeOfChange}
#
#    return changes


# Only Basic Projections regarding atmospheric composition are directly shown to the user.
# Atmospheric projections are then used to model Earth's Temperature using a relationship defined by the IPCC
def basicProjection(dataset):
    global thisDataset
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
        thisDataset = 'TemperatureData/json'

    projectedSet = {}
    startYear = currentYear()
    thisYear = currentYear()
    endYear = currentYear + 100

    basepath = os.getcwd()
    filePath = os.path.abspath(os.path.join(basepath, '..', 'LifesVitalSigns/static/static_dirs/js/json/' + thisDataset))

    data = open(filePath)
    data = json.load(data)
        
    startLoad = ""
    counter = 0
    while len(startLoad) < 2:
        try:
            startLoad = data[thisYear + counter]
            startLoad = str(startLoad)
            startYear = thisYear + counter
        except KeyError:
            counter = counter - 1

    startLoad = float(startLoad)
    precedingLoad = float(data[(startYear) - 1])
    changeInLoad = startLoad - precedingLoad
    projectedSet[startYear + 1] = startLoad + changeInLoad
    startYear += 2
    while startYear <= endYear:
        projectedSet[startYear] = projectedSet[startYear - 1] + changeInLoad
        startYear += 1

    outfile = open('/home/zer0/Desktop/Github/LVSDjango/LifesVitalSigns/LifesVitalSigns/static/static_dirs/js/json/' + 
        thisDataset + 'BasicProjection.json', 'w')
    json.dump(projectedSet, outfile)
    outfile.close()
    data = None



# Calculates the Radiative Forcing or Flux using the relationship defined by the National Oceanic and Atmospheric Administration(NOAA)
# https://www.esrl.noaa.gov/gmd/aggi/aggi.html
def calculateChangeInRadiativeFlux(searchYear):
    thisYear = currentYear()
    basepath = os.getcwd()
    filePath = os.path.abspath(os.path.join(basepath, '..', 'LifesVitalSigns/static/static_dirs/js/json/'))

    # Contains initial values of: CO2 PPM, N2O PPB, CH4 PPB, CFC-11 PPT, CFC-12 PPT
    initialValues = []
    # Contains final values of: CO2 PPM, N2O PPB, CH4 PPB, CFC-11 PPT, CFC-12 PPT
    finalValues = []
    # Contains the changes in radiative flux due to: CO2, N2O, CH4, CFC-11, CFC-12
    changesInRadiativeFlux = []
    
    datasets = ['CO2', 'N2O', 'CH4', 'CFC11', 'CFC12']
    thisSet = 0

    if searchYear < thisYear:

        for eachSet in datasets:
            with open(filePath + eachSet +'Data.json') as json_file:
                data = json.load(json_file)

                finalValues[thisSet] = data[searchYear]
                initialValues[thisSet] = data[searchYear - 1]
                thisSet += 1

    if searchYear > thisYear:

        for eachSet in datasets:
            with open(filePath + eachSet +'DataBasicProjection.json') as json_file:
                data = json.load(json_file)

                finalValues[thisSet] = data[searchYear]
                initialValues[thisSet] = data[searchYear - 1]
                thisSet += 1
    
    if searchYear == thisYear:

        for eachSet in datasets:
            with open(filePath + eachSet + 'DataBasicProjection.json') as json_file:
                data = json.load(json_file)

                finalValues[thisSet] = data[searchYear]
                with open(filePath + datasets[thisSet] +'Data.json') as json_file:
                    data = json.load(json_file)
                    initialValues[thisSet] = data[searchYear - 1]
                    thisSet += 1

    changesInRadiativeFlux[0] = calculateChangeInRadiativeFluxDueToCO2(initialValues[0], finalValues[0])
    changesInRadiativeFlux[1] = calculateChangeInRadiativeFluxDueToN2O(initialValues[1], finalValues[1], initialValues[2])
    changesInRadiativeFlux[2] = calculateChangeInRadiativeFluxDueToCH4(initialValues[1], initialValues[2], finalValues[2])
    changesInRadiativeFlux[3] = calculateChangeInRadiativeFluxDueToCFC11(initialValues[3], finalValues[3])
    changesInRadiativeFlux[4] = calculateChangeInRadiativeFluxDueToCFC12(initialValues[4], finalValues[4])
 
    changeInRadiativeFlux = changesInRadiativeFlux[0] + changesInRadiativeFlux[1] + changesInRadiativeFlux[2] + \
        changesInRadiativeFlux[3] + changesInRadiativeFlux[4]
    
    return changeInRadiativeFlux

def calculateChangeInRadiativeFluxDueToCO2(initialCO2PPM, finalCO2PPM):
    return (5.35) * math.log((finalCO2PPM / initialCO2PPM))

def calculateChangeInRadiativeFluxDueToN2O(initialN2OPPB, finalN2OPPB, initialCH4PPB):
    return ( (0.12) * ( (finalN2OPPB ** (0.5)) - (initialN2OPPB ** (0.5)) ) ) - ( functionInterdependence(initialCH4PPB,finalN2OPPB) - 
        functionInterdependence(initialCH4PPB,initialN2OPPB) )

def calculateChangeInRadiativeFluxDueToCH4(initialN2OPPB, initialCH4PPB, finalCH4PPB):
    return ( (0.036) * ( (finalCH4PPB ** (0.5)) - (initialCH4PPB ** (0.5)) ) ) - ( functionInterdependence(finalCH4PPB,initialN2OPPB) - 
        functionInterdependence(initialCH4PPB,initialN2OPPB) )

def calculateChangeInRadiativeFluxDueToCFC11(initialCFC11PPT, finalCFC11PPT):
    return (0.25) * (finalCFC11PPT - initialCFC11PPT)

def calculateChangeInRadiativeFluxDueToCFC12(initialCFC12PPT, finalCFC12PPT):
    return (0.32) * (finalCFC12PPT - initialCFC12PPT)

def functionInterdependence(CH4PPB, N2OPBB):
    return ( (0.47) * math.log(1 + ( ( (2.01) * ( (10) ** (-5) ) ) * ( ( (CH4PPB) * (N2OPBB) ) ** (0.75) ) ) +
        ( ( (5.31) * ( (10) ** (-15) ) ) * (CH4PPB) * ( ( (CH4PPB) * (N2OPBB) ) ** (1.52) ) ) ) )

def calculateChangeInTemperature(searchYear):
    basepath = os.path.dirname(__file__)
    filePath = os.path.abspath(os.path.join(basepath, '..', 'LifesVitalSigns/static/static_dirs/js/json/'))
    with open(filePath + 'TemperatureData.json') as json_file:
        data = json.load(json_file)

        finalTemp = data[searchYear]
        initialTemp = data[searchYear - 1]
        changeInTemperature = finalTemp - initialTemp
        return changeInTemperature

def calculateChangeOfChangeInTemperature(searchYear):
    finalChange = calculateChangeInTemperature(searchYear)
    initialChange = calculateChangeInTemperature(searchYear - 1)
    changeOfChangeInTemperature = finalChange - initialChange
    return changeOfChangeInTemperature

def calculateClimateSensitivityParameter():
    lowestCommonYear = write_data_final.findCommonStartYear() + 1
    highestCommonYear = write_data_final.findCommonEndYear()

    counter = 0
    sumClimateSensitivityParameter = 0
    startYear = lowestCommonYear
    while startYear < highestCommonYear:
        changeOfChangeInTemperature = calculateChangeOfChangeInTemperature(startYear)
        changeInRadiativeFlux = calculateChangeInRadiativeFlux(startYear)
        sumClimateSensitivityParameter += changeOfChangeInTemperature / changeInRadiativeFlux
        startYear += 1
        counter += 1

    climateSensitivityParameter = sumClimateSensitivityParameter / counter
    return climateSensitivityParameter

def calculateChangeInClimateSensitivityParameter(searchYear):
    changeOfChangeInTemperatureFinal = calculateChangeOfChangeInTemperature(searchYear)
    changeInRadiativeFluxFinal = calculateChangeInRadiativeFlux(searchYear)

    finalClimateSensitivityParameter = changeOfChangeInTemperatureFinal / changeInRadiativeFluxFinal

    changeOfChangeInTemperatureInitial = calculateChangeOfChangeInTemperature(searchYear - 1)
    changeInRadiativeFluxInitial = calculateChangeInRadiativeFlux(searchYear - 1)

    initialClimateSensitivityParameter = changeOfChangeInTemperatureInitial / changeInRadiativeFluxInitial

    changeInClimateSensitivityParameter = finalClimateSensitivityParameter - initialClimateSensitivityParameter
    return changeInClimateSensitivityParameter




# Models Earth's Temperature using the relationship defined between an instantaneous change in net radiative flux and global mean surface temperature
# Outlined in Section 8.1.1.1 of the Fifth Assessment of the IPCC

# Myhre, G., D. Shindell, F.-M. Bréon, W. Collins, J. Fuglestvedt, J. Huang, D. Koch, J.-F. Lamarque, D. Lee, B. Mendoza, T. Nakajima, A. Robock, G. Stephens,
# T. Takemura and H. Zhang, 2013: Anthropogenic and Natural Radiative Forcing. In: Climate Change 2013: The Physical Science Basis. Contribution of Working 
# Group I to the Fifth Assessment Report of the Intergovernmental Panel on Climate Change [Stocker, T.F., D. Qin, G.-K. Plattner, M. Tignor, S.K. Allen, 
# J. Boschung, A. Nauels, Y. Xia, V. Bex and P.M. Midgley (eds.)]. Cambridge University Press, Cambridge, United Kingdom and New York, NY, USA

# https://www.ipcc.ch/site/assets/uploads/2018/02/WG1AR5_Chapter08_FINAL.pdf
# ---------------------------------------------------------------------------------------------------
# Projects temperature for the year succeeding real data,
# calculates the change in Radiative Flux and Climate Sensitivity Parameter; to project the succeeding years' temperature in a continuous fashion.
# Changes in radiative flux are a function of projected changes in atmospheric composition
# Changes in the Climate Sensitivity Parameter are a function of projected changes in radiatve flux and the rate of change of the rate of change of temperature
def projectTemperature():
    #basepath = os.path.dirname(__file__)
    basepath = os.getcwd()
    filePath = os.path.abspath(os.path.join(basepath, '..', 'LifesVitalSigns/static/static_dirs/js/json/'))
    startYear = currentYear()
    nextCentury = startYear + 100
    changesOfChangeInTemperature = {}
    changesOfClimateSensitivityParameter = {}

    changesOfChangeInTemperature[startYear] = (calculateChangeInClimateSensitivityParameter(startYear - 1)) * (calculateChangeInRadiativeFlux(startYear - 1))
  
    
    changeOfChangeInTemperatureFinal = changesOfChangeInTemperature[startYear]
    changeInRadiativeFluxFinal = calculateChangeInRadiativeFlux(startYear)

    finalClimateSensitivityParameter = changeOfChangeInTemperatureFinal / changeInRadiativeFluxFinal

    changeOfChangeInTemperatureInitial = calculateChangeOfChangeInTemperature(startYear - 1)
    changeInRadiativeFluxInitial = calculateChangeInRadiativeFlux(startYear - 1)

    initialClimateSensitivityParameter = changeOfChangeInTemperatureInitial / changeInRadiativeFluxInitial

    changesOfClimateSensitivityParameter[startYear] = finalClimateSensitivityParameter - initialClimateSensitivityParameter
        
    startYear +=  1
    changesOfChangeInTemperature[startYear] = (changesOfClimateSensitivityParameter[startYear - 1]) * (calculateChangeInRadiativeFlux(startYear - 1))

    while startYear <= nextCentury:
        changeOfChangeInTemperatureFinal = changesOfChangeInTemperature[startYear]
        changeInRadiativeFluxFinal = calculateChangeInRadiativeFlux(startYear)

        finalClimateSensitivityParameter = changeOfChangeInTemperatureFinal / changeInRadiativeFluxFinal

        changeOfChangeInTemperatureInitial = changesOfChangeInTemperature[startYear - 1]
        changeInRadiativeFluxInitial = calculateChangeInRadiativeFlux(startYear - 1)

        initialClimateSensitivityParameter = changeOfChangeInTemperatureInitial / changeInRadiativeFluxInitial

        changesOfClimateSensitivityParameter[startYear] = finalClimateSensitivityParameter - initialClimateSensitivityParameter
        
        startYear +=  1
        changesOfChangeInTemperature[startYear] = (changesOfClimateSensitivityParameter[startYear - 1]) * (calculateChangeInRadiativeFlux(startYear - 1))
    
    outfile = open(filePath + 'TemperatureProjection.json', 'w')
    json.dump(changesOfChangeInTemperature, outfile)
