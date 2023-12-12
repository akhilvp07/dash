#Run your Flask app:
```
python app.py
```
HOST variable configured in app.py sets the host IP.
Visit http://127.0.0.1:5000/ in your web browser to see the dashboard displaying the devices and their IP addresses.

=========================
Run app:
 gunicorn -w 4 -b  172.18.55.68:5000 app:app