from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__, static_folder = "static/dist", template_folder = "static")
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    sensors =  { 
        'temperature': 80,
        'distance': 10
    }

    return render_template('index.html', sensors = sensors)

@socketio.on('my event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']})

@socketio.on('my broadcast event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8080, debug=True)
    socketio.run(app, host='0.0.0.0', port=8080, debug=True)
