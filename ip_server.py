from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

device_info = {}

@app.route('/register', methods=['POST'])
def register_ip():
    data = request.get_json()
    device_name = data.get('name')
    ip = data.get('ip')
    
    if device_name and ip:
        device_info[device_name] = ip
        print('name: ', device_name, 'ip:', ip)
        return jsonify({'status': 'success', 'name': device_name, 'ip': ip}), 200
    else:
        return jsonify({'status': 'failure', 'message': 'Invalid request'}), 400

@app.route('/get_ips', methods=['GET'])
def get_ips():
    return jsonify(device_info), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

