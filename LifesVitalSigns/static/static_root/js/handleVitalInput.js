window.onload = function() {
    this.handleCO2Panel();
    this.animateDrawButton();
}

function setSelectorColorScheme(panelSelected) {
    if (panelSelected == "CO2Panel") {
        (document.getElementById("triggerCO2")).style.backgroundColor = "#153183";
        (document.getElementById("CO2")).style.color = "#cdedf7";
        (document.getElementById("triggerTemperature")).style.backgroundColor = "#cdedf7";
        (document.getElementById("Temperature")).style.color = "#153183";
    }

    if (panelSelected == "temperaturePanel") {
        (document.getElementById("triggerTemperature")).style.backgroundColor = "#153183";
        (document.getElementById("Temperature")).style.color = "#cdedf7";
        (document.getElementById("triggerCO2")).style.backgroundColor = "#cdedf7";
        (document.getElementById("CO2")).style.color = "#153183";
    }
}

/*
function animateChart() {
    var panelChart = document.getElementById("lineChart");
    panelChart.className = panelChart.className !== 'hide' ? 'hide' : 'hide';

    if (panelChart.className === 'hide') {
        setTimeout(function(){
            panelChart.style.display = 'none';
        },700); 
    }

        drawSelectedPanel();

        panelChart.className = panelChart.className !== 'show' ? 'show' : 'show';

    if (panelChart.className === 'show') {
        setTimeout(function(){
            panelChart.style.display = 'show';
        },700); 
    }

}
*/

function animateDrawButton() {
    var panelDraw = document.getElementById("drawChart")
    panelDraw.className = panelDraw.className !== 'show' ? 'show' : 'show';

    if (panelDraw.className === 'show') {
        setTimeout(function(){
            panelDraw.style.display = 'block';
        },700); 
    }
}

function drawSelectedPanel() {
    if ((document.getElementById("CO2Panel")).style.display == "block"){
        loadCO2();
    }

    if ((document.getElementById("advancedCO2Panel")).style.display == "block"){
        loadCO2();
    }

    if ((document.getElementById("temperaturePanel")).style.display == "block") {
        loadTemperature();
    }

    if ((document.getElementById("advancedTemperaturePanel")).style.display == "block") {
        loadTemperature();
    }

    draw();
}

function closeSelectedPanel() {
    var panelCO2 = document.getElementById("CO2Panel");
    var panelAdvancedCO2 = document.getElementById("advancedCO2Panel");
    var panelTemperature = document.getElementById("temperaturePanel");
    var panelAdvancedTemperature = document.getElementById("advancedTemperaturePanel");
    if (panelCO2.style.display == "block") {
        panelCO2.className = panelCO2.className !== 'hide' ? 'hide' : 'hide';
    
        if (panelCO2.className === 'hide') {
            setTimeout(function(){
              panelCO2.style.display = 'none';
            },700); 
          }
    }
    if (panelAdvancedCO2.style.display == "block") {
        panelAdvancedCO2.className = panelAdvancedCO2.className !== 'hide' ? 'hide' : 'hide';
    
        if (panelAdvancedCO2.className === 'hide') {
            setTimeout(function(){
              panelAdvancedCO2.style.display = 'none';
            },700); 
          }
    }
    if (panelTemperature.style.display == "block") {
        panelTemperature.className = panelTemperature.className !== 'hide' ? 'hide' : 'hide';
    
        if (panelTemperature.className === 'hide') {
            setTimeout(function(){
              panelTemperature.style.display = 'none';
            },700); 
          }
    }
    if (panelAdvancedTemperature.style.display == "block") {
        panelAdvancedTemperature.className = panelAdvancedTemperature.className !== 'hide' ? 'hide' : 'hide';
    
        if (panelAdvancedTemperature.className === 'hide') {
            setTimeout(function(){
              panelAdvancedTemperature.style.display = 'none';
            },700); 
          }
    } 
}

function handleCO2Panel() {
    closeSelectedPanel();
    setSelectorColorScheme("CO2Panel");
    var panelCO2 = document.getElementById("CO2Panel")
    panelCO2.className = panelCO2.className !== 'show' ? 'show' : 'show';

    if (panelCO2.className === 'show') {
        setTimeout(function(){
          panelCO2.style.display = 'block';
        },700); 
      }

}

function handleCO2AdvancedPanel() {
    var panelCO2 = document.getElementById("CO2Panel")
    panelCO2.className = panelCO2.className !== 'hide' ? 'hide' : 'show';

    if (panelCO2.className === 'show') {
        setTimeout(function(){
          panelCO2.style.display = 'block';
        },700); 
      }
  
      if (panelCO2.className === 'hide') {
        setTimeout(function(){
          panelCO2.style.display = 'none';
        },700);
      }

    var panelAdvancedCO2 = document.getElementById("advancedCO2Panel");
    panelAdvancedCO2.className = panelAdvancedCO2.className !== 'show' ? 'show' : 'hide';

    if (panelAdvancedCO2.className === 'show') {
      setTimeout(function(){
        panelAdvancedCO2.style.display = 'block';
      },700); 
    }

    if (panelAdvancedCO2.className === 'hide') {
      setTimeout(function(){
        panelAdvancedCO2.style.display = 'none';
      },700);
    }
}

function listenToCO2Advanced() {
    var panelAdvancedCO2 = (document.getElementById("advancedCO2Panel"));
    if (panelAdvancedCO2.style.display == "none") {
        return true;
    } else if (panelAdvancedCO2.style.display == "block") {
        return false;
    }
}

function handleTemperaturePanel() {
    closeSelectedPanel();
    setSelectorColorScheme("temperaturePanel");
    var panelTemperature = document.getElementById("temperaturePanel");
    panelTemperature.className = panelTemperature.className !== 'show' ? 'show' : 'show';

    if (panelTemperature.className === 'show') {
        setTimeout(function(){
          panelTemperature.style.display = 'block';
        },700); 
      }
}

function handleTemperatureAdvancedPanel() {
    var panelTemperature = document.getElementById("temperaturePanel")
    panelTemperature.className = panelTemperature.className !== 'hide' ? 'hide' : 'show';

    if (panelTemperature.className === 'show') {
        setTimeout(function(){
            panelTemperature.style.display = 'block';
        },700); 
      }
  
      if (panelTemperature.className === 'hide') {
        setTimeout(function(){
          panelTemperature.style.display = 'none';
        },700);
      }

    var panelAdvancedTemperature = document.getElementById("advancedTemperaturePanel");
    panelAdvancedTemperature.className = panelAdvancedTemperature.className !== 'show' ? 'show' : 'hide';

    if (panelAdvancedTemperature.className === 'show') {
      setTimeout(function(){
        panelAdvancedTemperature.style.display = 'block';
      },700); 
    }

    if (panelAdvancedTemperature.className === 'hide') {
      setTimeout(function(){
        panelAdvancedTemperature.style.display = 'none';
      },700);
    }
}

function listenToTemperatureAdvanced() {
    var panelAdvancedTemperature = (document.getElementById("advancedTemperaturePanel"));
    if (panelAdvancedTemperature.style.display == "none") {
        return true;
    } else if (panelAdvancedTemperature.style.display == "block") {
        return false;
    }
}