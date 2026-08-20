from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def input():
    return render_template('index.html')

@app.route("/regex.py", methods=["GET", "POST"])
def regex():
    message = None
    if request.method == "POST":
        email = request.form.get("email")
        if email:
           email_pattern = r"^[a-zA-Z0-9]+([._%+-][a-zA-Z0-9]+)*[@][a-zA-Z0-9]+([-][a-zA-Z0-9]+)*([.][a-zA-Z]{2,})+$"
           if re.fullmatch(email_pattern, email):
                   message = f"You submitted: {email}"
           else:
               message = "wrong format bud"
        else:
            message = "Internal Error Whoopidy Doo Dah"
        
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)