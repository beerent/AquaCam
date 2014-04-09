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

        $index_q = mysqli_query($database, "select img_path from img_history where aquarium_name = \"" . $_POST['aquarium_name'] . "\" and ID !=-1 order by date DESC, time DESC");
        $row = mysqli_fetch_array($index_q);
        echo "<img border=\"0\" src=\"" . $row['img_path'] . "\" alt=\"Pulpit rock\" width=\"304\" height=\"228\">";
        echo"<br><br>";

        $index_q = mysqli_query($database, "select time, date, temperature from temp_history where aquarium_name = \"" . $_POST['aquarium_name'] . "\" order by date DESC, time DESC");
        $row = mysqli_fetch_array($index_q);
        
        echo "most current data as of " . $row['time'] . ", " . $row['date'];
        echo "<br><br>";
        //echo "Aquarium Temperature: " . $row['temperature'];
    
        $index_q = mysqli_query($database, "select distinct light_number, power, time, date from light_history order by date DESC, time DESC");
        $row1 = mysqli_fetch_array($index_q);
        $row2 = mysqli_fetch_array($index_q);

        echo"<br>";

        //echo "Light #" . $row1['light_number'] . "| Power: " . $row1['power'];
        //echo"<br>";
        //echo "Light #" . $row2['light_number'] . "| Power: " . $row2['power'];
        //echo"<br>";

        echo "<table border='1'>";
        echo "<tr>";
        echo "<td>" . "Time" . "</td>";
        echo "<td>" . $row['time'] . "</td>";
        echo "</tr>";

        echo "<tr>";
        echo "<td>" . "Date" . "</td>";
        echo "<td>" . $row['date'] . "</td>";
        echo "</tr>";

        echo "<tr>";
        echo "<td>" . "Temperature" . "</td>";
        echo "<td>" . $row['temperature'] . "</td>";
        echo "</tr>";

        echo "<tr>";
        echo "<td>" . "Light " . $row1['light_number'] . "</td>";
        echo "<td>" . $row1['power'] . "</td>";
        echo "</tr>";

        echo "<tr>";
        echo "<td>" . "Light " . $row2['light_number'] . "</td>";
        echo "<td>" . $row2['power'] . "</td>";
        echo "</tr>";
        echo "</table>";

    ?>
    <br>
    <!-- BUTTONS -->
    <form> 
      <input 
        type = "button" 
        value = "Get Current Data"
        onClick = "window.location.href='./getPic.php'"
      >
    </form>
    </center>

  </body>
</html>
