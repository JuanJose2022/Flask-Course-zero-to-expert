from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap                                     
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import unittest

app = Flask(__name__) #Refering the flask server to this archive
bootstrap = Bootstrap(app)
app.config["SECRET_KEY"]= 'CLAVE SECRETA' #Making encryption our cookie ip, utilizing python session 

items =["rice", "bread", "pupetter", "tomate" ]


class LoginForm(FlaskForm):
    username = StringField("User Name: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    submit = SubmitField("Send Data: ")


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

@app.route("/show_information_address", methods=["GET", "POST"])
def show_information():
   #user_ip = request.cookies.get("user_ip_information") 
    user_ip = session.get("user_ip_information")
    username = session.get("username")

    login_form = LoginForm()
    context = {
        "user_ip": user_ip,
        "items":items,
        "login_form":login_form,
        "username": username
     }
    if login_form.validate_on_submit():
        username = login_form.username.data
        session["username"] = username            
        flash("User Name logged well") #Sending messages in Flask 
        #return make_response(redirect("/inde"))
        return redirect(url_for("index")) #url_for: To clean and update the screen 
                                     #context=context           
    return render_template("ip_information.html", **context) 

if __name__== "__main__":
    app.run(host='0.0.0.0' , port=5000, debug='True') # Accesing from anywhere ip adress on our app on the port..
                                    #activate to show errors in development else not in productions