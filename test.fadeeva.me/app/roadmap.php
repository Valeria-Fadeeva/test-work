<?php
declare(strict_types=1);

class TestConnDB extends SQLite3
{
	private $filename;

    function __construct($path, $dbname)
    {
		$this->filename = $path . $dbname;

		if (file_exists($path)) {
			if (!is_writable($path)) {
				throw new Exception('Папка недоступна для записи ' . $path);
			}
		} else {
			throw new Exception('Папка не существует ' . $path);
		}

		if (file_exists($this->filename)) {
			if (!is_writable($this->filename)) {
				throw new Exception('Файл БД недоступен для записи ' . $this->filename);
			} 
		}	

		$this->open($this->filename);
    }
}

const PATH = '../db/';
const DBNAME = 'valeria.sqlite';
const SQL_FILE = 'valeria.dump.sql';

$test_conn_db = new TestConnDB(PATH, DBNAME);
unset($test_conn_db);

$pdo = new PDO("sqlite:". PATH . DBNAME);

$check_db_empty = "
SELECT name FROM sqlite_master
WHERE type IN ('table','view') AND name NOT LIKE 'sqlite_%'
UNION ALL
SELECT name FROM sqlite_temp_master
WHERE type IN ('table','view')
ORDER BY 1";

$check = $pdo->query($check_db_empty)->fetchAll();

