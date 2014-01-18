<html>
  <body>
    <?php
      
      error_reporting(E_ALL);
      echo "opening socket.\n";
      $host = "127.0.0.1";
      $port = 5678;
      $socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
      if($socket == false) {
        echo "failed socket creation.\n";
      }
      echo "socket created.\n";
      $result = socket_connect($socket, $host, $port);
      if(result == false){
        echo"failed connection to server.\n";
      }   
      echo "connection made.\n";

      $out = "test\n";
      socket_write($socket, $in, strlen($in));
      echo "data sent\n.";

      fclose($socket);      
      echo "socket closed.\n";
    ?>
  </body>
</html>
