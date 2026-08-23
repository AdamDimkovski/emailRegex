from flask import Flask, render_template, request
import dns.resolver

import re

app = Flask(__name__)

@app.route('/')
def input():
    return render_template('index.html')

@app.route("/regex.py", methods=["GET", "POST"])
def regex():
    message = None
    result_gif = None

    if request.method == "POST":
        email = request.form.get("email")
        if email:
           email_pattern = r"^[a-zA-Z0-9]+([._%+-][a-zA-Z0-9]+)*[@][a-zA-Z0-9]+([-][a-zA-Z0-9]+)*([.][a-zA-Z]{2,})+$"
           if re.fullmatch(email_pattern, email):

                    # IF email format is valid, check to see if its on a blocklist
                   domain_to_check = email.partition('@')[2]
                   dbl_zone = "dbl.spamhaus.org"
                   query_target = f"{domain_to_check}.{dbl_zone}"
                   
                   try:
                        dns.resolver.resolve(query_target, "A")
                        
                        # This runs if the email is malicious 
                        message = None
                        result_gif = "hacker.gif"
                        
                   # This runs if the email is not on the dbl block list
                   except dns.resolver.NXDOMAIN:
                        message = f"Valid Email Alert! {email}"
                        result_gif = "success.gif"
                        
                   # This runs if there is an error checking domains
                   except Exception as e:
                        message = "Internal Error Whoopidy Doo Dah"
                        result_gif = "error.gif"
           else:
               message = "wrong format bud"
               result_gif = "failed.png" 
        else: 
            message = "Internal Error Whoopidy Doo Dah"
            result_gif = "error.gif"

        
    return render_template("index.html", message=message, result_gif=result_gif)

if __name__ == "__main__":
    app.run(debug=True)