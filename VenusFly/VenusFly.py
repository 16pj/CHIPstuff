import RPi.GPIO as GPIO
import time

'''Requires a camera module to be connected and the input from pir sensor.
Output to led is option but supported.

Default input pin: 11
Default output pin: 12'''



def setup_step(input, output=None):
	GPIO.setwarnings(False)

	# setup GPIO pins as seen on board
	GPIO.setmode(GPIO.BOARD)

	# optionally set up output pin
	GPIO.setup(input, GPIO.IN)
	if (output is not None):
		GPIO.setup(output, GPIO.OUT)

def check_input(input):
        if (GPIO.input(input) == 1):
                return 1
        else:
                return 0

def send_out(signal, output=None):
	if output is not None:
		GPIO.output(output, signal)
	else:
		print(signal)


def start_system(input,output=None, wait=None):
	if wait is None:
		wait = 0.01

	while True:
                time.sleep(wait)
                if (check_input(input) == 1):
                        send_out(1, output)
                else:
                        send_out(0, output)


if __name__ == '__main__':
	inPin = 11
	outPin = 12
	wait = 0.01

	setup_step(inPin, outPin)
	start_system(inPin, outPin, wait=wait)
