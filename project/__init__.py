import os
import datetime
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# we initiate the application
app = Flask(__name__)

# we set the application Configuration
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
})
