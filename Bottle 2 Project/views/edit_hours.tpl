% rebase('layout.tpl', title='Update Data')

<form action='/editHours' method='POST'>
    <input type='text' name='eid' required="required"> Employee ID<br><br>
    <input type='text' name='hrs' required="required"> Enter hours<br><br>
    <input type="submit" value='Submit Query'>
</form>
