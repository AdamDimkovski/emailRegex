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
                   message = f"Valid Email Alert! {email}"
                   result_gif = "success.gif"
           else:
               message = "wrong format bud"
               result_gif = "failed.png" 
        else: 
            message = "Internal Error Whoopidy Doo Dah"
            result_gif = "error.gif"
        
    return render_template("index.html", message=message, result_gif=result_gif)

if __name__ == "__main__":
    app.run(debug=True)