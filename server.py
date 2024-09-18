from flask import Flask, jsonify
import threading
import time
import random

app = Flask(__name__)

# Function to perform random refresh
def random_refresh():
    while True:
        time.sleep(random.randint(30, 60))
        # Add your refresh logic here

@app.route('/start', methods=['GET'])
def start_refresh():
    threading.Thread(target=random_refresh).start()
    return jsonify({"status": "started"})

@app.route('/stop', methods=['GET'])
def stop_refresh():
    # Logic to stop the refresh
    return jsonify({"status": "stopped"})

if __name__ == '__main__':
    app.run(port=5000)
