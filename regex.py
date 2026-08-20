from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def input():
    return render_template('index.html')

@app.route("/regex.py", methods=["GET", "POST"])
def regex():

    email = request.form.get("email")
    return f"You submitted: {email}"

if __name__ == "__main__":
    app.run(debug=True)