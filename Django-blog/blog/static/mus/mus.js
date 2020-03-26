	//底部显示区域总宽度
    var footerW = $('.myaudio').width();
	//中央显示区域的宽度
    var audioW = $('.myaudio-center').width();
	//alert(footerW);
	//alert(audioW);
	$('.myaudio-center').css({'left':(footerW-audioW)/2})
	$('.aud-show').css({'width':audioW-70})
	$('#Progress').css({'width':audioW-170})

	var i=0;
	$('#play').click(function () {
		i++;
		if (i % 2 !=0) {
			$(this).attr('src', '/media/img/pause.png');
			aud_play();
		} else {
			$(this).attr('src', '/media/img/play.png');
			aud_pause()
		}
	})
	var music;
	var audio = document.getElementById("aud");

	function aud_play(q=0) {
		audio.currentTime = q;
		audio.play();
		music = setInterval(function () {
			var curtime = audio.currentTime.toFixed(2);//播放进度
			var durtime = audio.duration.toFixed(2);//播放时间
			var str = "00:00";

			var time = formatSeconds(curtime);

			var time1 = str.substring(0, str.length - formatSeconds(durtime).length) + formatSeconds(durtime);

			$('#Progress-time').html(time);
			$('#Progress-end').html(time1);
			$width = curtime / durtime * (audioW - 181);
			$('#jin').css({width: $width})
			$('#yuan').css({left: $width})
		}, 100);
	}
	function aud_pause() {
		document.getElementById("aud").pause();
		clearInterval(music);
	}

	function formatSeconds(value) {
		var theTime = parseInt(value);// 秒
		var theTime1 = 0;// 分
		var theTime2 = 0;// 小时
		if (theTime > 60) {
			theTime1 = parseInt(theTime / 60);
			theTime = parseInt(theTime % 60);
			if (theTime1 > 60) {
				theTime2 = parseInt(theTime1 / 60);
				theTime1 = parseInt(theTime1 % 60);
			}
		}
		var result = "" + theTime;
		result  =   (result.length==1)?'0'+result:result;
		if (theTime1 > 0) {
			theTime1  =   (theTime1.length==1)?'0'+theTime1:theTime1;

			result = "" + theTime1 + ":" + result;
		}
		if (theTime2 > 0) {
			theTime2  =   (theTime2.length==1)?'0'+theTime2:theTime2;
			result = "" + theTime2 + ":" + result;
		}
		result =   (result.length==2)?'00:'+result:result;
		return result;
	}

	var cont = $("#yuan");
	var contW = $("#yuan").width();
	var startX, sX, moveX, disX;
	var winW = $('#Progress').width();
	$("#yuan").on({//绑定事件
		touchstart: function (e) {

			startX = e.originalEvent.targetTouches[0].pageX;    //获取点击点的X坐标
			sX = $(this).offset().left-110;//相对于当前窗口X轴的偏移量
			leftX = startX - sX;//鼠标所能移动的最左端是当前鼠标距div左边距的位置
			rightX = winW - contW + leftX;//鼠标所能移动的最右端是当前窗口距离减去鼠标距div最右端位置
		},
		touchmove: function (e) {
			//aud_pause();
			e.preventDefault();
			moveX = e.originalEvent.targetTouches[0].pageX;//移动过程中X轴的坐标

			if(moveX<leftX){moveX=leftX;}
			if(moveX>rightX){moveX=rightX;}
			$(this).css({
				"left":moveX+sX-startX,
			});
			$('#jin').width($(this).width()+moveX+sX-startX);
		   var w = audio.duration.toFixed(2)*($('#jin').width()/winW)
			$('#play').attr('src', '/media/img/pause.png');
			aud_play(w)
		},
		mousedown: function (ev) {
			aud_pause()
			var patch = parseInt($(this).css("height")) / 2;
			var left1 = parseInt($(this).parents('.myaudio-center').css("left"));


			$(this).mousemove(function (ev) {
				var oEvent = ev || event;
			   // console.log(oEvent);
				var oX = oEvent.clientX;
				console.log(oX);
				var l = oX - patch-left1-115;//115为$("#yuan")的起始位置到$('.myaudio-center')左边的距离
				console.log(l);
				var w = $(window).width() - $(this).width();
				console.log(w);
				if (l < 0) {
					l = 0
				}
				if (l > w) {
					l = w
				}
				$(this).css({left: l})
				$('#jin').width($(this).width()+l);
				var w = audio.duration.toFixed(2)*($('#jin').width()/winW)
				 $('#play').attr('src', '/media/img/pause.png');
				 aud_play(w)
			});
			$(this).mouseup(function () {
				$(this).unbind('mousemove');
			});
		}
	});
