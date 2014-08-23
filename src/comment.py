from flask import Flask
app = Flask(__name__)

@app.route("/comment")
def comment():
    return "comments, comments.."

if __name__ == "__main__":
    app.run(port=4001)
