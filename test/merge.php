<?php

    $a1 = [21,5,89,45,6];
    $a2 = [45,65,2,35,66];
    $a1 = array_merge($a1,$a2);
    $l = count($a1);
    rsort($a1);
    for ($i=0; $i < $l ; $i++) { 
        echo "$a1[$i] ";
    }

?>