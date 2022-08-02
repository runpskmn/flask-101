from flask import Flask, make_response, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

db = [{"name":"run","age": 14}, {"name":"abc", "age": 12}]

@app.route("/api", methods=["GET"])
def hello():
    args = request.args
    name = args.get('name')
    found = False
    data = {}
    for d in db :
        if d['name'] == name :
            found = True
            data = d
            break

    if found == False :
        return make_response("Not found", 404)

    return make_response(data, 200)

@app.route("/api", methods=["POST"])
def hello2():
    args = request.get_json(force=True)
    print(args)
    data = {"name" : args["name"]}
    return make_response(data, 200)

print("Hello")
if __name__ == "__main__" :
    app.run(port=8080, debug=True)

