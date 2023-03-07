# Google-EAFIT-Translator

Software for voice2voice translate system without machine lerning via sockets

### Install
	
	pip install -r requeriments.txt

### Run 

Run the first instance

	python server.py

Run the second instance
	
	python client.py

talk to the second instance and frist instance will answer you

### Configuration

How to change langues?

Edit tools/tools.py and change 

	FROMIDIOM="prefix of langue 1"
	TOIDIOM="prefix of langue 1"

**Example:**

	FROMIDIOM="es"
	TOIDIOM="de"


How to conect with other computer?

Two computers must be on the same network, at the same port and host.

you can change that in tools/tools.py and change port and host

**Example:**

	PORT=12345
	HOST='0.0.0.0'
	
notes:

is very sensible to noise
