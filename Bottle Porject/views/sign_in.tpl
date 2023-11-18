<!DOCTYPE html>
<html>
<head>
    <title>Sign In</title>
    <style>
        body{
        background-color: tan;
        }
        </style>
</head>
<body>
    <h1>Sign In</h1>
    <form action="/login" method="post">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>

        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>

        <button type="submit">Sign In</button>
    </form>
</body>
</html>
