<?php
function php_func(){

//echo file_get_contents('file.txt'); // foo
    $command = escapeshellcmd('pythontest.py');
    $output = shell_exec($command);
    echo $output;
}
php_func();
?>

