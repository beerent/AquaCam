<html>
  <style> 
    h1{ font-size:72; text-align: center; }
    #banner{ background-image:  <a href="myfile.htm"><img src="IMG-5707.jpeg"></a>; }
  </style>
  <body>
    <div id = "banner">
      <h1>AQUARICAM!</h1>
    </div>
    <?php
      echo "<center>Please select an Aquarium to view:</center>";

    ?>
    <!-- The form Value's represent the user. There are TWO users,
         Riley (0), and Brent(1).
      -->
    <form action="user.php" 
	  method="post">
      <input type="image" 
	     src="IMG_5733.jpeg"
	     height="42"
	     width="82"
      />
      <input type="hidden" name="Language" value="0">
    </form>

    <form action="user.php" 
	  method="post">
      <input type="image" 
	     src="IMG_5733.jpeg" 
      />
      <input type="hidden" name="Language" value="1">
    </form>

  </body>
</html>
