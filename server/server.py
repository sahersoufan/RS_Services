from traceback import print_exc
from Class.rsCore import rsCore
from flask import Flask, jsonify, request

from Class.rsCore import rsCoreV2

restPort = 8050
app = Flask(__name__)



# @app.route('/setSqlInfo', methods=["POST"])
# def setSqlInfo():
#     try:
#         sqlInfo = request.get_json(force=True)
#         rsCore.setSqlInfo(sqlInfo)
#         return jsonify(success=True)
#     except:
#         return jsonify(success=False)



# @app.route('/initializeRecoSys', methods=['POST'])
# def initiate():
#     try:
#         rsCore.initiate()
#         return jsonify(success=True)
#     except:
#         return jsonify(success=False)



# @app.route('/updateRecoSys', methods=['POST'])
# async def update():
#     try:
#         await rsCore.update()
#         return jsonify(success=True)
#     except:
#         return jsonify(success=False)


# @app.route('/getReco', methods=['POST'])
# def getRecommend():
#     try:
#         userServices = request.get_json(force=True)
#         r = rsCore.getRecommend(userServices)
#         return jsonify(r)
#     except:
#         raise
        # return jsonify(success=False)

###############################################################
#                     EMBEDDING
###############################################################
@app.route('/setSqlInfo', methods=["POST"])
def setSqlInfo():
    try:
        sqlInfo = request.get_json(force=True)
        rsCoreV2.setSqlInfo(sqlInfo)
        return jsonify(success=True)
    except:
        print_exc()
        return jsonify(success=False)



@app.route('/initializeRecoSys', methods=['POST'])
def initiate():
    try:
        rsCoreV2.initiate()
        return jsonify(success=True)
    except:
        print_exc()
        return jsonify(success=False)



@app.route('/getReco', methods=['POST'])
def getRecommend():
    try:
        userServices = request.get_json(force=True)
        r = rsCoreV2.getRecommend(userServices)
        return jsonify(r)
    except:
        print_exc()
        return jsonify(success=False)


###############################################################
@app.route('/test', methods=['GET'])
def testF():
    # data = request.get_json(force=True)
    return 'it\'s a good way to communcation'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = restPort)