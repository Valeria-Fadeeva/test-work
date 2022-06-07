<?php

declare(strict_types=1);

$input_content = "FFFFFF";

$input_content_len = mb_strlen($input_content, '8bit');

echo "length of input content = $input_content_len\n";

$filename = "1.bin";

$f_len = filesize($filename);
echo "filesize = $f_len\n";

$fp = fopen($filename, "r+");
if ($fp) {
    echo "file $filename opened\n";
    rewind($fp);
    echo "CURSOR POSITION " . ftell($fp) . "\n";

    $cursor = (int)round($f_len / 2, 0);

    if (0 === fseek($fp, $cursor, SEEK_CUR)) {
        echo "CURSOR POSITION " . ftell($fp) . "\n";

        $second_half_substr = fgets($fp);
        echo "read to var second half substr\n";
        rewind($fp);
        echo "CURSOR POSITION " . ftell($fp) . "\n";

        if (0 === fseek($fp, $cursor, SEEK_CUR)) {
            $res_wr_input_content = fwrite($fp, $input_content);
            echo "CURSOR POSITION " . ftell($fp) . "\n";

            if ($res_wr_input_content !== false) {
                echo "$res_wr_input_content bytes writed to file $filename \n";

                $res_wr_second_half_substr = fwrite($fp, $second_half_substr);

                if ($res_wr_second_half_substr !== false) {
                    echo "$res_wr_second_half_substr bytes writed to file $filename \n";
                } else {
                    echo "error writing to file $filename second half substring\n";
                }
            }
        } else {
            echo "error writing to file $filename input content\n";
        }
    }

    if (fclose($fp)) {
        echo "file $filename closed\n";
    }
}
