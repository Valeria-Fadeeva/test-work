<?php
function get_request() {
	if ( !empty( $_SERVER['QUERY_STRING'] ) ) {
		return $_SERVER['QUERY_STRING'];
	} else if ( !empty( $_SERVER['REQUEST_URI'] ) ) {
		return $_SERVER['REQUEST_URI'];
	}
	
	return false;
}
