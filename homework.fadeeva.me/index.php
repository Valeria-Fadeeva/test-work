<?php
$tpl = 
"<!DOCTYPE html>
<html lang='ru' dir='ltr'>
	<head>
		<meta charset='utf-8'>
		<title></title>
		<meta name='description' content='Демонстрация кода домашних заданий'>
		<meta name='viewport' content='width=device-width, initial-scale=1'>
		<link rel='stylesheet' href='//unpkg.com/@highlightjs/cdn-assets@11.2.0/styles/default.min.css'>
		<script src='//unpkg.com/@highlightjs/cdn-assets@11.2.0/highlight.min.js'></script>
		<style>
			div.container {
				margin-left: 0%;
				margin-right: 0%;
			}

			div.code {
				padding: 1rem;
				white-space: break-spaces;
				overflow-wrap: break-word;
			}

			@media screen and (min-width : 320px) {
				container {
					margin-left: 0%;
					margin-right: 0%;
				}
			}

			@media screen and (min-width : 480px) {
				div.container {
					margin-left: 0%;
					margin-right: 0%;
				}
			}

			@media screen and (min-width : 720px) and (orientation: landscape) {
				div.container {
					margin-left: 10%;
					margin-right: 10%;
				}
			}

			@media screen and (min-width : 1224px) and (orientation: landscape) {
				div.container {
					margin-left: 15%;
					margin-right: 15%;
				}
			}

			@media screen and (min-width : 1600px) and (orientation: landscape) {
				div.container {
					margin-left: 20%;
					margin-right: 20%;
				}
			}
			
			@media screen and (min-width : 1824px) and (orientation: landscape) {
				div.container {
					margin-left: 25%;
					margin-right: 25%;
				}
			}

			/*@media screen and (min-width : 29em) {
				div.container {
					margin-left: 0%;
					margin-right: 0%;
				}
			}

			@media screen and (min-width : 35em) {
				div.container {
					margin-left: 10%;
					margin-right: 10%;
				}
			}*/
		</style>
	</head>
	<body>
		<div class='container'>
			<a href='{php_file}' target='_blank'>{php_file}</a>
			<div class='code'>
				<code class='language-php hljs'>
{text}
				</code>
			</div>
		</div>
	</body>
	<script>
		//hljs.highlightAll();
		// first, find all the div.code blocks
		document.querySelectorAll('div.code').forEach(el => {
		// then highlight each
		hljs.highlightElement(el);
		});
	</script>
</html>";

function load_template($tpl_file = false) {
	
	if (!empty($tpl_file)) {
		if (file_exists($tpl_file)) {
			$handle = fopen($tpl_file, "r");
			$tpl = fread($handle, filesize($tpl_file));
			fclose($handle);
			
			return $tpl;
		}
	}
	
	return false;
}

$php_file = 'oop-tank.php';
$text = load_template('oop-tank.php');
$text = htmlspecialchars($text, ENT_QUOTES | ENT_HTML401 | ENT_XML1 | ENT_XHTML | ENT_HTML5);
$text = str_replace('<?php', '', $text);
$text = str_replace('{text}', $text, $tpl);
$text = str_replace('{php_file}', $php_file, $text);
echo $text;
