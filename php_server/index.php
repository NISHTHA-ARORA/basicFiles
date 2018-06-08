<?php
if(isset($_GET['light'])){
    $light = $_GET['light'];
    
    if($light == "on") {
      $file = fopen("bulb.txt", "w") or die("can't open file");
      fwrite($file, '1');
      fclose($file);
    } 
    else if ($light == "off") {
      $file = fopen("bulb.txt", "w") or die("can't open file");
      fwrite($file, '0');
      fclose($file);
    }
    else {
      $pwmfile = fopen("pwm.txt", "w") or die("can't open file");
      fwrite($pwmfile, $light);
      fclose($pwmfile);
    }

}

?>

<html>
  <head>      
    
    
    <title>LED for Khushbu</title>
  
  </head>
  <body>
        <a href="?light=on" >Turn On</a>
        <br />

        <a href=?light=off" >Turn Off</a>
        <br />

  </body>
</html>

