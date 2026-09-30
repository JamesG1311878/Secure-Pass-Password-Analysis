from flask import Flask, render_template, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from Checks import Strength_calc

app = Flask(__name__)

limiter = Limiter(
    get_key_func=get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"] 
)

@app.route("/", methods=["GET", "POST"])
def home():
    label = None
    score = None
    tips = []

    if request.method == "POST":
        password = request.form["password"]
        result = Strength_calc(password)
        label = result["label"]
        score = result["score"]
        tips = result["tips"]

    return render_template(
        "index.html",
        label=label,
        score=score,
        tips=tips
    )

if __name__ == '__main__':
    app.run(debug=True)