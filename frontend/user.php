<?php session_start(); ?>
<html> 
  <body>
    <center>
    <?php     
       if ($_POST["user"] == 1){
         $_SESSION['name'] = "Brent";
         $_SESSION['ip'] = "192.168.1.141";
         $_SESSION['port'] = 5678;
         $userPORT = 5678;

       } else if ($_POST["user"] == 0){
         $_SESSION['name'] = "Riley";
         $_SESSION['ip'] = "192.168.1.142";
         $_SESSION['port'] = 5678;
       }

       echo "You Are Viewing ", $_SESSION['name'], "'s Aquarium.";
    ?>
    <!-- BUTTONS -->    
    <form> 
      <input 
        type = "button" 
        value = "Get Pic of Tank"
        onClick = "window.location.href='./getPic.php'"
      >
    </form>
<!--
    <form> 
      <input 
        type = "button" 
        value = "Live Video of Tank!"
        onClick = "window.location.href='./getVid.php'"
      >
    </form>
-->
    </center>

  </body>
</html>
