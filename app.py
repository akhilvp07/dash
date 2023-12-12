from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Define the host variable
HOST = '192.168.0.108'

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

@app.route('/add_device', methods=['POST'])
def add_device():
    data = request.get_json()
    new_device = {
        'name': data['name'],
        'ip': data['ip']
    }
    devices.append(new_device)
    return jsonify(devices)

if __name__ == '__main__':
    # Change the host parameter to your desired IP address
    app.run(host=HOST, port=5000, debug=True)