$content = '';
if (empty($check)) {
	$sql_f = PATH . SQL_FILE;

	if (file_exists($sql_f)) {
		$handle = fopen($sql_f, "r");

		if ($handle) {
			while (($line = fgets($handle)) !== false) {
				if (!empty($line) AND !str_starts_with($line, '--') AND !str_starts_with($line, 'BEGIN TRANSACTION') AND !str_starts_with($line, 'COMMIT')) {
						$sql .= $line;
					}
			}
		}

		fclose($handle);	
	}

	$pdo->beginTransaction();
	$import_result = $pdo->exec($sql);
	$pdo->commit();

	if ($import_result) {
		$content = 'Импорт данных в БД выполнен. Вы можете перезагрузить страницу для дальнейшей работы.';
	} else {
		$content = 'Импорт данных в БД не удался.';
	}
} else {
	$sql = "
	SELECT `post`.`id` AS `p_id`, 
	`post`.`type` AS `p_type`, 
	`post`.`header` AS `p_header`, 
	`post`.`content` AS `p_content`, 
	`post`.`table_of_contents` AS `p_table_of_contents`, 
	`post`.`date` AS `p_date`, 
	`post`.`column` AS `p_col`, 
	`post_type`.`id` AS `pt_id`, 
	`post_type`.`type` AS `pt_type` 
	FROM `post` LEFT OUTER JOIN `post_type` ON `post`.`type` = `post_type`.`id`
	WHERE `post`.`hidden` IS NOT TRUE ORDER BY date(`p_date`) ASC LIMIT 0, 30";

	$posts = $pdo->query($sql)->fetchAll(PDO::FETCH_ASSOC);

	$tpl_page = 
	"					<div class='blog-post clearfix'>
							<h4 class='blog-post-title'>Планы</h2>
							<p class='blog-post-meta'></p>
							
							<div class='row'>
								<div class='col-12 center'>
									Приоритеты
								</div>
							</div>
							
							<div class='row'>
								<div class='col center'>
									1
								</div>
								<div class='col center'>
									2
								</div>
							</div>
	{CONTENT}
						</div>
	";

	$tpl_row = 
	"						<div class='row'>
	{col}
							</div>
	";

	$tpl_col = 
	"							<div class='col {class}'>
									<form>
										<input type='hidden' value='{p_id}'>
										<div class='card rm-card' style='width: 100%'>
											<div class='card-header'>
												{pt_type}
											</div>
											<div class='card-body'>
												<h6 class='card-title'>
													{p_header}
												</h6>
	{progress}
												
	{table_of_contents_block}
											</div>
											<div class='card-footer' title='{date_human_month}'>
												{p_date}
											</div>
										</div>
									</form>
								</div>
	";

	$tpl_empty_col = 
	"							<div class='col {class}'>
								</div>
	";

	$tpl_progress = 
	"											<div class='card-text progress'>
													<div class='progress-bar progress-bar-striped progress-bar-animated bg-success' 
													role='progressbar' 
													aria-valuenow='{progress_cur}' 
													aria-valuemin='0' 
													aria-valuemax='{progress_max}'>
													</div>
												</div>
												<div class='card-text'>
													{progress_cur} из {progress_max} страниц.
												</div>
												<div class='card-text'>
													{days_cur} из {days_max} дней. <br>
													{weeks_estimate} недель на выполнение.
												</div>
												<br>
	";

	$table_of_contents_tpl = 
	"											<div class='card-text'>
	{accordion_tpl}
												</div>
	";

	$accordion_tpl = 
	"												<div class='accordion accordion-flush' id='accordion_flush_{view_post_id}'>
														<div class='accordion-item'>
															<h2 class='accordion-header' id='flush-heading_{view_post_id}'>
															<button class='accordion-button collapsed' type='button' data-bs-toggle='collapse' data-bs-target='#flush-collapse_{view_post_id}' aria-expanded='false' aria-controls='flush-collapse_{view_post_id}'>
																Оглавление
															</button>
															</h2>
															<div id='flush-collapse_{view_post_id}' class='accordion-collapse collapse' aria-labelledby='flush-heading_{view_post_id}' data-bs-parent='#accordion_flush_{view_post_id}'>
																<div class='accordion-body'>
	{table_of_contents}
																</div>
															</div>
														</div>
													</div>
	";


	$html = "";
	$row_block = "";
	$last_p_date = "";

	$col_array = array();

	$view_post_id = 0;

	foreach($posts as $sql_row) {
		$progress = "";
		if (!empty($sql_row['p_content'])) {
			$a = explode(':', $sql_row['p_content']);

			if (count($a) == 1) {
				$p_content_arr = explode(';', $sql_row['p_content']);
			} else if (count($a) > 1) {
				$p_content_arr = explode(';', $a[0]);
			}

			if (is_array($p_content_arr) AND count($p_content_arr) == 2) {
				$progress = str_replace(
				array('{progress_cur}', '{progress_max}', '{days_cur}', '{days_max}', 
					'{weeks_estimate}'), 
				array($p_content_arr[0], $p_content_arr[1], round($p_content_arr[0]/25/1.66), round($p_content_arr[1]/25/1.66), 
					round(
						($p_content_arr[1]/25/1.66 - $p_content_arr[0]/25/1.66) * 2 / 7
						)
					), 
				$tpl_progress);
			}
		}

		$table_of_contents = '';
		if ($sql_row['p_table_of_contents']) {
			foreach(preg_split("/((\r?\n)|(\r\n?))/", $sql_row['p_table_of_contents']) as $line) {
				// do stuff with $line
				$line_arr = explode('|', $line);
				if (is_array($line_arr) AND count($line_arr) == 2 AND is_array($p_content_arr) AND count($p_content_arr) == 2) {
					if (!empty($line_arr[1]) AND $p_content_arr[0] >= $line_arr[1]) {
						$table_of_contents .= PHP_EOL . "<p class='text-success'>" . "(" . $line_arr[1] . ") " . $line_arr[0] . "</p>" . PHP_EOL;
					} else {
						$table_of_contents .= PHP_EOL . "<p>" . "(" . $line_arr[1] . ") " . $line_arr[0] . "</p>" . PHP_EOL;
					}
				} else {
					if (count($line_arr) == 1 AND empty($line_arr[0])) {
						$table_of_contents .= "<br>";
					} else {
						$table_of_contents .= PHP_EOL . "<p>" . $line_arr[0] . "</p>" . PHP_EOL;
					}
					
				}
			}
		}

		if (!empty($table_of_contents)) {
			$accordion_block = str_replace(
			array("{table_of_contents}", "{view_post_id}"), 
			array($table_of_contents, $view_post_id), 
			$accordion_tpl);

			$table_of_contents_block = str_replace(
			"{accordion_tpl}",
			$accordion_block,
			$table_of_contents_tpl);
		} else {
			$table_of_contents_block = "";
		}

		$view_post_id++;

		$p_date = str_replace(
		"-",
		".",
		$sql_row['p_date']);

		list($sql_row_yyyy, $sql_row_mm, $sql_row_dd) = explode('-', $sql_row['p_date']);

		$date_human_month = date("F", mktime(0, 0, 0, intval($sql_row_mm), intval($sql_row_dd), intval($sql_row_yyyy)));
		
		switch ($sql_row['p_col']) {
			case "0":
				$html_class = "col-sm-12 col-md-12";
				break;
				
			case "1":
				$html_class = "col-sm-12 col-md-6 order-{$sql_row['p_col']}";
				break;
				
			case "2":
				$html_class = "col-sm-12 col-md-6 order-{$sql_row['p_col']}";
				break;
		}
		
		$col_block = str_replace(
		array("{p_id}", "{pt_type}", "{p_header}", "{p_content}", "{table_of_contents_block}", "{p_date}", "{date_human_month}", "{class}", "{progress}"), 
		array($sql_row['p_id'], $sql_row['pt_type'], $sql_row['p_header'], $sql_row['p_content'], $table_of_contents_block, $p_date, $date_human_month, $html_class, $progress), 
		$tpl_col);
		
		$col_array[$p_date][] = array($col_block, $sql_row['p_col']);
		
		$last_p_date = $p_date;
	}

	$html_class_1 = "col-sm-12 col-md-6 order-1";
	$html_class_2 = "col-sm-12 col-md-6 order-2";

	$empty_col_order_block_array = array();

	$empty_col_order_block_array[] = str_replace(
	"{class}", 
	$html_class_1, 
	$tpl_empty_col);

	$empty_col_order_block_array[] = str_replace(
	"{class}", 
	$html_class_2, 
	$tpl_empty_col);

	foreach($col_array as $html_col) {
		
		if (is_array($html_col)) {
			$html_cols = "";
			
			switch (count($html_col)) {
				case 1:
					if ($html_col[0][1] == 0) {
						$html_cols = $html_col[0][0];
						
					} else if ($html_col[0][1] == 1) {
						$html_cols = $html_col[0][0] . $empty_col_order_block_array[1];
						
					} else if ($html_col[0][1] == 2) {
						$html_cols = $empty_col_order_block_array[0] . $html_col[0][0];
						
					} 
					break;
					
				case 2:
					$html_cols = $html_col[0][0] . $html_col[1][0];
					break;
			}
		}

		$row_block = str_replace(
		"{col}",
		$html_cols,
		$tpl_row);
		
		$html .= $row_block;
	}

	$content = str_replace("{CONTENT}", $html, $tpl_page);
}
