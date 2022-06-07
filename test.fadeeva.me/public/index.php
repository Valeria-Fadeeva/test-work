<?php
declare(strict_types=1);

error_reporting(E_ALL);
ini_set('display_errors', '1');
ini_set('display_startup_errors', '1');

set_exception_handler(function($exception) {
    // @var Exception $exception
    echo $exception->getMessage(), "\n<br>\n";
    echo $exception->getFile(), ':', $exception->getLine(), "\n<br>\n";
    echo $exception->getTraceAsString(), "\n<br>\n";
});

date_default_timezone_set('UTC');
require_once('../app/init.php');

$req = get_request();

if ( $req ) {
	$QS = $req;
	$RAW_QS = rawurldecode($req);
	$code_escape_qs = htmlspecialchars($RAW_QS, ENT_QUOTES | ENT_HTML401 | ENT_XML1 | ENT_XHTML | ENT_HTML5);
	
	$retval = route($code_escape_qs);
	
	if (!empty($retval['refresh'])) {
		header('Refresh: ' . $retval['seconds'] . '; URL=' . $retval['link']);
		$tpl = load_template('../template/redirect.tpl');
		$retval['content'] = str_replace(array("{seconds}", "{link}", "{hint}"), array($retval['seconds'], $retval['link'], $retval['hint']), $tpl);
	}
	
	if (!empty($retval['content'])) {
		if (!empty($retval['httpcode'])) {
			$response_code = $retval['httpcode'];
			http_response_code($response_code);
		}
		$tpl = load_template('../template/index.tpl');
		$content = str_replace(array("{CONTENT}"), array($retval['content']), $tpl);
		
	} else {
		$response_code = 404;
		http_response_code($response_code);
		$content = "404 Not Found";
	}
	
	print($content);
}