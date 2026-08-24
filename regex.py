# Regex.py: a flask file which connects backend to frontend, created by Adam Dimkovski [24/08/2026]
# Imports used in backend
from flask import Flask, render_template, request
import dns.resolver

import re

app = Flask(__name__)

# App route connecting index.html to regex.py
@app.route('/')
def input():
    return render_template('index.html')

# App route allowing for Get and Post Request
@app.route("/regex.py", methods=["GET", "POST"])

# Method which runs when textfield is submitted
def regex():
    
    # Declares both variables as nothing to prevent overlap
    message = None
    result_gif = None

    # Checks for Post request
    if request.method == "POST":
        
        # Collects email from textfield
        email = request.form.get("email")
        
        # When Email is collected
        if email:
            
           # Email format regex
           email_pattern = r"^[a-zA-Z0-9]+([._%+-][a-zA-Z0-9]+)*[@][a-zA-Z0-9]+([-][a-zA-Z0-9]+)*([.][a-zA-Z]{2,})+$"
           
           # Match email if format is followed
           if re.fullmatch(email_pattern, email):

                   # If email format is valid, check to see if its on a blocklist
                   domain_to_check = email.partition('@')[2]
                   dbl_zone = "dbl.spamhaus.org"
                   query_target = f"{domain_to_check}.{dbl_zone}"
                   
                   try:
                        blocklist_response = dns.resolver.resolve(query_target, "A")
                        blocklist_codes = {
                            f"127.0.1.{code}" for code in range(2, 12)
                        }

                        if any(address.to_text().rstrip(".") in blocklist_codes for address in blocklist_response):
                            # This runs if the email is malicious
                            message = "Warning: this email domain is on the phishing blocklist."
                            result_gif = "hacker.gif"
                        else:
                            # A DNS answer outside Spamhaus's DBL codes is not a listing.
                            message = f"Valid Email Alert! {email}"
                            result_gif = "success.gif"
                        
                   # This runs if the email is not on the dbl block list
                   except dns.resolver.NXDOMAIN:
                        message = f"Valid Email Alert! {email}"
                        result_gif = "success.gif"
                        
                   # This runs if there is an error checking domains
                   except Exception as e:
                        message = "Internal Error Whoopidy Doo Dah"
                        result_gif = "error.gif"
                        
           # This runs if the email format is incorrect             
           else:
               message = "wrong format bud"
               result_gif = "failed.png" 
               
        # This runs if there is an internal error      
        else: 
            message = "Internal Error Whoopidy Doo Dah"
            result_gif = "error.gif"

    # Returns index.html after reload with correctly passed html request    
    return render_template("index.html", message=message, result_gif=result_gif)

if __name__ == "__main__":
    app.run(debug=True)