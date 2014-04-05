<html>
 <head>
  <title>Aquarameter</title>
 </head>
 <body>
 <?php 
 
   $database = mysqli_connect("localhost","root","cuse1234","aquarameter");
   // Check connection
   if (mysqli_connect_errno()){
     echo "Failed to connect to MySQL: " . mysqli_connect_error();
   } else {
   	 echo "brent we in dis bitch";
   }

   mysqli_close($database);
 ?> 
 </body>
</html>