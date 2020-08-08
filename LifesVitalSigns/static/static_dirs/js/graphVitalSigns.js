google.charts.load('45', {
    packages:['corechart']
});

    var chart;
    var data;
    var options;

    function draw() {
        chart = new google.visualization.LineChart(document.getElementById('linechart_'));

        chart.draw(data, options);
    }

    function loadCO2() {

        data = new google.visualization.DataTable();

        data.addColumn('string', 'Year');
        data.addColumn('number', 'CO2 Actual');
        data.addColumn('number', 'CO2 Projected');


        year = new Date().getFullYear();
        latestDataYear = 0;
        if (CO2Data.hasOwnProperty(year.toString())){
            latestDataYear = year;
        } else if (CO2Data.hasOwnProperty((year - 1).toString())){
            latestDataYear = (year - 1);
        } else if (CO2Data.hasOwnProperty((year - 2).toString())){
            latestDataYear = (year - 2);
        } else if (CO2Data.hasOwnProperty((year - 3).toString())){
            latestDataYear = (year - 3);
        } else {
            latestDataYear = 2018;
        }

        
        for (i = 1959; i < latestDataYear ; i = i + 1)
        {
           stringI = i.toString();
           data.addRow([stringI, CO2Data[i], null ]);
        }

        data.addRow([latestDataYear.toString(), CO2Data[latestDataYear], CO2Data[latestDataYear] ]);

        
        var yearRangeRateOfChange = document.getElementById('CO2Range').value;
        var annualChangeOfRateOfChange = document.getElementById('CO2Change').value;
        var signSelector = document.getElementById('SignSelectCO2').value;
        var checkboxes = document.getElementsByName('CO2Selector');

        var preset = false;
        preset = listenToCO2Advanced();


        if (preset) {

            var checkedValue = 0;
            for(var i=0,l=checkboxes.length;i<l;i++)
            {
                if(checkboxes[i].checked)
                {
                    if (i == 0) {checkedValue = 1;}
                    if (i == 1) {checkedValue = 2;}
                }
            }

            if (checkedValue == 1) {
                rateOfChangeLatest = (CO2Data[latestDataYear] - CO2Data[(latestDataYear - 1)]);
                rateOfChangeLatestSubTen = (CO2Data[(latestDataYear - 10)] - CO2Data[(latestDataYear - 11)]);
                decadeChangeOfRateOfChange = rateOfChangeLatest / rateOfChangeLatestSubTen; 
                if (decadeChangeOfRateOfChange >= 1) {
                    annualChangeOfRateOfChange = (((decadeChangeOfRateOfChange - Math.floor(decadeChangeOfRateOfChange)) / 10.0) + 1);
                } else if (decadeChangeOfRateOfChange < 1) {
                    annualChangeOfRateOfChange = (1 - ((1 - decadeChangeOfRateOfChange) / 10.0));
                }
                rateOfChange = ((CO2Data[latestDataYear] - CO2Data[latestDataYear - 9]) / 10.0);  
            } else if (checkedValue == 2) {
                rateOfChangeLatest = (CO2Data[latestDataYear] - CO2Data[(latestDataYear - 1)]);
                rateOfChangeLatestSubFifty = (CO2Data[(latestDataYear - 50)] - CO2Data[(latestDataYear - 51)]);
                fifthChangeOfRateOfChange = rateOfChangeLatest / rateOfChangeLatestSubFifty; 
                if (fifthChangeOfRateOfChange >= 1) {
                    annualChangeOfRateOfChange = (((fifthChangeOfRateOfChange - Math.floor(fifthChangeOfRateOfChange)) / 50.0) + 1);
                } else if (fifthChangeOfRateOfChange < 1) {
                    annualChangeOfRateOfChange = (1 - ((1 - fifthChangeOfRateOfChange) / 50.0));
                }
                rateOfChange = ((CO2Data[latestDataYear] - CO2Data[latestDataYear - 49]) / 50.0);  

            }
        } else {
            
            if (!(yearRangeRateOfChange.length > 0)) {
                yearRangeRateOfChange = 10;
            }
            yearRangeRateOfChange = parseInt(yearRangeRateOfChange);

            if (!(annualChangeOfRateOfChange.length > 0)) {
                annualChangeOfRateOfChange = 0;
            }
        

            if (signSelector == "positive") {
                annualChangeOfRateOfChange = (1 + ((parseFloat(annualChangeOfRateOfChange)) * 0.01));
            } else if (signSelector == "negative") {
                annualChangeOfRateOfChange = (1 - ((parseFloat(annualChangeOfRateOfChange)) * 0.01));
            }

            rateOfChange = (CO2Data[latestDataYear] - CO2Data[latestDataYear - yearRangeRateOfChange])/yearRangeRateOfChange;
        }



        value = CO2Data[latestDataYear]
        for (i = latestDataYear + 1; i < latestDataYear + 50; i = i + 1) {
            stringI = i.toString();
            rateOfChange = rateOfChange * (annualChangeOfRateOfChange);
            value = value + rateOfChange;
            data.addRow([stringI, null, value ]);
        }

        options = {
            title: 'Carbon Dioxide (ppm) vs Time (Years)',
            curveType: 'function',
            legend: {position: 'bottom'},
            width: 900,
            height: 500,
            series :
                {
                    1: { lineDashStyle: [10, 2] }
                }
        };
    }



    function loadTemperature() {

        data = new google.visualization.DataTable();

        data.addColumn('string', 'Year');
        data.addColumn('number', 'Temperature Average Actual');
        data.addColumn('number', 'Temperature Average Projected');


        year = new Date().getFullYear();
        latestDataYear = 0;
        if (TemperatureData.hasOwnProperty(year.toString())){
            latestDataYear = year;
        } else if (TemperatureData.hasOwnProperty((year - 1).toString())){
            latestDataYear = (year - 1);
        } else if (TemperatureData.hasOwnProperty((year - 2).toString())){
            latestDataYear = (year - 2);
        } else if (TemperatureData.hasOwnProperty((year - 3).toString())){
            latestDataYear = (year - 3);
        } else {
            latestDataYear = 2018;
        }

        
        for (i = 1880; i < latestDataYear ; i = i + 1)
        {
           stringI = i.toString();
           data.addRow([stringI, TemperatureData[i], null ]);
        }

        data.addRow([latestDataYear.toString(), TemperatureData[latestDataYear], TemperatureData[latestDataYear] ]);

        
        var yearRangeRateOfChange = document.getElementById('TemperatureRange').value;
        var annualChangeOfRateOfChange = document.getElementById('TemperatureChange').value;
        var signSelector = document.getElementById('SignSelectTemperature').value;
        var checkboxes = document.getElementsByName('TempSelector');

        var preset = false;
        preset = listenToTemperatureAdvanced();


        if (preset) {

            var checkedValue = 0;
            for(var i=0,l=checkboxes.length;i<l;i++)
            {
                if(checkboxes[i].checked)
                {
                    if (i == 0) {checkedValue = 1;}
                    if (i == 1) {checkedValue = 2;}
                }
            }

            if (checkedValue == 1) {
                rateOfChangeLatest = (TemperatureData[latestDataYear] - TemperatureData[(latestDataYear - 1)]);
                rateOfChangeLatestSubTen = (TemperatureData[(latestDataYear - 10)] - TemperatureData[(latestDataYear - 11)]);
                decadeChangeOfRateOfChange = rateOfChangeLatest / rateOfChangeLatestSubTen; 
                if (decadeChangeOfRateOfChange >= 1) {
                    annualChangeOfRateOfChange = (((decadeChangeOfRateOfChange - Math.floor(decadeChangeOfRateOfChange)) / 10.0) + 1);
                } else if (decadeChangeOfRateOfChange < 1) {
                    annualChangeOfRateOfChange = (1 - ((1 - decadeChangeOfRateOfChange) / 10.0));
                }
                rateOfChange = ((TemperatureData[latestDataYear] - TemperatureData[latestDataYear - 9]) / 10.0);  
            } else if (checkedValue == 2) {
                rateOfChangeLatest = (TemperatureData[latestDataYear] - TemperatureData[(latestDataYear - 1)]);
                rateOfChangeLatestSubFifty = (TemperatureData[(latestDataYear - 50)] - TemperatureData[(latestDataYear - 51)]);
                fifthChangeOfRateOfChange = rateOfChangeLatest / rateOfChangeLatestSubFifty; 
                if (fifthChangeOfRateOfChange >= 1) {
                    annualChangeOfRateOfChange = (((fifthChangeOfRateOfChange - Math.floor(fifthChangeOfRateOfChange)) / 50.0) + 1);
                } else if (fifthChangeOfRateOfChange < 1) {
                    annualChangeOfRateOfChange = (1 - ((1 - fifthChangeOfRateOfChange) / 50.0));
                }
                rateOfChange = ((TemperatureData[latestDataYear] - TemperatureData[latestDataYear - 49]) / 50.0);  

            }
        } else {
            
        if (!(yearRangeRateOfChange.length > 0)) {
            yearRangeRateOfChange = 10;
        }

        if (!(annualChangeOfRateOfChange.length > 0)) {
            annualChangeOfRateOfChange = 0;
        }
        
        yearRangeRateOfChange = parseInt(yearRangeRateOfChange);
        if (signSelector == "positive") {
            annualChangeOfRateOfChange = parseFloat(annualChangeOfRateOfChange) * 0.01;
        } else if (signSelector == "negative") {
            annualChangeOfRateOfChange = -(parseFloat(annualChangeOfRateOfChange) * 0.01);
        }

        // Find rateofchange Temperature / year over year range input
        rateOfChange = (TemperatureData[latestDataYear] - TemperatureData[latestDataYear - yearRangeRateOfChange])/yearRangeRateOfChange;
        }


        value = TemperatureData[latestDataYear]
        for (i = latestDataYear + 1; i < latestDataYear + 50; i = i + 1) {
            stringI = i.toString();
            rateOfChange = rateOfChange * (1 + annualChangeOfRateOfChange);
            value = value + rateOfChange;
            data.addRow([stringI, null, value ]);
        }

        options = {
            title: 'Global Average Temperature (Celsius) vs Time (Years)',
            curveType: 'function',
            legend: {position: 'bottom'},
            width: 900,
            height: 500,
            series :
                {
                    1: { lineDashStyle: [10, 2] }
                }
        };

    }





