build:
	echo "Hello, World"
	python3 -m venv venv
	./venv/bin/pip3 install -r requirements.txt

run:
	./venv/bin/python3 hooker.py

test:
	curl -X POST -u username:password http://localhost:8090/restart_script