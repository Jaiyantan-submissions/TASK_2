from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import re

def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one digit.")
    if re.search(r'[@$!%*?&#]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")

    return {"strength": strength, "feedback": feedback}

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_password', methods=['POST'])
def check_password():
    data = request.get_json()
    password = data.get('password', '')
    result = check_password_strength(password)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

