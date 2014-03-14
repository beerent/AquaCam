for ($x=0; $x<=10; $x++)
  {
  echo "The number is: $x <br>";
  } <html>
<body>
<h1>Brent's Database</h1>

<?php

$database = mysqli_connect("localhost","root","arcland","aquarameter");

// Check connection
if (mysqli_connect_errno())
  {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  } 
// ******connection complete******

$data = mysqli_query($database, "select * from aquarium");

echo ("<table border = '1'>
       <tr>
       <th>Tank Name</th>
       <th>Active</th>
       </tr>");

while($row = mysqli_fetch_array($data)){
  echo "<tr>";
  echo "<td>" . $row[0] . "</td>";
  echo "<td>" . $row[1] . "</td>";
  echo "</tr>";
}
echo "</table>";

?> 
</body>
</html>

