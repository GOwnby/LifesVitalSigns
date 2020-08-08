import json
import datetime
import write_data_final

def currentYear():
    return datetime.datetime.now().year

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
    thisDataset = ''
    if dataset == 'N2O':
        thisDataset = 'N2OData.json'
    if dataset == 'CFC11':
        thisDataset = 'CFC11Data.json'
    if dataset == 'CFC12':
        thisDataset = 'CFC12Data.json'

    with open('/home/zer0/Desktop/Github/LVSDjango/LifesVitalSigns/LifesVitalSigns/static/static_dirs/js/json/' + thisDataset) as json_file:
        data = json.load(json_file)
        newData = {}
        beginYear = 1977
        currentYear = currentYear()
        while beginYear <= currentYear:
            currentSet = {}
            month = 1
            while month <= 12:
                try:
                    entry = data[(str(beginYear) + '_' + str(month))]
                    currentSet[month] = entry
                month = month + 1
            countMonth = 1
            sum = 0.0
            while countMonth <= 12:
                sum = sum + currentSet[countMonth]
                countMonth = countMonth + 1
            countMonth = 0
            for each in currentSet:
                countMonth = countMonth + 1
            average = sum / float(countMonth)
            newData[beginYear] = average
            beginYear = beginYear + 1
    outfile = open('/home/zer0/Desktop/Github/LVSDjango/LifesVitalSigns/LifesVitalSigns/static/static_dirs/js/json/' + thisDataset, 'w')
    json.dump(newData, outfile)

# Unused Calculations, most recent rate of change is used to project future atmospheric composition as opposed to average rate of change
# to reflect changing energy consumption and pollution within this era
'''
# Takes the average rate of change of a dataset over the past 10 years
def rateOfChange_dataset(dataset):
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
        
    with open('/home/zer0/Desktop/Github/LVSDjango/LifesVitalSigns/LifesVitalSigns/static/static_dirs/js/json/' + thisDataset) as json_file:
        data = json.load(json_file)

        changeSet = {}
        currentYear = currentYear()
        startYear = currentYear - 10

        while startYear <= currentYear:
            try:
                changeSet[startYear] = data[startYear] - data[startYear - 1]
            startYear = startYear + 1
        
        startYear = currentYear - 10
        sumSet = 0
        count = 0
        while startYear <= currentYear:
            try:
                sumSet = sumSet + changeSet[startYear]
            else:
                count = count + 1
            startYear = startYear + 1
        averageChange = float(sumSet) / float(count)

        changeOfChangeSet = {}
        currentYear = currentYear()
        startYear = currentYear - 10

        while startYear <= currentYear:
            try:
                changeOfChangeSet[startYear] = changeSet[startYear + 1] - changeSet[startYear]
            startYear = startYear + 1

        startYear = currentYear - 10
        sumSet = 0
        count = 0
        while startYear <= currentYear:
            try:
                sumSet = sumSet + changeOfChangeSet[startYear]
            else:
                count = count + 1
            startYear = startYear + 1
        averageChangeOfChange = float(sumSet) / float(count)

    changes = {'averageRateOfChange' : averageChange , 'averageRateOfChangeOfRateOfChange' : averageChangeOfChange}

    return changes
'''

# Only Basic Projections regarding atmospheric composition are directly shown to the user.
# Atmospheric projections are then used to model Earth's Temperature using a relationship defined by the IPCC
def basicProjection(dataset):
    thisDataset = ''
    if dataset == 'CO2':
        thisDataset = 'CO2Data'
    if dataset == 'N2O':
        thisDataset = 'N2OData'
    if dataset == 'CH4':
        thisDataset = 'CH4Data'
    if dataset == 'CFC11':
        thisDataset = 'CFC11Data'
    if dataset == 'CFC12':
        thisDataset = 'CFC12Data'
    if dataset == 'Temperature':
        thisDataset = 'TemperatureData'

    projectedSet = {}
    currentYear = currentYear()
    startYear = currentYear()
    endYear = currentYear() + 100

    with open('/home/zer0/Desktop/Github/LVSDjango/LifesVitalSigns/LifesVitalSigns/static/static_dirs/js/json/' + thisDataset + '.json') as json_file:
        data = json.load(json_file)
        
        startLoad = ""
        counter = 0
        while len(startLoad) < 2:
            try:
                startLoad = data[currentYear + counter]
                startLoad = str(startLoad)
                startYear = currentYear + counter
            except:
                counter = counter - 1

        startLoad = float(startLoad)
        precedingLoad = float(data[(currentYear + counter) - 1])
        changeInLoad = startLoad - precedingLoad
        projectedSet[currentYear] = startLoad + changeInLoad
        currentYear += 1
        while currentYear <= endYear:
            projectedSet[currentYear] = projectedSet[currentYear - 1] + changeInLoad
            currentYear += 1

    outfile = open('/home/zer0/Desktop/Github/LVSDjango/LifesVitalSigns/LifesVitalSigns/static/static_dirs/js/json/' + thisDataset + 'BasicProjection.json', 'w')
    json.dump(projectedSet, outfile)


