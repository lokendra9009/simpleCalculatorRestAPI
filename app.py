from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


def checkPostedData(postedData: dict, functionName: str) -> int:
    """[Function checks for the whether the postedData is valid for not]
    
    Arguments:
        postedData {dict} -- [description]
        functionName {str} -- [description]
    
    Returns:
        int -- [description]
    """        
    if functionName == "add" or functionName == "substract" or functionName == "multiply":
        if 'x' not in postedData or 'y' not in postedData:
            return 301
        else:
            return 200
    
    elif functionName == 'divide':
        if 'x' not in postedData or 'y' not in postedData:
            return 301
        elif postedData['y']==0:
            return 302
        else:
            return 200



class Add(Resource):
    def post(self) -> dict:
        """[summary]
        
        Arguments:
            Resource {[type]} -- [description]
        
        Returns:
            dict -- [Returns a JSON object with two key value pair - 'Message' and 'Status Code']
        """        
        postedData = request.get_json()
        status_code = checkPostedData(postedData, "add")
        

        if (status_code != 200):
            retJson = {
                'Message': "An error has occured",
                'Status Code': status_code
            }
            return jsonify(retJson)

        x = postedData['x']
        y = postedData['y']

        x = int(x)
        y = int(y)

        res = x+y

        retMap = {
            'Message': res,
            'Status Code': 200
        }
        return jsonify(retMap)


class Subtract(Resource):
    def post(self):
        postedData = request.get_json()
        status_code = checkPostedData(postedData, "substract")
        

        if (status_code != 200):
            retJson = {
                'Message': "An error has occured",
                'Status Code': status_code
            }
            return jsonify(retJson)

        x = postedData['x']
        y = postedData['y']

        x = int(x)
        y = int(y)

        res = x-y

        retMap = {
            'Message': res,
            'Status Code': 200
        }
        return jsonify(retMap)


class Multiply(Resource):
    def post(self):
        postedData = request.get_json()
        status_code = checkPostedData(postedData, "multiply")
        

        if (status_code != 200):
            retJson = {
                'Message': "An error has occured",
                'Status Code': status_code
            }
            return jsonify(retJson)

        x = postedData['x']
        y = postedData['y']

        x = int(x)
        y = int(y)

        res = x*y

        retMap = {
            'Message': res,
            'Status Code': 200
        }
        return jsonify(retMap)


class Divide(Resource):
    def post(self):
        postedData = request.get_json()
        status_code = checkPostedData(postedData, "divide")
        

        if (status_code != 200):
            retJson = {
                'Message': "An error has occured",
                'Status Code': status_code
            }
            return jsonify(retJson)

        x = postedData['x']
        y = postedData['y']

        x = int(x)
        y = int(y)

        res = x/y

        retMap = {
            'Message': res,
            'Status Code': 200
        }
        return jsonify(retMap)


api.add_resource(Add, "/add")
api.add_resource(Subtract, "/substract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/divide")


@app.route('/')
def hello():
    return 'Hello World!'

# if __name__ == "__main__":
#     app.debug = True
#     app.run(host="127.0.0.1", port=5000)
