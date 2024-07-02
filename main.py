from flask import Flask

app = Flask(__name__) #Refering the server flask to this archive

@app.route("/")
def hello():
    return "Hello world"+{}

app.run(host='0.0.0.0' , port=5000, debug='True') # Accesing from anywhere adress ip on app on the port..
                                    #activate to show errors in development not in productions
