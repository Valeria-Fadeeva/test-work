<?php

declare(strict_types=1);

$filename = "1.bin";

$f_len = filesize($filename);
echo "filesize = $f_len\n";

$fp = fopen($filename, "r+");
if ($fp) {
    echo "file $filename opened\n";
    rewind($fp);
    fseek($fp, $f_len - 1, SEEK_CUR);

    for ($i = 0; $i < $f_len; $i++) {
        echo "CURSOR POSITION " . ftell($fp) . "\n";

        if (false !== ($char = fgetc($fp))) {
            echo "$char\n\n";
        }

        fseek($fp, -2, SEEK_CUR);
    }

    if (fclose($fp)) {
        echo "file $filename closed\n";
    }
}
