<html> 
  <body>
 
    <?php 
      $name = "Brent";
      echo "<center>Welcome to $name's AquaCam!</center>";
      echo "<br><center>What would you like to do?</center>";
    ?>

    <br> <center>
    <form>
      <input type = "button" value = "Get Pic of Tank"
      onClick = "window.location.href='./getPic.php'">
    </form>
    </center>

  </body>
</html>