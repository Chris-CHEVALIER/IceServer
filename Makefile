make:
	slice2py MP3Manager.ice
	slice2js MP3Manager.ice

server:
	python Serveur/server.py

client:
	node Client/Client.js