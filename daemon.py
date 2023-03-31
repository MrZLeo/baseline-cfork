from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello python!\n'

if __name__ == '__main__':
    # time that start serverless function
    startTime = int(round(time.time() * 1000))
    logf = open("log.txt", "w")
    logf.write(str(startTime))
    logf.close()

    app.run(host='0.0.0.0',port=int(8080))
