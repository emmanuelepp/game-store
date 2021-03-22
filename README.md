# Game store notes

<p><strong>Technologies</strong></p>

<ul>
<li>Python3</li>
<li>Flask</li>
<li>MongoDb</li>
<li>Pytest</li>
</ul>


<p><strong>Instalation</strong></p>

<p>1 - Clone the repository</p>

<code>git@github.com:emmanuelepp/game-store.git </code>


<p>2 - Install dependencies</p>

<p>Instal mongodb in your docker container</p>

Mongodb on docker (https://phoenixnap.com/kb/docker-mongodb)

If you have some troubles with the  container (https://stackoverflow.com/questions/37450871/how-to-allow-remote-connections-from-mongo-docker-container)


<p>Go to the game-store folder and runs those commands</p>

<code> python3 -m venv venv </code>

<p>Run the virtual env</p>

<code> source venv/bin/activate </code>

<code> pip3 install flask-script </code>

<code> pip3 install flask-WTF </code>

<code> pip3 install secrets </code>

<code> pip3 install pytest </code>

<code> pip3 install pymongo </code>

<code> pip3 install bcrypt </code>

3 - Run the app

<p>Go to the app folder and run this command</p>

<code> python manage.py runserver</code>

Check http://localhost:5000







