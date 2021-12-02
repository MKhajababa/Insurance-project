<?php
for($i = 1;$i<50;$i++){
    $sum = 0;
    for ($j=1; $j < $i; $j++) { 
        if ($i%$j == 0) {
            $sum++;
        }
    }
    if ($sum == 1) {
        echo "$i ";
    }
} 
?>