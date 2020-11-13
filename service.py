from flask import Flask
from flask import request
import socket
import os
import sys
import requests

app = Flask(__name__)

@app.route('/test', methods=['GET', 'POST'])
def test():
	app.logger.info(request.json)
	return socket.gethostbyname(socket.gethostname())

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
