from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
import unittest
from app import create_app
from app.forms import LoginForm
app = create_app()


items =["rice", "bread", "pupetter", "tomate" ]


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found_endpoint(error):
    return render_template('404.html', error=error)

@app.route("/inde")
def index():              #Request object for obtaining all client information  
    user_ip_information = request.remote_addr
    response = make_response(redirect("/show_information_address"))
   #response.set_cookie("user_ip_information", user_ip_information)
    session["user_ip_information"] = user_ip_information   #Encrypted
    return response

@app.route("/show_information_address")
def show_information():
   #user_ip = request.cookies.get("user_ip_information") 
    user_ip = session.get("user_ip_information")
    username = session.get("username")

    context = {
        "user_ip": user_ip,
        "items":items,
        "username": username
     }                                       #context=context 
    return render_template("ip_information.html", **context) 

if __name__== "__main__":
    app.run(host='0.0.0.0' , port=5000, debug='True') # Accesing from anywhere ip adress on our app on the port..
                                    #activate to show errors in development else not in productions