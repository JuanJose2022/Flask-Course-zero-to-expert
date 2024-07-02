from flask import Flask, request

app = Flask(__name__) #Refering the server flask to this archive

@app.route("/")
def hello():              #Request object for pbtaining all client information  
    user_ip_information = request.remote_addr
    return f"Hows you doing, Your IP adress is: {user_ip_information}"

app.run(host='0.0.0.0' , port=5000, debug='True') # Accesing from anywhere adress ip on app on the port..
                                    #activate to show errors in development not in productions
