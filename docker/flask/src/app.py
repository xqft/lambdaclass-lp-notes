from flask import Flask

app = Flask(__name__)
port = 3000

@app.route("/")
def main():
    return "Hello world"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
