import sys
from flask import Flask, render_template, request
import signal
import threading

from Adafruit_MotorHAT import Adafruit_MotorHAT
 
import time
import atexit

import Adafruit_PCA9685

app = Flask(__name__)

mh = Adafruit_MotorHAT(addr=0x60)
Motor1 = mh.getMotor(1)
Motor2 = mh.getMotor(2)

@app.route("/motor_forward", methods=["POST"])
def motor_forward():
    if "POST" == request.method:
        t = threading.Thread(target=forward_action, args=(request.form['LR'], request.form['speed'],))
        t.start()
            
    return ""

def forward_action(LR, speed):
    if LR == "0": 
        Motor1.run(Adafruit_MotorHAT.FORWARD)
        Motor1.setSpeed(int(speed))
    elif LR == "1":
        Motor2.run(Adafruit_MotorHAT.FORWARD)
        Motor2.setSpeed(int(speed))
        
@app.route("/motor_back", methods=["POST"])
def motor_back():
    if "POST" == request.method:
        LR = request.form['LR']
        speed = request.form['speed']

        if LR == "0": 
            Motor1.run(Adafruit_MotorHAT.BACKWARD)
            Motor1.setSpeed(int(speed))
        elif LR == "1":
            Motor2.run(Adafruit_MotorHAT.BACKWARD)
            Motor2.setSpeed(int(speed))

    return ""

@app.route("/motor_stop", methods=["POST"])
def motor_stop():

    if "POST" == request.method:
        t = threading.Thread(target=stop_action, args=(request.form['LR'],))
        t.start()
    return ""

def stop_action(LR):
    if LR == "0": 
        Motor1.run(Adafruit_MotorHAT.RELEASE)
        print("0 stop")
    elif LR == "1":
        Motor2.run(Adafruit_MotorHAT.RELEASE)
        print("1 stop")
                             
@app.route("/")
def index():
    return render_template("index.html")


def sigint_handler(signal, frame):
    """
    the exit for [Ctrl+C]
    """
    app.logger.debug("Closing")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, sigint_handler)    
    app.run("0.0.0.0", debug=True)

