% rebase('layout.tpl', title='View by Department')

<h4>Choose department<h4>
<form action='/getDepartment' method='POST'>
	<label for="dept">Department:</label>
	<select id="dept" name="dept" required>
		<option value='advertising'>Advertising</option>
		<option value='environment'>Environment</option>
		<option value='maintenance'>Maintenance</option>
		<option value='shipping'>Shipping</option>
	</select>

	<input type='submit' value='Submit Query'>
<form>
