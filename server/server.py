from Class.rsCore import rsCore
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'this is my first api'

@app.route('/post', methods=["POST"])
def post():
    input_json = request.get_json(force=True)
    dictToReturn = {'data':input_json['data']}
    return jsonify(dictToReturn['data'])

@app.route('/initializeRecoSys', methods=['GET'])
def initiate():
    rsCore.initiate()
    return 'bla bla'
@app.route('/updateRecoSys', methods=['GET'])
async def update():
    await rsCore.update()
    return 'bla bla'

@app.route('/getReco', methods=['POST'])
def getRecommend():
    userServices = request.get_json(force=True)
    r = rsCore.getRecommend(userServices)
    return jsonify(r)


app.run()