<?php
function php_func(){

//echo file_get_contents('file1.txt'); // foo
    $command = escapeshellcmd('pythontest1.py');
    $output = shell_exec($command);
    echo $output;
}
php_func();
?>
