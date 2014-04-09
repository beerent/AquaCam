<html>
  <body>
  <center>
    <?php
        class Timer {
            private $time = null;
            public function __construct() {
                $this->time = time();
                echo 'Working - please wait..<br/>';
            }

            public function __destruct() {
                echo '<br/>Job finished in '.(time()-$this->time).' seconds.';
            }
        }


      $t = new Timer(); // echoes "Working, please wait.."
      
      sleep(7);     
  //echo "socket closed.<br>";
      unset($t);  // echoes "Job finished in n seconds." n = seconds elapsed
    
    ?>

    <form> 
      <input 
        type = "button" 
        value = "Return To Home"
        onClick = "window.location.href='./'"
      >
    </form>
    </center>

  </body>
</html>
