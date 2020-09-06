import socketio


class Logger:
    def __init__(self):
        self.sio = socketio.Client()
        self.url = 'http://127.0.0.1:6969'
        self.namespace = '/'

    def connect(self):
        self.sio.connect(self.url)
        print('Logger connected to server.')
    
    def disconnect(self):
        self.sio.disconnect()
        print('Logger disconnected from the server.')

    def log(self, _str):
        self.sio.emit('message', data=str(_str), namespace=self.namespace)
