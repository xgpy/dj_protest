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












