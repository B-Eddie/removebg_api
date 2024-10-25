from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/strings', methods=['GET'])
def get_strings():
    strings = ["apple", "banana", "cherry", "date", "elderberry"]
    return jsonify(strings)

if __name__ == '__main__':
    app.run()
