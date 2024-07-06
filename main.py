from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__) #Refering the flask server to this archive

items =["rice", "bread", "pupetter", "tomate" ]
@app.route("/inde")
def index():              #Request object for obtaining all client information  
    user_ip_information = request.remote_addr
    response = make_response(redirect("/show_information_address"))
    response.set_cookie("user_ip_information", user_ip_information)
    return response

@app.route("/show_information_address")
def show_information():
    user_ip = request.cookies.get("user_ip_information")
    context = {
        "user_ip": user_ip,
        "items":items
     }                                           #context=context           
    return render_template("ip_information.html", **context) 

app.run(host='0.0.0.0' , port=5000, debug='True') # Accesing from anywhere adress ip on app on the port..
                                    #activate to show errors in development else not in productions

