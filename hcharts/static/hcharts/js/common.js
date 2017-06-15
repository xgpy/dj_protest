$(function(){
	$.getJSON('/hchartsdata/',function(data){
		Highcharts.setOptions({
			lang:{
				resetZoom:'重置缩放比例',
			}
		});
		$('#container').highcharts({
            chart: {
                zoomType: 'x'
            },
            title: {
                text: '图表练习'
            },
            subtitle: {
                text: document.ontouchstart === undefined ?
                '鼠标拖动可以进行缩放' : '手势操作进行缩放'
            },
            xAxis: {
                labels:{
                	formatter:function(){
                		var x=this.value*1000;
                		var newx=new Date();
                		newx.setTime(x);
                		//return x
                		Date.prototype.format = function(format) {
				        var date = {
				              "M+": this.getMonth() + 1,
				              "d+": this.getDate(),
				              "h+": this.getHours(),
				              "m+": this.getMinutes(),
				              "s+": this.getSeconds(),
				              "q+": Math.floor((this.getMonth() + 3) / 3),
				              "S+": this.getMilliseconds()
				        };
				        if (/(y+)/i.test(format)) {
				              format = format.replace(RegExp.$1, (this.getFullYear() + '').substr(4 - RegExp.$1.length));
				        }
				        for (var k in date) {
				              if (new RegExp("(" + k + ")").test(format)) {
				                     format = format.replace(RegExp.$1, RegExp.$1.length == 1
				                            ? date[k] : ("00" + date[k]).substr(("" + date[k]).length));
				              }
				        }
				        return format;
						}
						return newx.format('yyyy-MM-dd h:m:s');
                	}
                }
            },
            tooltip: {
            	crosshairs:[true,true],
            	formatter:function(){
            		var x2=this.x*1000;
            		var newx2=new Date();
            		newx2.setTime(x2);
            		return newx2.toLocaleString()+'<br/>'+this.series.name+':'+this.y;
            	}
            },
            yAxis: {
                title: {
                    text: 'Y轴'
                }
            },
            legend: {
                enabled: false
            },
            plotOptions: {
                area: {
                    fillColor: {
                        linearGradient: {
                            x1: 0,
                            y1: 0,
                            x2: 0,
                            y2: 1
                        },
                        stops: [
                            [0, Highcharts.getOptions().colors[0]],
                            [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                        ]
                    },
                    marker: {
                        radius: 2
                    },
                    lineWidth: 1,
                    states: {
                        hover: {
                            lineWidth: 1
                        }
                    },
                    threshold: null
                }
            },
            credits:{
            	// enabled:true,    // 默认值，如果想去掉版权信息，设置为false即可 
            	text: 'www.hcharts.cn', // 显示的文字 
            	href: 'http://www.hcharts.cn', // 链接地址 
            	position: { // 位置设置 
            		align: 'right', 
            		x: -100, 
            		verticalAlign: 'top', 
            		y: 30 
            		}, 
            	style: { // 样式设置 
            		cursor: 'pointer', 
            		color: 'red', 
            		fontSize: '25px' 
            	}
            },
            series: [{
                type: 'area',
                name: '图表测试',
                data: data
            }]
        });
	});
});








