
$(function(){
	$.ajax({
			url:'/curblogs/',
			type:'POST',
			success:function(arg){
				var obj=jQuery.parseJSON(arg);
				var titleid=obj.cur_obj
				$("#"+titleid).attr('class','a_tb a_active');
				$("#"+titleid).siblings().attr('class','a_tb');
			},
			error:function(){
				console.log('failed');
			},
		});
});


function change_cla(arg){
	var th_cla=$(arg).attr("class");
	$(arg).attr('class','a_tb a_active');
	$(arg).siblings().attr('class','a_tb');
}


function doajax(){
		var tmp = $('#hostid').val();
		var errinfo = $('#delerrid').text();
		$.ajax({
			url:'/webapp/deldata/',
			type:'POST',
			data:{dat:tmp},
			success:function(arg){
				var obj=jQuery.parseJSON(arg);
				console.log(obj.msg);
				console.log(tmp);
				console.log(obj.data);
				console.log(errinfo);
				console.log('success');
				$('#delerrid').text(obj.msg);
			},
			error:function(){
				console.log('failed');
			},
		});
};
function jlogout(){
		var tmp=0;
		$.ajax({
			url:'/webapp/logout/',
			type:'GET',
			data:{dat:tmp},
			success:function(){
				console.log('success');
			},
			error:function(){
				console.log('failed');
			},
		});
};
function changepageitem(arg){
	var value=$(arg).val();
	$.cookie('pager_num',value,{path:'/'});
};












