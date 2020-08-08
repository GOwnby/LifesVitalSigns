google.charts.load('45', {
   // callback: drawCO2Charts,
    packages:['corechart']
});




    function drawChart1() {

        var data = new google.visualization.DataTable();

        data.addColumn('string', 'Year');
        data.addColumn('number', 'CO2 Actual');
        data.addColumn('number', 'CO2 Projected');


        var year = 2018;
        var stringI;
        for (var i = 1959; i < year ; i = i + 4)
        {
           stringI = i.toString();
           data.addRow([stringI, dataCO2Past[stringI], null ]);
        }

        data.addRow([year.toString(), dataCO2Current[year.toString()], dataCO2Current[year.toString()] ]);

        for (var i = year + 4; i < year + 50; i = i + 4) {
            stringI = i.toString();
            data.addRow([stringI, null, dataCO2Future[stringI] ]);
        }

        var options = {
            title: 'Carbon Dioxide (ppm) vs Time (Years) at Current Rate Of Change',
            curveType: 'function',
            legend: {position: 'bottom'},
            width: 900,
            height: 500,
            series :
                {
                    1: { lineDashStyle: [10, 2] }
                }
        };

        var chart = new google.visualization.LineChart(document.getElementById('linechart_'));

        chart.draw(data, options);

    }

    function drawChart2() {

        var data = new google.visualization.DataTable();

        data.addColumn('string', 'Year');
        data.addColumn('number', 'Global Temperature Actual');
        data.addColumn('number', 'Global Temperature Projected');


        var year = 2018;
        var stringI;
        for (var i = 1880; i < year ; i = i + 4)
        {
            stringI = i.toString();
            data.addRow([stringI, dataGlobalTempPast[stringI], null ]);
        }

        data.addRow([year.toString(), dataGlobalTempCurrent[year.toString()], dataGlobalTempCurrent[year.toString()] ]);

        for (var i = year + 4; i < 2070; i = i + 4) {
            stringI = i.toString();
            data.addRow([stringI, null, dataGlobalTempFuture[stringI]]);
        }

        var options = {
            title: 'Global Temperature Change (Celsius) vs Time (Years)',
            curveType: 'function',
            legend: {position: 'bottom'},
            width: 900,
            height: 500,
            series :
                {
                    1: { lineDashStyle: [10, 2] }
                }
        };

        var chart = new google.visualization.LineChart(document.getElementById('linechart_'));

        chart.draw(data, options);

    }

    function drawChart3() {

        var data = new google.visualization.DataTable();

        data.addColumn('string', 'Year');
        data.addColumn('number', 'Arctic Ice Extent Actual');
        data.addColumn('number', 'Arctic Ice Extent Projected');


        var year = 2017;
        var stringI;
        for (var i = 1979; i < year ; i = i + 4)
        {
            stringI = i.toString();
            data.addRow([stringI, dataArcticIceExtentPast[stringI], null ]);
        }

        data.addRow([year.toString(), dataArcticIceExtentCurrent[year.toString()], dataArcticIceExtentCurrent[year.toString()] ]);

        for (var i = year + 4; i < 2070; i = i + 4) {
            stringI = i.toString();
            data.addRow([stringI, null, dataArcticIceExtentFuture[stringI] ]);
        }

        var options = {
            title: 'Arctic Ice Minimum Extent (Sq KM) vs Time (Years)',
            curveType: 'function',
            legend: {position: 'bottom'},
            width: 900,
            height: 500,
            series :
                {
                    1: { lineDashStyle: [10, 2] }
                }
        };

        var chart = new google.visualization.LineChart(document.getElementById('linechart_'));

        chart.draw(data, options);
    }

