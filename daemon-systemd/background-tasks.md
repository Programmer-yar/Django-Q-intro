# Background Tasks
- Email is sent to reciever everytime a message is sent in chat
- Email sending is run in background using 'django-q'
- redis data base is used for storing background tasks

## local settings:
- activate virtual environment
- Install all requirements and run migrations
- Start the qcluster using:
```
python manage.py qcluster
```

## production settings:
- In production q cluster should be run as daemon process
- In (`qcluster.service`)[https://github.com/ARPA-Industry/HAMYABI-Web/blob/master/HAMYABIWeb/background%20tasks/qcluster.service]:
	- change the `User` according to your server user
	- change the `ExecStart` and add paths to the project and virtual environement according to the server
- copy the file `qcluster.service` in this folder and place it in `/etc/systemd/system`
- Reload daemon process using:
```
sudo systemctl daemon-reload
```
- enable the process so that it runs everytime system is restarted
```
sudo systemctl enable qcluster.service
```

- start the daemon process:
```
sudo systemctl start qcluster.service
```

- check status of this process:
```
sudo systemctl status qcluster.service
```