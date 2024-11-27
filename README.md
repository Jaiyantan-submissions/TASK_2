
# Password Strength Checker

This is a web application built using **Flask** to check the strength of a password based on various criteria such as length, uppercase and lowercase letters, digits, and special characters.

## Features
- Check password strength (Weak, Moderate, Strong)
- Provides feedback on password improvements
- Built using Flask, HTML, CSS, and JavaScript

## Technologies Used
- **Backend**: Flask, Python
- **Frontend**: HTML, CSS, JavaScript
- **Libraries**: Flask-CORS, Regular Expressions

## Setup Instructions

### 1. Clone the repository
```bash
git clone <repository_url>
cd password-strength-checker
```

### 2. Create a virtual environment (optional but recommended)
#### For Windows:
```bash
python -m venv venv
.env\Scriptsctivate
```

#### For macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install the dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Flask app
```bash
python app.py
```

### 5. Access the app
Once the server is running, open a browser and go to `http://127.0.0.1:5000/` to use the Password Strength Checker.

## File Structure
```
password-strength-checker/
│
├── app.py                  # Flask backend application
├── templates/              # Directory for HTML templates
│   └── index.html          # Main HTML page for the user interface
│
├── static/                 # Directory for static files (CSS, JS)
│   ├── styles.css          # CSS styles
│   └── script.js           # JavaScript for handling form submission and displaying results
│
└── requirements.txt        # Python dependencies (Flask, Flask-CORS)
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
