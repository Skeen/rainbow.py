#!/usr/bin/python
import mraa
import time

redPin = 20;
greenPin = 19;
bluePin = 18;

def setup():
    setColourRgb(0,0,0);

def loop():

    rgbColour=[1,0,0]
    for decColour in range(0, 3):
        incColour = 0 if (decColour == 2) else decColour + 1;

	for i in range(0, 100):
            rgbColour[decColour] -= 0.01;
            rgbColour[incColour] += 0.01;

            setColourRgb(rgbColour[0], rgbColour[1], rgbColour[2]);
            time.sleep(0.01);

LED_R = None
LED_G = None
LED_B = None

# Setup the GPIOs for output
def setup_led():
    global LED_R, LED_G, LED_B

    LED_R = mraa.Pwm(20);
    LED_R.enable(True);
    LED_G = mraa.Pwm(19);
    LED_G.enable(True);
    LED_B = mraa.Pwm(18);
    LED_B.enable(True);

# Set the color of the leds
def setColourRgb(red, green, blue):
    global LED_R, LED_G, LED_B

    print("R:" + str(red) + ", G:" + str(green) + ", B:" + str(blue));

    LED_R.write(red);
    LED_G.write(green);
    LED_B.write(blue);

setup_led();
while True:
    loop();
