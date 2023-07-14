$(document).ready(function() {

  console.log("hi1");

  $.get("http://172.29.1.198:9007/current_tmp", function(data) {
    //let curr_temp = document.getElementById("#curr_temp");
    //console.log(data);
    //curr_temp.innerHTML() = `
    //${data["current temp"]}°C
    //`
    console.log(data);
    $("#curr_temp").text(data["current temp"] + "°C");
  });

  $.get("http://172.29.1.198:9007/average_tmp", function(data) {
    $("#avg_temp").text(data["average"]+ "°C");
  });


  $.get("http://172.29.1.198:9007/current_hmd", function(data) {
    $("#current_hmd").text(data["current hmd"]);
  });

  $.get("http://172.29.1.198:9007/average_hmd", function(data) {
    $("#avg_hmd").text(data["average"]);
  });

  var tableShown = false;

  $("#show-data-btn").on("click", function() {
    if (!tableShown) {
      $.getJSON("http://172.29.1.198:9007/show_data", function(data) {
        var table = $("<table/>");
        table.append("<thead><tr><th>ID</th><th>Node ID</th><th>Device Type</th><th>Temperature</th><th>Humidity</th><th>Date</th><th>Time</th></tr></thead>");
        var tbody = $("<tbody/>");
        $.each(data, function(index, element) {
          var row = $("<tr/>");
          row.append($("<td/>").text(element.ID));
          row.append($("<td/>").text(element['Node ID']));
          row.append($("<td/>").text(element['Device Type']));
          row.append($("<td/>").text(element.Temperature));
          row.append($("<td/>").text(element.Humidity));
          var date = new Date(element.Date);
          row.append($("<td/>").text(date.toLocaleDateString("en-US")));
          row.append($("<td/>").text(element.Time));
          tbody.append(row);
        });
        table.append(tbody);
        $("#data-table").html(table);
        $("#data-table-container").fadeIn();
        $("#show-data-btn").text("Hide All Data");
        tableShown = true;
      });
    } else {
      $("#data-table-container").fadeOut();
      $("#show-data-btn").text("Show All Data");
      tableShown = false;
    }
  });

  // clock functionality
  function updateTime() {
    const now = new Date();
    const time = now.toLocaleTimeString();
    const date = now.toLocaleDateString("en-US");
    document.querySelector('.time').textContent = time;
    document.querySelector('.date').textContent = date;
  }

  setInterval(updateTime, 1000);

  var tableShown = false;

  $("#temperature-btn").on("click", function() {
    if (!tableShown) {
      $.getJSON("http://172.29.1.198:9007/show_data", function(data) {
        var table = $("<table/>");
        table.append("<thead><tr><th>ID</th><th>Temperature</th><th>Humidity</th><th>Date</th><th>Time</th></tr></thead>");
        var tbody = $("<tbody/>");
        $.each(data, function(index, element) {
          var row = $("<tr/>");
          row.append($("<td/>").text(element.ID));
          row.append($("<td/>").text(element.Temperature));
          row.append($("<td/>").text(element.Humidity));
          var date = new Date(element.Date);
          row.append($("<td/>").text(date.toLocaleDateString("en-US")));
          row.append($("<td/>").text(element.Time));
          tbody.append(row);
        });
        table.append(tbody);
        $("#temp-table").html(table);
        $("#temp-table-container").fadeIn();
        tableShown = true;
      });
    } else {
      $("#temp-table-container").fadeOut();
      tableShown = false;
    }
  });
  
});
