<?php session_start(); ?>
<html> 
  <body>
    <center>
    <?php
        echo "You Are Viewing ", $_POST['owner'], "'s Aquarium: ", $_POST['aquarium_name'];
        echo "<br><br><br>";

        $database = mysqli_connect("localhost","root","cuse1234","aquarameter");
        if (mysqli_connect_errno()){
          echo "Failed to connect to MySQL: " . mysqli_connect_error();
        }

        $index_q = mysqli_query($database, "select img_path from img_history where aquarium_name = \"" . $_POST['aquarium_name'] . "\" and ID =-1");
        $row = mysqli_fetch_array($index_q);
        echo "<img border=\"0\" src=\"" . $row['img_path'] . "\" alt=\"Pulpit rock\" width=\"304\" height=\"228\">";
        echo"<br><br>";

        $index_q = mysqli_query($database, "select time, date, temperature from temp_history where aquarium_name = \"" . $_POST['aquarium_name'] . "\" order by time ASC, date ASC");
        $row = mysqli_fetch_array($index_q);
        
        echo "most current data as of " . $row['time'] . ", " . $row['date'];
        echo "<br><br>";
        echo "Aquarium Temperature: " . $row['temperature'];
        
        //$index_q = mysqli_query($database, "select time, date, light_number from temp_history where aquarium_name = \"" . $_POST['aquarium_name'] . "\"");
        //$row = mysqli_fetch_array($index_q);


        //echo $row['owner'] . "'s Aquarium: " . $row['aquarium_name'];
    ?>
    <!-- BUTTONS -->
    <form> 
      <input 
        type = "button" 
        value = "Get Current Data"
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
