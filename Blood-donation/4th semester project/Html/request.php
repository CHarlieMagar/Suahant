<?php

include 'db_connection.php';


if(isset($_POST['register'])){
    $name=$_POST['name'];
    $phone=$_POST['phone'];
    $email=$_POST['email'];
    $blood_required=$_POST['blood-require'];
    $message=$_POST["message"];

        $checkEmail="SELECT * From blood_requests where email='$email'";
        $result=$conn->query($checkEmail);
        if($result->num_rows>0){
            echo "Email Address Already Exist !";
        }
        else{
            $insertQuery="INSERT INTO blood_requests(name, phone, email, blood_required, message)
                            VALUES ('$name', '$phone', '$email', '$blood_required', '$message')";
                    if($conn->query($insertQuery)==TRUE){
                        header("location  : RequestBlood.html");
                    }
                    else{
                        echo "Request Sent Successfully".$conn->error;
                    }
        }

}







?>