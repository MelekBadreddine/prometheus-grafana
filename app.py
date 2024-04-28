from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_number', methods=['POST'])
def generate_number():
    min_value = int(request.form['min_value'])
    max_value = int(request.form['max_value'])
    random_number = random.randint(min_value, max_value)
    return str(random_number)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
