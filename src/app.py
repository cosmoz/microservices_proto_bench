from flask import Flask
import requests
app = Flask(__name__)

@app.route("/")
def full():
    r = requests.get('http://localhost:4001/comment')
    body = "%s <br /> %s" % ("article, article..", r.text)
    return body

@app.route("/article")
def article():
    return "article, article.."

if __name__ == "__main__":
    app.run(port=4000)
