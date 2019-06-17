
from flask import Flask
import os


app = Flask(__name__)

port = int(os.getenv("PORT", 9009))

@app.route('/')
def hello_world():
    liste = []
    t = 0
    while t < 10:
        liste.append("coucou"+str(t+1))
        t=t+1

    return str(liste)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)


