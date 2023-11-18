<!DOCTYPE html>
<html>
<head>
    <tittle>Trip Entry</tittle>
</head>
    <style>
        body{
        background-color: tan;
        }
    </style>
<body>
    <form action='/add_trip' method='POST'>
        <input type='text' name='user' required="required">Username<br><br>
        <input type='text' name='date' required="required">Date<br><br>
        <input type='text' name='dest' required="required">destination<br><br>
        <input type='text' name='miles' required="required">Miles traveled<br><br>
        <input type='text' name='gallons' required="required">Gallons used<br><br>
        <input type="submit">
    </form>
</body>
</html>