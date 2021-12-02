<?php
    $str = "Hello,How are you.";
    $l = strlen($str);
    $wl = str_word_count($str);
    $rstring = strrev($str);
    echo "Length of String = $l";
    echo "<br>";
    echo "Word count of string = $wl";
    echo "<br>";
    echo "Reverse of String = $rstring";
    echo "<br>";
    if (strpos($str,"are")) {
        echo "The word 'are' exsist.";
    }
    else{
        echo "The word 'are' not exsist.";
    }


?>