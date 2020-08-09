from flask import Flask
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app)

temp_list = []


@socketio.on('message')
def create_logs(message):
    if len(temp_list) > 500:
        temp_list.clear()

    temp_list.append(str(message))
    print('LOG: ' + message)
    access_logs()


def access_logs():
    print('Broadcasting now...')
    send(temp_list, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, port=6969, log_output=True)