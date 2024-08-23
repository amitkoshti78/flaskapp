import sys

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from dbconnect import db_connect

app = Flask(__name__)
CORS(app)


# Route to render the index.html page
@app.route('/')
def home():
    return render_template('index.html')


# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.json
    print(f"Received data: {data}")

    for key, value in data.items():
        match key:
            case 'payload':
                payload = value
            case _:
                return jsonify({"message": "Wrong data submitted"})

    print(f"Received data: {payload}")

    response_text = db_connect(payload)

    print(response_text)

    # You can process the data here (e.g., save to DB, perform some logic, etc.)

    return jsonify({"message": response_text})


if __name__ == '__main__':
    app.run(debug=True)
