#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# 1. Index Route
@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


# 2. Print String Route
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter  # Remove <p> tags

# 3. Count Route
@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = [str(i) for i in range(parameter)]
    return '\n'.join(numbers) + '\n'


# 4. Math Operation Route
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return "Error: Division by zero!"
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Error: Unsupported operation."

    return str(result)  # Return only the result as plain text

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