function drawChart4() {

    var data = new google.visualization.DataTable();

    data.addColumn('string', 'Year');
    data.addColumn('number', 'Arctic Ice Area Actual');
    data.addColumn('number', 'Arctic Ice Area Projected');


    var year = 2017;
    var stringI;
    for (var i = 1979; i < year; i = i + 4) {
        stringI = i.toString();
        data.addRow([stringI, dataArcticIceAreaPast[stringI], null]);
    }

    data.addRow([year.toString(), dataArcticIceAreaCurrent[year.toString()], dataArcticIceAreaCurrent[year.toString()]]);

    for (var i = year + 4; i < 2070; i = i + 4) {
        stringI = i.toString();
        data.addRow([stringI, null, dataArcticIceAreaFuture[stringI]]);
    }

    var options = {
        title: 'Arctic Ice Minimum Area (Sq KM) vs Time (Years)',
        curveType: 'function',
        legend: {position: 'bottom'},
        width: 900,
        height: 500,
        series:
            {
                1: {lineDashStyle: [10, 2]}
            }
    };

    var chart = new google.visualization.LineChart(document.getElementById('linechart_'));

    chart.draw(data, options);
    }

    function drawCO2() {

        var data = new google.visualization.DataTable();

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
        var checkedValue = 0;
        for(var i=0,l=checkboxes.length;i<l;i++)
        {
            if(checkboxes[i].checked)
            {
                preset = true;
                if (i == 0) {checkedValue = 1;}
                if (i == 1) {checkedValue = 2;}
                break;
            }
        }


        if (preset) {

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
                yearRangeRateOfChange = 1;
            }
            yearRangeRateOfChange = parseInt(yearRangeRateOfChange);

            if (!(annualChangeOfRateOfChange.length > 0)) {
                annualChangeOfRateOfChange = 0;
                rateOfChange = (CO2Data[latestDataYear] - CO2Data[latestDataYear - yearRangeRateOfChange])/yearRangeRateOfChange;
            } else {
                rateOfChange = (CO2Data[latestDataYear] - CO2Data[latestDataYear - yearRangeRateOfChange])/yearRangeRateOfChange;
            }
        

            if (signSelector == "positive") {
                annualChangeOfRateOfChange = (1 + ((parseFloat(annualChangeOfRateOfChange)) * 0.01));
            } else if (signSelector == "negative") {
                annualChangeOfRateOfChange = (1 - ((parseFloat(annualChangeOfRateOfChange)) * 0.01));
            }

        }



        value = CO2Data[latestDataYear]
        for (i = latestDataYear + 1; i < latestDataYear + 50; i = i + 1) {
            stringI = i.toString();
            rateOfChange = rateOfChange * (annualChangeOfRateOfChange);
            value = value + rateOfChange;
            data.addRow([stringI, null, value ]);
        }

        var options = {
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

        var chart = new google.visualization.LineChart(document.getElementById('linechart_'));

        chart.draw(data, options);

    }

    function drawTemperature() {

        var data = new google.visualization.DataTable();

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

        if (!(yearRangeRateOfChange.length > 0)) {
            yearRangeRateOfChange = 10;
        }

        if (!(annualChangeOfRateOfChange.length > 0)) {
            annualChangeOfRateOfChange = -0.025;
        }
        
        yearRangeRateOfChange = parseInt(yearRangeRateOfChange);
        if (signSelector == "positive") {
            annualChangeOfRateOfChange = parseFloat(annualChangeOfRateOfChange) * 0.01;
        } else if (signSelector == "negative") {
            annualChangeOfRateOfChange = -(parseFloat(annualChangeOfRateOfChange) * 0.01);
        }

        // Find rateofchange Temperature / year over year range input
        rateOfChange = (TemperatureData[latestDataYear] - TemperatureData[latestDataYear - yearRangeRateOfChange])/yearRangeRateOfChange;

        value = TemperatureData[latestDataYear]
        for (i = latestDataYear + 1; i < latestDataYear + 50; i = i + 1) {
            stringI = i.toString();
            rateOfChange = rateOfChange * (1 + annualChangeOfRateOfChange);
            value = value + rateOfChange;
            data.addRow([stringI, null, value ]);
        }

        var options = {
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

        var chart = new google.visualization.LineChart(document.getElementById('linechart_'));

        chart.draw(data, options);

    }





