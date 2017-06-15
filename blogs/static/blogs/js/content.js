setInterval('get_chatdata()',5000);
function get_chatdata(){
	$.ajax({
		url:'/webchat_incre/',
		type:'POST',
		data:{dat:'data'},
		success:function(arg_cont){
			var obj=jQuery.parseJSON(arg_cont);
			if(obj.data_st==1){
				$.each(obj.chat_incre,function(k,v){
					var template="<div class='chat_u'>"+v.username+" : "+v.chat_date+"</div><div class='chat_c'>"+v.chat_cont+"</div>"
					$(".chat_part").append(template);
					var height=$(".chat_part")[0].scrollHeight;
					$(".chat_part").scrollTop(height);
				});
			}else{
				var height=$(".chat_part")[0].scrollHeight;
				$(".chat_part").scrollTop(height);				
			};
		},
		error:function(){
			console.log('failed');
		},
	});
};
function stru_click(arg){
		var stru_title_js=$(arg).text();
        $(arg).siblings('.menu_title2').addClass('hide');
        $(arg).next().removeClass('hide');
		$.ajax({
			url:'/visitnum/',
			type:'POST',
			data:{dat:stru_title_js},
			success:function(arg_cont){
				var obj=jQuery.parseJSON(arg_cont);
				if(obj.msg == 1){
					console.log('success');
				}else{
					alert('查询失败！！！');
				}
			},
			error:function(){
				console.log('failed');
			},
		});
		$.ajax({
			url:'/blogs_cont/',
			type:'POST',
			data:{dat:stru_title_js},
			success:function(arg_cont){
				var obj=jQuery.parseJSON(arg_cont);
				$(arg).parent().next().children('#cont_t1').children('#cont_h1').text(obj.cont_title);
				$(arg).parent().next().children('#cont_t1').children('#cont_h2').children().text(obj.cont_visit);
				$(arg).parent().next().children('#cont_t1').children('#cont_h3').text('创建时间：'+obj.cont_date);
				$(arg).parent().next().children('#cont_t2').children().html(obj.cont_content);
				//console.log(obj.commentpy);
				$(arg).parent().next().children().last().html('');
				var comm_h1="<div class='comment_h'><a onclick='commclick_h(this);'>评论：</a>"+
							"<span>"+obj.commnum+"</span></div>"+
							"<div class='hide'></div><div class='commarea_h'><textarea class='comment_area'></textarea>"+
							"<div class='comment_button' onclick='comment_click(this);'>发表评论</div></div>";
				$(arg).parent().next().children().last().append(comm_h1);
				if(obj.commnum > 0){
					$.each(obj.commentpy,function(k1,v1){
					if(v1!=''){
						var comm_1c1="<div id=1><div class='comm_user'><span>"+v1[1].commuser+
									"</span><span>&nbsp;:&nbsp;</span><span>"+v1[1].commdate+
									"</span></div><div><pre class='comm_cont'>"+v1[1].commcont+
									"</pre></div><div class='reply_button' onclick='reply_click(this);'>回复</div>"+
									"</div><div class='hide'><textarea class='reply_area'></textarea>"+
									"<div class='reply_commit' onclick='reply_subcli(this);'>提交回复</div></div>";
						$(arg).parent().next().children().last().children().first().next().append(comm_1c1);
						if(v1.data!=''){
						$.each(v1.data,function(k2,v2){
						if(v2!=''){
							var comm_2c1="<div id=2><div class='comm_user2'><span>"+v2[2].commuser+
										"</span><span>&nbsp;:&nbsp;</span><span>"+v2[2].commdate+
										"</span></div><div><pre class='comm_cont2'>"+v2[2].commcont+
										"</pre></div><div class='reply_button2' onclick='reply_click(this);'>回复</div>"+
										"</div><div class='hide'><textarea class='reply_area2'></textarea>"+
										"<div class='reply_commit2' onclick='reply_subcli(this);'>提交回复</div></div>";
							$(arg).parent().next().children().last().children().first().next().append(comm_2c1);
							if(v2.data!=''){
								$.each(v2.data,function(k3,v3){
								if(v3[3]!=''){
									$.each(v3[3],function(kd3,d3){
										if(d3!=''){
											var comm_3c1="<div id=3><div class='comm_user3'><span>"+d3.commuser+
														"</span><span>&nbsp;:&nbsp;</span><span>"+d3.commdate+
														"</span></div><div><pre class='comm_cont3'>"+d3.commcont+
														"</pre></div><!--<div class='reply_button3' onclick='reply_click(this);'>回复</div>-->"+
														"</div><div class='hide'><textarea class='reply_area3'></textarea>"+
														"<div class='reply_commit3' onclick='reply_subcli(this);'>提交回复</div></div>";
											$(arg).parent().next().children().last().children().first().next().append(comm_3c1);
										};
									});
								};
								});
							};
							};
						});
						};
					};
					});
				};
			},
			error:function(){
				console.log('failed');
			},
		});
};
function cont_click(arg){
		var stru_title_js=$(arg).text();
		$.ajax({
			url:'/visitnum/',
			type:'POST',
			data:{dat:stru_title_js},
			success:function(arg_cont){
				var obj=jQuery.parseJSON(arg_cont);
				if(obj.msg == 1){
					console.log('success');
				}else{
					alert('查询失败！！！');
				}
			},
			error:function(){
				console.log('failed');
			},
		});
		$.ajax({
			url:'/blogs_cont/',
			type:'POST',
			data:{dat:stru_title_js},
			success:function(arg_cont){
				var obj=jQuery.parseJSON(arg_cont);
				$(arg).parent().parent().next().children('#cont_t1').children('#cont_h1').text(obj.cont_title);
				$(arg).parent().parent().next().children('#cont_t1').children('#cont_h2').children().text(obj.cont_visit);
				$(arg).parent().parent().next().children('#cont_t1').children('#cont_h3').text('创建时间：'+obj.cont_date);
				$(arg).parent().parent().next().children('#cont_t2').children().html(obj.cont_content);
				$(arg).parent().parent().next().children().last().html('');
				var comm_h1="<div class='comment_h'><a onclick='commclick_h(this);'>评论：</a>"+
							"<span>"+obj.commnum+"</span></div>"+
							"<div class='hide'></div><div class='commarea_h'><textarea class='comment_area'></textarea>"+
							"<div class='comment_button' onclick='comment_click(this);'>发表评论</div></div>";
				$(arg).parent().parent().next().children().last().append(comm_h1);
				if(obj.commnum > 0){
					$.each(obj.commentpy,function(k1,v1){
					if(v1!=''){
						var comm_1c1="<div id=1><div class='comm_user'><span>"+v1[1].commuser+
									"</span><span>&nbsp;:&nbsp;</span><span>"+v1[1].commdate+
									"</span></div><div><pre class='comm_cont'>"+v1[1].commcont+
									"</pre></div><div class='reply_button' onclick='reply_click(this);'>回复</div>"+
									"</div><div class='hide'><textarea class='reply_area'></textarea>"+
									"<div class='reply_commit' onclick='reply_subcli(this);'>提交回复</div></div>";
						$(arg).parent().parent().next().children().last().children().first().next().append(comm_1c1);
						if(v1.data!=''){
						$.each(v1.data,function(k2,v2){
						if(v2!=''){
							var comm_2c1="<div id=2><div class='comm_user2'><span>"+v2[2].commuser+
										"</span><span>&nbsp;:&nbsp;</span><span>"+v2[2].commdate+
										"</span></div><div><pre class='comm_cont2'>"+v2[2].commcont+
										"</pre></div><div class='reply_button2' onclick='reply_click(this);'>回复</div>"+
										"</div><div class='hide'><textarea class='reply_area2'></textarea>"+
										"<div class='reply_commit2' onclick='reply_subcli(this);'>提交回复</div></div>";
							$(arg).parent().parent().next().children().last().children().first().next().append(comm_2c1);
							if(v2.data!=''){
								$.each(v2.data,function(k3,v3){
								if(v3[3]!=''){
									$.each(v3[3],function(kd3,d3){
										if(d3!=''){
											var comm_3c1="<div id=3><div class='comm_user3'><span>"+d3.commuser+
														"</span><span>&nbsp;:&nbsp;</span><span>"+d3.commdate+
														"</span></div><div><pre class='comm_cont3'>"+d3.commcont+
														"</pre></div><!--<div class='reply_button3' onclick='reply_click(this);'>回复</div>-->"+
														"</div><div class='hide'><textarea class='reply_area3'></textarea>"+
														"<div class='reply_commit3' onclick='reply_subcli(this);'>提交回复</div></div>";
											$(arg).parent().parent().next().children().last().children().first().next().append(comm_3c1);
										};
									});
								};
								});
							};
							};
						});
						};
					};
					});
				};
			},
			error:function(){
				console.log('failed');
			},
		});
};
function chat_sendjs(arg){
		var chat_cont=$(arg).prev().val();
		$.ajax({
			url:'/web_addchat/',
			type:'POST',
			data:{dat:chat_cont},
			success:function(arg_cont){
				var obj=jQuery.parseJSON(arg_cont);
				if(obj.msg == 1){
					var template="<div class='chat_u'>"+obj.curuser+" : "+obj.time_now+"</div><div class='chat_c'>"+obj.chatcont+"</div>"
					$(arg).parent().prev().append(template);
					$(arg).prev().val('');
					var height=$(".chat_part")[0].scrollHeight;
					$(".chat_part").scrollTop(height);
				}else{
					alert('发送失败！！！');
				}
			},
			error:function(){
				console.log('failed');
			},
		});
};
function comment_click(arg){
		var comment_cont=$(arg).prev().val();
		console.log(comment_cont);
		$.ajax({
			url:'/commentpy/',
			type:'POST',
			data:{dat:comment_cont},
			success:function(arg_cont){
				var obj=jQuery.parseJSON(arg_cont);
				if(obj.msg == 1){
					var commnum=parseInt($(arg).parent().prev().prev().children().last().text());
					var template="<div id=1><div class='comm_user'><span>"+obj.commuser+
						"</span><span> &nbsp;: &nbsp;</span><span>"+obj.commdate+
						"</span></div><div><pre class='comm_cont'>"+obj.commcont+
						"</pre></div><div class='reply_button' onclick='reply_click(this);'>回复</div>"+
						"</div><div class='hide'><textarea class='reply_area'></textarea>"+
						"<div class='reply_commit' onclick='reply_subcli(this);'>提交回复</div></div>";
					$(arg).parent().prev().append(template);
					$(arg).parent().prev().prev().children().last().text(commnum+1);
					console.log(commnum);
					$(arg).prev().val('');
				}else{
					alert('评论失败！！！');
				}
			},
			error:function(){
				console.log('failed');
			},
		});
};
function reply_click(arg){
		$(arg).parent().next().toggleClass('hide');
		console.log($(arg).prev().text());
};
function code_click(arg){
		$(arg).next().toggleClass('hide');
};
function reply_subcli(arg){
		var reply_userobj=$(arg).parent().prev().children().first().children().first().text();
		var reply_timeobj=$(arg).parent().prev().children().first().children().last().text();
		var reply_cont=$(arg).prev().val();
		console.log(reply_userobj);
		console.log(reply_timeobj);
		console.log(reply_cont);
		$.ajax({
			url:'/replysubmit/',
			type:'POST',
			data:{userobj:reply_userobj,timeobj:reply_timeobj,cont:reply_cont},
			success:function(arg_cont){
				var obj=jQuery.parseJSON(arg_cont);
				if(obj.msg == 1){
					var level=parseInt($(arg).parent().prev().attr("id"));
					var commnum=parseInt($(arg).parent().parent().prev().children().last().text());
					if(level < 3){
						var level=level+1;
					}else{
						var level=3;
					};
					var temp1="<div class='comm_user"+level+"'><span>"+obj.curuser+
						"</span><span> &nbsp;: &nbsp;</span><span>"+obj.replydate+
						"</span></div><div><pre class='comm_cont"+level+"'>"+obj.replycont+"</pre></div>";
					var temp2="<div class='reply_button"+level+"' onclick='reply_click(this);'>回复</div>";
					if(level < 3){
						$(arg).parent().prev().append(temp1);
						$(arg).parent().prev().append(temp2);
					}else{
						$(arg).parent().prev().append(temp1);
					};
					$(arg).parent().parent().prev().children().last().text(commnum+1);
					console.log(obj);
					$(arg).prev().val('');
				}else{
					alert('回复失败！！！');
				}
			},
			error:function(){
				console.log('failed');
			},
		});
};
function commclick_h(arg){
	$(arg).parent().next().toggleClass('hide');
};
//$(function(){
//    $('.menu_title1').click(function(){
//    	var stru_title_js=$(this).text()
//    	$.cookie('cur_stru_title',stru_title_js,{path:'/'});
//    	console.log($.cookie('cur_stru_title'));
//        $(this).siblings('.menu_title2').addClass('hide');
//        $(this).next().removeClass('hide');
//        
//    });
//});

//$(function(){
//		var per_item=$.cookie('pager_num');
//		console.log(per_item);
//		if(per_item){
//			$('#per_pgid').val(per_item)
//		}else{
//			$.cookie('pager_num',3,{path:'/'});
//		};
//	});
//$(function(){
//    $('.menu_title1').click(function(){
//    	var stru_title_js=$(this).text()
//    	$.cookie('cur_stru_title',stru_title_js,{path:'/'});
//        $(this).siblings('.menu_title2').addClass('hide');
//        $(this).next().removeClass('hide');
//		$.ajax({
//			url:'/blogs/',
//			type:'POST',
//			data:{dat:stru_title_js},
//			success:function(){
//				console.log(stru_title_js);
//			},
//			error:function(){
//				console.log('failed');
//			},
//		});
//        
//    });
//});