from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__) #Refering the flask server to this archive
bootstrap = Bootstrap(app)
app.config["SECRET_KEY"]= 'CLAVE SECRETA' #Making encryption our cookie ip, utilizing python session 

items =["rice", "bread", "pupetter", "tomate" ]


class LoginForm(FlaskForm):
    username = StringField("User Name: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    submit = SubmitField("Send Data: ", validators=[DataRequired()])
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
    login_form = LoginForm()
    context = {
        "user_ip": user_ip,
        "items":items,
        "login_form":login_form
     }                                           #context=context           
    return render_template("ip_information.html", **context) 
app.run(host='0.0.0.0' , port=5000, debug='True') # Accesing from anywhere ip adress on our app on the port..
                                    #activate to show errors in development else not in productions