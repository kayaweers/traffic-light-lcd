import RPi.GPIO as GPIO
import time as time
from RPLCD import CharLCD

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

button = 6
buttonCount = 0
redLed = 26
yellowLed = 19
greenLed = 13

lcd = CharLCD(numbering_mode=GPIO.BCM, cols=16, rows=2, pin_rs=22, pin_e=27, pins_data=[2,3,4,17])

GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(redLed, GPIO.OUT)
GPIO.setup(yellowLed, GPIO.OUT)
GPIO.setup(greenLed, GPIO.OUT)

def updateLcd(buttonCount):
    print("clicked: ", buttonCount)
    lcd.write_string(u"click number: " + str(buttonCount))
    return

def updateLedsToGreen():
    turnLedOff(redLed)
    turnLedOn(greenLed)
    return

def updateLedsToRed():
    turnLedOff(greenLed)
    turnLedOn(yellowLed)
    time.sleep(2)
    turnLedOff(yellowLed)
    turnLedOn(redLed)
    return

def turnLedOn(led):
    GPIO.output(led, True)
    return

def turnLedOff(led):
    GPIO.output(led, False)
    return

lcd.clear()
lcd.write_string('Please press!')

turnLedOn(redLed)
turnLedOff(yellowLed)
turnLedOff(greenLed)


while (buttonCount < 3):
    if GPIO.input(button) == False:
        lcd.clear()
        buttonCount +=1
        updateLcd(buttonCount)
        time.sleep(2)
        updateLedsToGreen()
        time.sleep(1)
        lcd.clear()
        time.sleep(3)
        updateLedsToRed()

time.sleep(1)
lcd.write_string('Done')
lcd.clear()

GPIO.cleanup()




    

