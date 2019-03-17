// from data.js
var tableData = data;

// Select Table Body Location
var tbody = d3.select("tbody");

//Load All Data
tableData.forEach((sighting) => {
    var row = tbody.append("tr");
    Object.entries(sighting).forEach(([key,value]) => {
      var cell = tbody.append("td");
      cell.text(value);
    });
  });

    //select the filter button
var filter_data = d3.select("#filter-btn")
filter_data.on("click", function() {
    d3.event.preventDefault();
    
    //clear previous contents
    document.getElementById("yourID").innerHTML="";

    //Store Inputs
    var inputElement = d3.select("#userInput");
    var inputValue = inputElement.property("value");
    

    //Filter Results
    //var filteredData = tableData.filter(sighting => sighting.datetime === inputValue);
    var filteredData = tableData.filter(sightings => Object.values(sightings).includes(inputValue))
    
    //Build New Table
    filteredData.forEach((sighting) => {
        var row = tbody.append("tr");
        Object.entries(sighting).forEach(([key,value]) => {
          var cell = tbody.append("td");
          cell.text(value);
        });
      });

})


