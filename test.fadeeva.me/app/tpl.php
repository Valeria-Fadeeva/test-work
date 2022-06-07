<?php
function load_template($tpl_file = false) {
	
	if (!empty($tpl_file)) {
		if (file_exists($tpl_file . '.html')) {
			$handle = fopen($tpl_file . '.html', "r");
			$tpl = fread($handle, filesize($tpl_file . '.html'));
			fclose($handle);
			
			return $tpl;
		}
	}
	
	return false;
}
