
$(function() {

$('#multicheckbox').multiselect({

includeSelectAllOption: true

});

});


$(function() {
  $("#multicheckbox").on("change",function() {
     $('#machineName').val($('#multicheckbox').val().join());
  }); 
});

function visitorData(divNO, titleText, series, xAxisTitle, yAxisTitle) {

    Highcharts.setOptions({
        chart: {
            backgroundColor: {
                linearGradient: [0, 0, 500, 500],
                stops: [
                    [0, 'rgb(255, 255, 255)'],
                    [1, 'rgb(240, 240, 255)']
                    ]
            },
            borderWidth: 0,
            plotBackgroundColor: 'rgba(255, 255, 255, .9)',
            plotShadow: true,
            plotBorderWidth: 1
        },
        global: {
        //useUTC: false
        timezoneOffset: -8 * 60
    }
    });


   $(divNO).highcharts({
            chart: {
                type: 'spline',
            },
            
            title: {
                text: titleText
            },
            subtitle: {
                text: 'Monitor Server System Resource'
            },

            xAxis: {
                type: 'datetime',
                tickPixelInterval: 200,
                //maxZoom: 20 * 1000,
                dateTimeLabelFormats: { // don't display the dummy year
                    second: '%H:%M:%S'
                   // month: '%e. %b'
                  //  year: '%Y'
                },
                title: {
                    text: xAxisTitle
                }
            },
            yAxis: {
                title: {
                    text: yAxisTitle
                },
                min: 0
            },
           
            tooltip: {
                headerFormat: '<b>{series.name}</b><br>',
                pointFormat: '{point.x:%H:%M:%S %B%e}: {point.y:.2f}'
            },

            series: series
   
        });
}
    
jQuery('#StartTime').datetimepicker({
  startDate:'+1971/05/01',//or 1986/12/08,
  format:'Y-m-d H:i'
});
jQuery('#EndTime').datetimepicker({
  startDate:'+1971/05/01',//or 1986/12/08,
  format:'Y-m-d H:i'
});

$("#queryButton").click(function(e){

 $.ajax({
    //url: '/getData/' + machineName +'/' + StartTime +'/' +EndTime,
    url: '/getData',
    data: $('form').serialize(),
    type: 'POST',
    async: true,
    dataType: "json",
    success: function (data) {
        var cpuSeriesData = data['cpuUser'];
        var memorySeriesData = data['memUser'];
        var newworkIOsent = data['newworkIOSent'];
        var newworkIORecv = data['newworkIORecv'];
        //var newworkIOrecv = data['newworkIOsent'];

        visitorData('#cpuChart', 'CPU Usage/Percentage', cpuSeriesData, 'Time', 'Usage (percent)')
        visitorData('#memChart', 'Memory Usage/Percentage', memorySeriesData, 'Time', 'Usage (percent)')

        $('#networkIOChartSent').show();
        $('#networkIOChartRecv').show();
        visitorData('#networkIOChartSent', 'NetworkIO Sent/KB', newworkIOsent, 'Time', 'IO sent (KB)')
        visitorData('#networkIOChartRecv', 'NetworkIO Receive/KB', newworkIORecv, 'Time', 'IO Receive (KB)')
        
    },
    error: function(error) {
                console.log(error);
            }
  });
 });