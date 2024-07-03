<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Age Calculator</title>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>

<style>
    <style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f0f0f0;
        padding: 20px;
    }
    h2 {
        text-align: center;
        color: #333;
    }
    form {
        max-width: 400px;
        margin: 0 auto;
        background-color: #fff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    label {
        font-weight: bold;
    }
    input[type="text"],
    input[type="date"],
    input[type="submit"] {
        width: 100%;
        padding: 10px;
        margin-bottom: 10px;
        box-sizing: border-box;
        border: 1px solid #ccc;
        border-radius: 4px;
        font-size: 16px;
    }
    input[type="submit"] {
        background-color: #4CAF50;
        color: white;
        cursor: pointer;
    }
    input[type="submit"]:hover {
        background-color: #45a049;
    }
    #result {
        margin-top: 20px;
        padding: 10px;
        background-color: #fff;
        border-radius: 8px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
</style>
</style>
</head>
<body>

<h2>Age Calculator</h2>

<form id="ageForm">
    <label for="name">Name:</label><br>
    <input type="text" id="name" name="name" required><br><br>
    
    <label for="birthdate">Birthdate:</label><br>
    <input type="date" id="birthdate" name="birthdate" required><br><br>
    
    <input type="submit" value="Calculate Age">
</form>

<div id="result"></div>

<script>
$(document).ready(function() {
    $('#ageForm').submit(function(e) {
        e.preventDefault();
        
        var formData = {
            name: $('#name').val(),
            birthdate: $('#birthdate').val()
        };
        
        $.ajax({
            type: 'POST',
            url: 'calculate_age.php',
            data: formData,
            dataType: 'json',
            success: function(response) {
                $('#result').html('<p>Hello, ' + response.name + '! You are ' + response.age + ' years old.</p>');
            },
            error: function() {
                $('#result').html('<p>An error occurred while processing your request.</p>');
            }
        });
    });
});
</script>

</body>
</html>
