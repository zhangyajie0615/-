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

	var cont = $("#yuan");
	var contW = $("#yuan").width();
	var startX, sX, moveX, disX;
	var winW = $('#Progress').width();