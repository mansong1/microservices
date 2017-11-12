import os
from flask import Flask, jsonify

# we initiate the application
app = Flask(__name__)

# we set the application Configuration
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

print(app.config)

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status':'success',
        'message':'pong!'
})
