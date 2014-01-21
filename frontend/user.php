<html> 
  <body>
    <br><br><br>

      Welcome <?php echo $_POST["Language"]; ?><br>
      Your email address is: <?php echo $_POST["email"]; ?>

    
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
