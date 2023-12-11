from flask import Flask, render_template

app = Flask(__name__)

# Dummy data for demonstration purposes
devices = [
    {"name": "Device 1", "ip": "192.168.1.1"},
    {"name": "Device 2", "ip": "192.168.1.2"},
    {"name": "Device 3", "ip": "192.168.1.3"},
    {"name": "Device 4", "ip": "192.168.1.4"},
    {"name": "Device 5", "ip": "192.168.1.5"},
]

@app.route('/')
def index():
    return render_template('dashboard.html', devices=devices)

if __name__ == '__main__':
    app.run(debug=True)
