from flask import Flask, jsonify, make_response, request
from flask_cors import CORS
import db_connection as db

app = Flask(__name__)
CORS(app)

# db = [{"name":"run","age": 14}, {"name":"abc", "age": 12}]

# @app.route("/api", methods=["GET"])
# def hello():
#     args = request.args
#     name = args.get('name')
#     found = False
#     data = {}
#     for d in db :
#         if d['name'] == name :
#             found = True
#             data = d
#             break

#     if found == False :
#         return make_response("Not found", 404)

#     return make_response(data, 200)

# @app.route("/api", methods=["POST"])
# def hello2():
#     args = request.get_json(force=True)
#     print(args)
#     data = {"name" : args["name"]}
#     return make_response(data, 200)

user = db.UserRepo()

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json(force=True)
    r = user.findByUsername(data['username'])
    if r != None :
        return make_response(jsonify("username was taken"), 400)

    r = user.insertOne(data)
    if r == None :
        return make_response(jsonify("insert fail"), 400)
    
    return make_response(jsonify("reister successful"), 200)

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(force=True)
    r = user.findByUsernameAndPassword(data['username'], data['password'])
    if r == None:
        r = user.findByUsername(data['username'])
        if r == None:
            return make_response(jsonify("not found"), 404)

        return make_response(jsonify("wrong password"), 400)
    
    return make_response(jsonify("login success"), 200)

if __name__ == "__main__" :
    app.run(port=8080, debug=True)