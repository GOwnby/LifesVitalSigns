var dataCO2Past;
var dataOne = $.getJSON("json/pastCO2Data.json", function (data){
    dataCO2Past = dataOne.responseJSON;
});

var dataCO2Current;
var dataTwo = $.getJSON("json/currentCO2Data.json", function (data){
    dataCO2Current = dataTwo.responseJSON;
});

var dataCO2Future;
var dataThree = $.getJSON("json/futureCO2Data.json", function (data){
    dataCO2Future = dataThree.responseJSON;
});

var dataGlobalTempPast;
var dataFour = $.getJSON("json/pastGlobalTempData.json", function (data){
    dataGlobalTempPast = dataFour.responseJSON;
});

var dataGlobalTempCurrent;
var dataFive = $.getJSON("json/currentGlobalTempData.json", function (data) {
    dataGlobalTempCurrent = dataFive.responseJSON;
});

var dataGlobalTempFuture;
var dataSix = $.getJSON("json/futureGlobalTempData.json", function (data) {
    dataGlobalTempFuture = dataSix.responseJSON;
});

var dataArcticIceExtentPast;
var dataSeven = $.getJSON("json/pastArcticIceExtentData.json", function (data) {
    dataArcticIceExtentPast = dataSeven.responseJSON;
});

var dataArcticIceExtentCurrent;
var dataEight = $.getJSON("json/currentArcticIceExtentData.json", function (data) {
    dataArcticIceExtentCurrent = dataEight.responseJSON;
});

var dataArcticIceExtentFuture;
var dataNine = $.getJSON("json/futureArcticIceExtentData.json", function (data) {
    dataArcticIceExtentFuture = dataNine.responseJSON;
});

var dataArcticIceAreaPast;
var dataTen = $.getJSON("json/pastArcticIceAreaData.json", function (data) {
    dataArcticIceAreaPast = dataTen.responseJSON;
});

var dataArcticIceAreaCurrent;
var dataEleven = $.getJSON("json/currentArcticIceAreaData.json", function (data) {
    dataArcticIceAreaCurrent = dataEleven.responseJSON;
});

var dataArcticIceAreaFuture;
var dataTwelve = $.getJSON("json/futureArcticIceAreaData.json", function (data) {
    dataArcticIceAreaFuture = dataTwelve.responseJSON;
});

var CO2Data;
var getCO2Data = $.getJSON("json/CO2Data.json", function (data){
    CO2Data = getCO2Data.responseJSON;
});