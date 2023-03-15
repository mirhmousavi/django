install:
	rsync -avzh gunicorn.service /etc/systemd/system/
	systemctl daemon-reload
	systemctl restart gunicorn
