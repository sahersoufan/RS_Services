from Class.rsCore import rsCore
from flask import Flask, jsonify, request

restPort = 8050
app = Flask(__name__)



@app.route('/setSqlInfo', methods=["POST"])
def setSqlInfo():
    try:
        sqlInfo = request.get_json(force=True)
        rsCore.setSqlInfo(sqlInfo)
        return jsonify(success=True)
    except:
        return jsonify(success=False)



@app.route('/initializeRecoSys', methods=['POST'])
def initiate():
    try:
        rsCore.initiate()
        return jsonify(success=True)
    except:
        return jsonify(success=False)



# @app.route('/updateRecoSys', methods=['POST'])
# async def update():
#     try:
#         await rsCore.update()
#         return jsonify(success=True)
#     except:
#         return jsonify(success=False)


@app.route('/getReco', methods=['POST'])
def getRecommend():
    try:
        userServices = request.get_json(force=True)
        r = rsCore.getRecommend(userServices)
        return jsonify(r)
    except:
        return jsonify(success=False)


@app.route('/test', methods=['GET'])
def testF():
    # data = request.get_json(force=True)
    return 'it\'s a good way to communcation'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = restPort)