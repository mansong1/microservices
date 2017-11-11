from flask import Flask, jsonify

# we initiate the application
app = Flask(__name__)

# we set the application Configuration
app.config.from_object('project.config.DevelopmentConfig')

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status':'success',
        'message':'pong!'
})
