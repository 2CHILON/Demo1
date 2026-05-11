from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! \n First program using codespaces and vcs github "                   

@app.route("/new")
def new():
    return "Endpoint number 2: Testing CI pipeline"            

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
