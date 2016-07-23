d3.csv("data.csv", function(error, data){
    var len1 = "";
    len1 += '<table class="table table-striped">';
    len1 += ' <tr><th>Date</th><th>Temperature</th><th>Humidity</th></tr>';
    for(var i=0; i<data.length; i++){
			len1 += '<tr><td>' + data[i].date + '</td><td>' + data[i].tmp + '℃' + '</td><td>'  + data[i].hum + '%' + '</td></tr>';
    }
    len1 += '</table>';
    d3.select("#text").html(len1);
});

