<html>
  <style> 
    h1{ font-size:72; text-align: center; }
    
    #banner{ background-image:  <a href="myfile.htm">
      <img src="IMG-5707.jpeg"></a>; 
    }

    #image{
      width:100%;
      height = 600 px;
      font-size = 72;
      float:right;
    }

  </style>
  <body>
    <div id = "banner">
      <h1>AQUARICAM!</h1>
    </div>
    <center> Please select an Aquarium to view:</center>

    <!-- The form Value's represent the user. There are TWO users,
         Riley (0), and Brent(1).
      -->
    Riley's Fish Tank
    <form action="user.php" 
	  method="post">
      <input type="image" 
	     src="IMG_5733.jpeg";
	     width="20%"
      />
      <input type="hidden" name="Language" value="0">
    </form>
    
    Brent's Turtle Tank
    <form action="user.php" 
	  method="post">
      <input type="image" 
	     src="IMG_5733.jpeg";
	     width="20%"
      />
      <input type="hidden" name="Language" value="1">
    </form>

  </body>
</html>
