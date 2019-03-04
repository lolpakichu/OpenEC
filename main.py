# imports
from flask import Flask, render_template
import secrets

app = Flask(__name__)

# Home Page
@app.route("/")
def index():
    return render_template('index.html')

# API
@app.route("/<string:encode_string>")
def api(encode_string):
    encode_string = encode_string.encode('utf-8')
    encoded_string = encode_string.hex()
    return encoded_string
# run app
if __name__ == "__main__":
    app.run(debug=True)