<!DOCTYPE html>
<html lang="ru-RU">
	<head>
		<script>
			<!-- //window.checkbrowser = true;
			if (window.checkbrowser) {
				try {
					if (new XMLHttpRequest()) {
						location.replace('/');
					}
				} catch(e) {
					try {
						if (new ActiveXObject('Msxml2.XMLHTTP')) {
							location.replace('/');
						}
					} catch(e) {}
					try {
						if (new ActiveXObject('Microsoft.XMLHTTP')) {
							location.replace('/');
						}
					} catch(e) {}
				}
			}
			-->
		</script>

		<meta charset="utf-8">
		<meta name="msapplication-tap-highlight" content="no">
		<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
		<meta name="HandheldFriendly" content="true">
		
		<script src="/assets/js/badbrowser.js"></script>

		<title>Вы используете устаревший браузер.</title>

		<link rel="stylesheet" href="/assets/css/badbrowser_common.css">
		<link rel="stylesheet" href="/assets/css/badbrowser.css">

		<!--[if lte IE 8]>
		<style>
		#bad_browser {
			border: none;
		}
		#wrap {
			border: solid #C3C3C3;
			border-width: 0px 1px 1px;
		}
		#content {
			border: solid #D9E0E7;
			border-width: 0px 1px 1px;
		}
		</style>
		<![endif]-->
	</head>
	<body class="">
		<div id="bad_browser">
			<div id="head" class="head"></div>
			<div id="wrap"><div id="content">
				Для работы с сайтом необходима поддержка Javascript и Cookies.
				<div>
					Чтобы использовать все возможности сайта, загрузите и установите один из этих браузеров:
					<div id="browsers" style="width: 360px;">
						<a href="https://mozilla.org/" target="_blank" style="background: url(/assets/image/icon/firefox.png) no-repeat 50% 17px;">Firefox</a>
						<a href="https://google.com/chrome/" target="_blank" style="background: url(/assets/image/icon/chrome.png) no-repeat 50% 17px;">Chrome</a>
						<a href="https://opera.com/" target="_blank" style="background: url(/assets/image/icon/opera.png) no-repeat 50% 15px;">Opera</a>
					</div>
				</div>
				<!--Или Вы можете воспользоваться <a href="https://m.fadeeva.me/">версией сайта для мобильных устройств</a>.-->
			</div></div>
		</div>
	</body>
</html>