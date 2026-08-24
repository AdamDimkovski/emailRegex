# emailRegex
A interface created to practice regex, added textfield which can return 4 cases:
- success: Email is formatted correctly and DNS is not on blocklist
- failure: Email is not formatted correctly, is not checked for blocklist
- hacker: Email is formatted correctly but is on a phising blocklist
- Error: internal Error prevents code from running correctly

Use case examples for each case:
- success: abc-d@mail.com, abc.def@mail.com, abc@mail.com, abc_def@mail.com
- failure: abc-@mail.com, abc..def@mail.com, .abc@mail.com, abc#def@mail.com
- hacker: test@dbltest.com
- Error: This is hard to test, however if you want to test it, disconnect your 
local machine from internet, and try to submit a valid email format. This will 
cause DNS issues and trigger error.

Utilises; 
Python (dns.resolver, flask, regex), 
Html (index.html), 
Css (index.css), 
Javascript (index.html)

Created by Adam Dimkovski [24/08/2026]