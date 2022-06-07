<?php
function route($RAW_QS){
	switch ($RAW_QS) {
		case "/":
			$tpl_file = "../template/_main_page_.tpl";
			break;
			
		case "/roadmap":
			require_once('roadmap.php');
			break;
			
		case "/donate";
			$tpl_file = "../template/donate.tpl";
			break;
		
		default:
			$tpl_file = "../template/404.tpl";
			$httpcode = 404;
	}
	
	if (empty($tpl_file)) {
		if (empty($content)) {
			$content = false;
		}
	} else {
		$content = load_template($tpl_file);
	}
	
	if (empty($link)) {
		$link = false;
	}
	
	if (empty($hint)) {
		$hint = false;
	}
	
	if (empty($seconds)) {
		$seconds = false;
	}
	
	if (empty($refresh)) {
		$refresh = false;
	}

	if (empty($httpcode)) {
		$httpcode = false;
	}
	
	return array("content" => $content, "link" => $link, "hint" => $hint, "seconds" => $seconds, "refresh" => $refresh, "httpcode" => $httpcode);
}
