from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
import subprocess

app = Flask(__name__)

# Basic Authentication Configuration
app.config['BASIC_AUTH_USERNAME'] = 'username'
app.config['BASIC_AUTH_PASSWORD'] = 'password'
basic_auth = BasicAuth(app)

# Endpoint to receive POST requests
@app.route('/restart_script', methods=['POST'])
@basic_auth.required
def restart_script():
    try:
        # Run the shell script
        result = subprocess.run(['./script_to_run.sh'], check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode('utf-8'))
                
        response = {'status': 'success', 'message': 'Script restarted successfully'}
    except subprocess.CalledProcessError as e:
        response = {'status': 'error', 'message': f'Error restarting script: {e.stderr.decode("utf-8")}'}
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082, debug=False)
