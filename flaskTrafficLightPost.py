from flask import Flask
from flask import request
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#leds setup
redLed = 26
greenLed = 13
GPIO.setup(redLed, GPIO.OUT)
GPIO.setup(greenLed, GPIO.OUT)

#instance flask class
app = Flask(__name__)

#define urls and methods
@app.route('/trafficlight', methods = ["POST"])
def changeTrafficLightColor():
    print(request.data)
    json = request.get_json()
    color = json.get('color')
    print(color)
    if color == 'red':
        GPIO.output(redLed, True)
        GPIO.output(greenLed, False)
    if color == 'green':
        GPIO.output(redLed, False)
        GPIO.output(greenLed, True)        
    return 'Changed light!'

@app.route('/red')
def redLight():
    GPIO.output(redLed, True)
    GPIO.output(greenLed, False)
    return 'Red!'

@app.route('/green')
def greenLight():
    GPIO.output(redLed, False)
    GPIO.output(greenLed, True)
    return 'Green!'

@app.route('/clear')
def allLightsOff():
    GPIO.output(redLed, False)
    GPIO.output(greenLed, False)
    return 'all off!'

#start server.
app.run(host='192.168.1.31', port=8090)
#app.run(host='127.0.0.1', port=8090) = loopback address

