<?php
$name = $_POST['name'];
$birthdate = $_POST['birthdate'];
$today = new DateTime();
$birthDate = new DateTime($birthdate);
$age = $today->diff($birthDate)->y;

$response = array(
    'name' => $name,
    'age' => $age
);

header('Content-Type: application/json');
echo json_encode($response);
?>
