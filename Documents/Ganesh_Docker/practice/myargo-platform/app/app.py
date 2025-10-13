from flask import Flask
app = Flask(__name__)

@app.get("/")
def hello():
    return "Hello from CI → CD via Argo CD! 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