'''
Calculates the Radiative Forcing or Flux using the relationship defined by the National Oceanic and Atmospheric Administration(NOAA)

https://www.esrl.noaa.gov/gmd/aggi/aggi.html
'''
def calculateChangeInRadiativeFlux(searchYear):
    thisYear = currentYear()

    if searchYear < thisYear:

        with open('/home/zer0/Desktop/Github/LVSDjango/LifesVitalSigns/LifesVitalSigns/static/static_dirs/js/json/CO2Data.json') as json_file:
            data = json.load(json_file)

            finalCO2PPM = data[searchYear]
            initialCO2PPM = data[searchYear - 1]
            changeDueToCO2 = (5.35) * math.log((finalCO2PPM / initialCO2PPM))

        with open('/home/zer0/Desktop/Github/LVSDjango/LifesVitalSigns/LifesVitalSigns/static/static_dirs/js/json/N2OData.json') as json_file:
            data = json.load(json_file)

            finalN2OPPB = data[searchYear]
            initialN2OPPB = data[searchYear - 1]
            changeDueToN2O = ( (0.12) * ( (finalN2OPPB ** (0.5)) - (initialN2OPPB ** (0.5)) ) ) - ( functionInterdependence(initialCH4PPB,finalN2OPPB) -
                functionInterdependence(initialCH4PPB,initialN2OPPB) )

        with open('/home/zer0/Desktop/Github/LVSDjango/LifesVitalSigns/LifesVitalSigns/static/static_dirs/js/json/CH4Data.json') as json_file:
            data = json.load(json_file)

            finalCH4PPB = data[searchYear]
            initialCH4PPB = data[searchYear - 1]
            changeDueToCH4 = ( (0.036) * ( (finalCH4PPB ** (0.5)) - (initialCH4PPB ** (0.5)) ) ) - ( functionInterdependence(finalCH4PPB,initialN2OPPB) -
                functionInterdependence(initialCH4PPB,initialN2OPPB) )

        with open('/home/zer0/Desktop/Github/LVSDjango/LifesVitalSigns/LifesVitalSigns/static/static_dirs/js/json/CFC11Data.json') as json_file:
            data = json.load(json_file)

            finalCFC11PPT = data[searchYear]
            initialCFC11PPT = data[searchYear - 1]
            changeDueToCFC11 = (0.25) * (finalCFC11PPT - initialCFC11PPT)

        with open('/home/zer0/Desktop/Github/LVSDjango/LifesVitalSigns/LifesVitalSigns/static/static_dirs/js/json/CFC12Data.json') as json_file:
            data = json.load(json_file)

            finalCFC12PPT = data[searchYear]
            initialCFC12PPT = data[searchYear - 1]
            changeDueToCFC12 = (0.32) * (finalCFC12PPT - initialCFC12PPT)

    else if searchYear > thisYear:

        with open('/home/zer0/Desktop/Github/LVSDjango/LifesVitalSigns/LifesVitalSigns/static/static_dirs/js/json/CO2DataBasicProjection.json') as json_file:
            data = json.load(json_file)

            finalCO2PPM = data[searchYear]
            initialCO2PPM = data[searchYear - 1]
            changeDueToCO2 = (5.35) * math.log((finalCO2PPM / initialCO2PPM))

        with open('/home/zer0/Desktop/Github/LVSDjango/LifesVitalSigns/LifesVitalSigns/static/static_dirs/js/json/N2ODataBasicProjection.json') as json_file:
            data = json.load(json_file)

            finalN2OPPB = data[searchYear]
            initialN2OPPB = data[searchYear - 1]
            changeDueToN2O = ( (0.12) * ( (finalN2OPPB ** (0.5)) - (initialN2OPPB ** (0.5)) ) ) - ( functionInterdependence(initialCH4PPB,finalN2OPPB) -
                functionInterdependence(initialCH4PPB,initialN2OPPB) )

        with open('/home/zer0/Desktop/Github/LVSDjango/LifesVitalSigns/LifesVitalSigns/static/static_dirs/js/json/CH4DataBasicProjection.json') as json_file:
            data = json.load(json_file)

            finalCH4PPB = data[searchYear]
            initialCH4PPB = data[searchYear - 1]
            changeDueToCH4 = ( (0.036) * ( (finalCH4PPB ** (0.5)) - (initialCH4PPB ** (0.5)) ) ) - ( functionInterdependence(finalCH4PPB,initialN2OPPB) -
                functionInterdependence(initialCH4PPB,initialN2OPPB) )

        with open('/home/zer0/Desktop/Github/LVSDjango/LifesVitalSigns/LifesVitalSigns/static/static_dirs/js/json/CFC11DataBasicProjection.json') as json_file:
            data = json.load(json_file)

            finalCFC11PPT = data[searchYear]
            initialCFC11PPT = data[searchYear - 1]
            changeDueToCFC11 = (0.25) * (finalCFC11PPT - initialCFC11PPT)

        with open('/home/zer0/Desktop/Github/LVSDjango/LifesVitalSigns/LifesVitalSigns/static/static_dirs/js/json/CFC12DataBasicProjection.json') as json_file:
            data = json.load(json_file)

            finalCFC12PPT = data[searchYear]
            initialCFC12PPT = data[searchYear - 1]
            changeDueToCFC12 = (0.32) * (finalCFC12PPT - initialCFC12PPT)
    
    else if searchYear == thisYear:

        with open('/home/zer0/Desktop/Github/LVSDjango/LifesVitalSigns/LifesVitalSigns/static/static_dirs/js/json/CO2DataBasicProjection.json') as json_file:
            data = json.load(json_file)

            finalCO2PPM = data[searchYear]
            with open('/home/zer0/Desktop/Github/LVSDjango/LifesVitalSigns/LifesVitalSigns/static/static_dirs/js/json/CO2Data.json') as json_file:
                data = json.load(json_file)
                initialCO2PPM = data[searchYear - 1]
                changeDueToCO2 = (5.35) * math.log((finalCO2PPM / initialCO2PPM))

        with open('/home/zer0/Desktop/Github/LVSDjango/LifesVitalSigns/LifesVitalSigns/static/static_dirs/js/json/N2ODataBasicProjection.json') as json_file:
            data = json.load(json_file)

            finalN2OPPB = data[searchYear]
            with open('/home/zer0/Desktop/Github/LVSDjango/LifesVitalSigns/LifesVitalSigns/static/static_dirs/js/json/N2OData.json') as json_file:
                data = json.load(json_file)
                initialN2OPPB = data[searchYear - 1]
                changeDueToN2O = ( (0.12) * ( (finalN2OPPB ** (0.5)) - (initialN2OPPB ** (0.5)) ) ) - ( functionInterdependence(initialCH4PPB,finalN2OPPB) -
                    functionInterdependence(initialCH4PPB,initialN2OPPB) )

        with open('/home/zer0/Desktop/Github/LVSDjango/LifesVitalSigns/LifesVitalSigns/static/static_dirs/js/json/CH4DataBasicProjection.json') as json_file:
            data = json.load(json_file)

            finalCH4PPB = data[searchYear]
            with open('/home/zer0/Desktop/Github/LVSDjango/LifesVitalSigns/LifesVitalSigns/static/static_dirs/js/json/CH4Data.json') as json_file:
                data = json.load(json_file)
                initialCH4PPB = data[searchYear - 1]
                changeDueToCH4 = ( (0.036) * ( (finalCH4PPB ** (0.5)) - (initialCH4PPB ** (0.5)) ) ) - ( functionInterdependence(finalCH4PPB,initialN2OPPB) -
                    functionInterdependence(initialCH4PPB,initialN2OPPB) )

        with open('/home/zer0/Desktop/Github/LVSDjango/LifesVitalSigns/LifesVitalSigns/static/static_dirs/js/json/CFC11DataBasicProjection.json') as json_file:
            data = json.load(json_file)

            finalCFC11PPT = data[searchYear]
            with open('/home/zer0/Desktop/Github/LVSDjango/LifesVitalSigns/LifesVitalSigns/static/static_dirs/js/json/CFC11Data.json') as json_file:
                data = json.load(json_file)
                initialCFC11PPT = data[searchYear - 1]
                changeDueToCFC11 = (0.25) * (finalCFC11PPT - initialCFC11PPT)

        with open('/home/zer0/Desktop/Github/LVSDjango/LifesVitalSigns/LifesVitalSigns/static/static_dirs/js/json/CFC12DataBasicProjection.json') as json_file:
            data = json.load(json_file)

            finalCFC12PPT = data[searchYear]
            with open('/home/zer0/Desktop/Github/LVSDjango/LifesVitalSigns/LifesVitalSigns/static/static_dirs/js/json/CFC12DataBasicProjection.json') as json_file:
                data = json.load(json_file)
                initialCFC12PPT = data[searchYear - 1]
                changeDueToCFC12 = (0.32) * (finalCFC12PPT - initialCFC12PPT)



    changeInRadiativeFlux = changeDueToCO2 + changeDueToN2O + changeDueToCH4 + changeDueToCFC11 + changeDueToCFC12
    return changeInRadiativeFlux

