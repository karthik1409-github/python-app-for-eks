from flask import Flask
import socket

app = Flask(__name__)

#for demo purposes only to see different requests handled by instances of the application
count = 0

@app.route('/')
def index():
    output = "<h2>This is a Python web app deployed on Amazon EKS</h2>"
    output = output + "<h3>Host name: " +socket.gethostname() +"</h3>"

    return output
    #return 'Goodbye from application ' + str(count)

if __name__ == '__main__':
    app.run(host='0.0.0.0')