from flask import Flask
from flask import request
from pprint import pformat


app = Flask(__name__)

HTTP_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']

@app.route('/', methods=HTTP_METHODS)
def hello_world():
  app.logger.info(pformat(request.get_json()))
  return 'ok'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')