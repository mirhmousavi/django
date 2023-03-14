install:
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt
	rsync -avzh gunicorn.service /etc/systemd/system/
	- ln -s ${PWD} /django
	systemctl daemon-reload
	systemctl restart gunicorn
