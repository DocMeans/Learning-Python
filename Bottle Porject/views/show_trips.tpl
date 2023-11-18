<!DOCTYPE html>
<html>
<head>
<title>All Trips</title>
<style>
        body{
        background-color: tan;
        }
        </style>
</head>
<body>
    <h3>Trips</h3>
    <table>
        <tr>
            <th>User</th>
            <th>Date</th>
            <th>Destination</th>
            <th>Miles</th>
            <th>Gallons</th>
        </tr>
        %for row in rows:
            <tr>
                %for col in row:
                    <td>{{col}}</td>
                %end
            </tr>
        %end
    </table>
</body>
</html>