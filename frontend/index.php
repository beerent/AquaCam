<html>
  <style> 
    h1{font-size:72; text-align: center;}
    footer{font-size:8; text-align:center;}

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
      <h1>AQUARAMETER!</h1>
    </div>
    <center> Please select an Aquarium to view:</center>
    
    <br><br><br>

    <!-- The form Value's represent the user. There are TWO users,
         Riley (0), and Brent(1).
      -->
      <center>
<?php 
 
  $database = mysqli_connect("localhost","root","cuse1234","aquarameter");
  // Check connection
  if (mysqli_connect_errno()){
    echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }

  $name = mysqli_query($database, "select owner, aquarium_name, img_path from aquarium, img_history where img_history.");

  while($row = mysqli_fetch_array($name)){
    echo $row['owner'] . "'s tank: " . $row['aquarium_name'];
    echo "<br>";
  }

  $img = mysqli_query($database, "select aquarium.aquarium_name, aquarium.owner, img_path from aquarium, img_history where aquarium.aquarium_name = img_history.aquarium_name and img_history.ID = -1");
  while($row = mysqli_fetch_array($img)){
    echo $row['owner'] . "'s tank: " . $row['aquarium_name'];
    echo "<br>";
    echo "<form action=\"user.php\" 
    method=\"post\">
      <input type=\"image\" 
       src=\"" . $row['img_path'] . "\"\;
       width=\"20%\"
      />
      <input type=\"hidden\" name=\"user\" value=\"0\">
    </form>";
  }

   mysqli_close($database);
 ?> 
    </center>
    <footer>Brent Ryczak (brentryczak@gmail.com)</footer>
  </body>
</html>
