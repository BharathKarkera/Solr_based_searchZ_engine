#! /bin/bash

temp_value=$(cat /Users/bharathkarkera/practice/python/search_engine2/raw_result.txt|sed '/^$/d'|awk -F'-->' '{printf("<tr bgcolor=#32CD32 height=30px><td  align =\"left\" ><p><a href=\"%s\" target=\"_blank\">%s</a> : %s </p></td></tr>\n",$2,$1,$2)}')

link_result="<table style='border:1px solid black;margin-left:auto;margin-right:auto;'><tr bgcolor=#FFF333 height=30px><th>Links</th></tr>$temp_value</table>"

cat << EOF  > /Users/bharathkarkera/practice/python/search_engine2/templates/test.html

<!DOCTYPE html>

<html>

	<head>



			<style>

			body {

			background-repeat: no-repeat;

			background-attached: fixed;

			background-size: cover;

			background-image: url({{url_for('static',filename='img/background_image1.png')}});



			}



		</style>



		<meta charset="UTF-8">

		<title>Bharath</title>

		<link rel="shortcut icon" href="{{ url_for('static', filename='favicon.ico') }}">

		<link rel="stylesheet" href="{{url_for('static', filename='css/main.css')}}">

	</head>

	<body>

		<br>

		<form action="search" method="post">

			{% for message in get_flashed_messages() %}

				<p> {{message}} </p>

				<p> $link_result </p>

			{% endfor %}

			<br>

			<input type="text" name="search_parameter">

			<br>

			<input type="submit" value="SEARCH" id="search">

		</form>

	</body>

</html>


EOF



exit 0