def functionInterdependence(CH4PPB, N2OPBB):
    return ( (0.47) * math.log(1 + ( ( (2.01) * ( (10) ** (-5) ) ) * ( ( (CH4PPB) * (N2OPBB) ) ** (0.75) ) ) +
        ( ( (5.31) * ( (10) ** (-15) ) ) * (CH4PPB) * ( ( (CH4PPB) * (N2OPBB) ) ** (1.52) ) ) ) )


def calculateChangeInTemperature(searchYear):
    with open('/home/zer0/Desktop/Github/LVSDjango/LifesVitalSigns/LifesVitalSigns/static/static_dirs/js/json/TemperatureData.json') as json_file:
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
    calculateChangeOfChangeInTemperature()
    lowestCommonYear = write_data.findCommonStartYear() + 1
    highestCommonYear = write_data.findCommonEndYear()

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



'''
Models Earth's Temperature using the relationship defined between an instantaneous change in net radiative flux and global mean surface temperature
Outlined in Section 8.1.1.1 of the Fifth Assessment of the IPCC

Myhre, G., D. Shindell, F.-M. Bréon, W. Collins, J. Fuglestvedt, J. Huang, D. Koch, J.-F. Lamarque, D. Lee, B. Mendoza, T. Nakajima, A. Robock, G. Stephens,
T. Takemura and H. Zhang, 2013: Anthropogenic and Natural Radiative Forcing. In: Climate Change 2013: The Physical Science Basis. Contribution of Working 
Group I to the Fifth Assessment Report of the Intergovernmental Panel on Climate Change [Stocker, T.F., D. Qin, G.-K. Plattner, M. Tignor, S.K. Allen, 
J. Boschung, A. Nauels, Y. Xia, V. Bex and P.M. Midgley (eds.)]. Cambridge University Press, Cambridge, United Kingdom and New York, NY, USA

https://www.ipcc.ch/site/assets/uploads/2018/02/WG1AR5_Chapter08_FINAL.pdf
'''
# Projects temperature for the year succeeding real data,
# calculates the change in Radiative Flux and Climate Sensitivity Parameter; to project the succeeding years' temperature in a continuous fashion.
# Changes in radiative flux are a function of projected changes in atmospheric composition
# Changes in the Climate Sensitivity Parameter are a function of projected changes in radiatve flux and the rate of change of the rate of change of temperature
def projectTemperature():
    startYear = currentYear()
    nextCentury = startYear + 100
    changesOfChangeInTemperature = {}
    changesOfClimateSensitivityParameter = {}
    changesOfRadiativeFlux = {}

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
    
    outfile = open('/home/zer0/Desktop/Github/LVSDjango/LifesVitalSigns/LifesVitalSigns/static/static_dirs/js/json/TemperatureProjection.json', 'w')
    json.dump(changesOfChangeInTemperature, outfile)

        




