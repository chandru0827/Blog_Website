from flask import Flask, request, jsonify
from tinydb import TinyDB, Query
from flask_cors import CORS
from uuid import uuid4

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

db = TinyDB("db.json")

posts = db.table("posts")


@app.route("/addPost", methods=["POST"])
def index():
    data = request.get_json()
    data["id"] = str(uuid4())
    posts.insert(data)
    return jsonify(data)


@app.route("/getPosts", methods=["GET"])
def getPosts():
    return jsonify(posts.all())


@app.route("/getPost/<id>", methods=["GET"])
def getPost(id):
    post = Query()
    return str(posts.search(post.id == request.args.get("id")))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
