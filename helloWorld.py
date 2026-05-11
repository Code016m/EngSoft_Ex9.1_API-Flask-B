from flask import Flask, jsonify, request

app = Flask(__name__)

# Rota GET
@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Hello World!'})

# Rota POST
@app.route('/salutation', methods=['GET', 'POST'])
def salutation():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
    else:
        name = request.args.get('name', 'Guest')
    return jsonify({
        'message': 'Hello %s!' % name
    })

if __name__ == "__main__":
    app.run(debug=True)
