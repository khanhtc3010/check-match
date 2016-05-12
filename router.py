from flask import request, abort
from flask import jsonify
from modules.text_processor import *
from app import *

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/check', methods=['GET'])
def check_match_sentence():
	try:
		args = request.args
		src = args.get('src')
		sen = args.get('sen')
		return jsonify({'status': check_match(src, sen)})
	except:
		abort(400)