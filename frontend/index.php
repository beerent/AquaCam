<html> 
  <body>
    <br><br><br>
    <?php
      $name = "Brent";
      echo "<center>Welcome to $name's AquaCam!</center>";
      echo "<br><center>What would you like to do?</center>";
    ?>
    
    <br> <br> <br> <br> <center>
    
    <!-- BUTTONS -->    
    <form> 
      <input 
        type = "button" 
        value = "Get Pic of Tank"
        onClick = "window.location.href='./getPic.php'"
      >
    </form>

    <form> 
      <input 
        type = "button" 
        value = "Live Video of Tank!"
        onClick = "window.location.href='./getVid.php'"
      >
    </form>

    </center>

  </body>
</html>
