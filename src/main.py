from flask import Flask
from flask.app import Flask as FlaskType

from counter import Counter
from flask import request

app: FlaskType = Flask(__name__)
    
db = Counter()

@app.route('/')
def index():
    return "Welcome to the Safe Counter App!"

@app.route('/counter/<name>', methods=['GET'])
def get_counter(name: str) -> dict[str, int | str]:
    return {"name": name, "value": db.read(name)}

@app.route('/counter', methods=['POST'])
def set_counter() -> dict[str, int | str]:
    # processing inputs
    data = request.get_json()
    name = data.get('name', 'default')
    x = data.get('increment', 1)

    # increment & response
    db.increment(name, x)
    return {"name": name, "value": db.read(name)}

def main():
    print("Starting the Safe Counter App...")
    app.run(debug=True, port=4000)

if __name__ == "__main__":
    main()
