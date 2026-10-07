# Secure Pass: Password Strength Checker

A Flask web app that scores a password out of 24, gives a rating, and suggests how to improve it.

**Live demo:** https://jg1311878.pythonanywhere.com/

## Features
- Scores passwords out of 24 based on:
  - length
  - character mix
  - variety of special characters
  - keyboard patterns (e.g. "qwerty")
  - predictable years
  - a list of 10,000 common passwords
- Returns a rating and tailored improvement tips
- Checks whether the password appears in known data breaches using the Have I Been Pwned API
- Per-IP rate limiting (50 requests per hour) using Flask-Limiter

## Privacy
The breach check uses k-anonymity: only the first 5 characters of the password's hash are sent to the Have I Been Pwned API. Neither the password nor its full hash leaves the app.

## Tech
Python, Flask, Flask-Limiter, Have I Been Pwned API, deployed on PythonAnywhere.

## Run locally
```
pip install flask flask-limiter requests
python app.py
```
Then open http://127.0.0.1:5000 in your browser. (Change `app.py` to your main file's name if it differs.)

## Possible improvements
- Train a machine learning model on leaked-password data and compare it with the rule-based scoring
- Add automated tests
