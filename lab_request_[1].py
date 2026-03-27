from flask import Flask, request, jsonify
import random

app = Flask(__name__)


# GET
@app.route('/number/', methods=['GET'])
def get_number():
    param = request.args.get('param')
    random_num = random.randint(1, 100)
    result = random_num * float(param)
    operation = random.choice(["sum", "sub", "mul", "div"])
    return jsonify({
        "result": result,
        "operation": operation,
        "random_number": random_num 
    })

# POST
@app.route('/number/', methods=['POST'])
def post_number():
    data = request.get_json()
    random_num = random.randint(1, 100)
    operation = random.choice(["sum", "sub", "mul", "div"])
    result = random_num * data['jsonParam']
    return jsonify({
        "result": result,
        "operation": operation,
        "random_number": random_num  
    })

# DELETE
@app.route('/number/', methods=['DELETE'])
def delete_number():
    random_num = random.randint(1, 100)
    operation = random.choice(["sum", "sub", "mul", "div"])
    return jsonify({
        "number": random_num,
        "operation": operation,
        "random_number": random_num 
    })

if __name__ == '__main__':
    app.run()