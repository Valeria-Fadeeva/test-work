<?php
declare(strict_types=1);

error_reporting(E_ALL);
ini_set('display_errors', '1');
ini_set('display_startup_errors', '1');

set_exception_handler(function($exception) {
    /** @var Exception $exception */
    echo $exception->getMessage(), "<br/>\n";
    echo $exception->getFile(), ':', $exception->getLine(), "<br/>\n";
    echo $exception->getTraceAsString(), "<br/>\n";
});

class Agent {};

(object)$a = new Agent();
$a->mind = 100;

echo $a->mind;

echo "<br>";

(string)$b = '100';
(int)$c = 100.15;
(int)$d = $b + $c;
echo (int)$d;