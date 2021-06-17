var myChart=echarts.init(document.getElementById('right'),'dark');
var option={
        title:{
            text:"过弯时间与过弯编号"
        },
        tooltip:{
            trigger:'axis'
        },
        xAxis:{
            type:'category',
            data:[],
            name:'过弯编号'
        },
        yAxis:{
            type:'value',
            name:'过弯时间'
        },
        series: [{
            data: [],
            type: 'line',
            smooth: true,
            color:'#5470c6'
        }]
};
$.ajax({
    type:"GET",
    url:"/",
    dataType:"json",
    success:function (data){
        option['xAxis']['data']=data['xData'];
        option['series'][0]['data']=data['yData'];
        myChart.setOption(option);
        window.onresize = function () {
	        myChart.resize();
        }
        }
});
