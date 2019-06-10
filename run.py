# appserver.py
import os
from flask import Flask
from flask import make_response
from flask import jsonify

app = Flask('CloudRun-Sample')

@app.route('/', methods=['GET'])
def get_sample():
    ret = {'get': 'OK'}
    return jsonify(ret)

@app.route('/', methods=['POST'])
def post_sample():
    ret = {'post': 'OK'}
    return jsonify(ret)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
