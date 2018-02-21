import RPi.GPIO as GPIO
import time
import os
import inspect

'''Requires a camera module to be connected and the input from PIR sensor.
Output to LED is an option but supported.

Default input pin: 11
Default output pin: 12'''

default_log_file = '/home/pi/CHIPstuff/VenusFly/flypaper.log'
PIC_PATH = '/home/pi/CHIPstuff/VenusFly/static/pics'
VID_PATH = '/home/pi/CHIPstuff/VenusFly/static/vids'
DEFAULT_VIDEO_TIMEOUT = 15 #seconds
IP='192.168.0.73'
PORT=5000



def setup_step(input, output=None):
    GPIO.setwarnings(False)
    # setup GPIO pins as seen on board
    GPIO.setmode(GPIO.BOARD)

    # optionally set up output pin
    GPIO.setup(input, GPIO.IN)
    if (output is not None):
        GPIO.setup(output, GPIO.OUT)


def execute(cmd):
    # can be replaced with subprocess or other
    log(cmd)
    os.system(cmd)


def log(msg, log_file=default_log_file):
    final_msg = "{0}: VenusFly : {1} : {2}\n"\
                .format(time.ctime(), inspect.stack()[1][3], msg)

    with open(log_file, 'a') as f:
        f.write(final_msg)
    print(final_msg)


def unlog(log_file=default_log_file):
    log = ""
    with open(log_file, 'r') as f:
        log = f.read()
    return log


def check_input(input):
    if (GPIO.input(input) == 1):
        return 1
    else:
        return 0


def send_out(signal, output=None):
    if output is not None:
        GPIO.output(output, signal)
        if signal == 1:
            # principle action when detected
            name = take_pic()
            if name is not None:
                log('{0} file created!'.format(name))
    else:
        log(signal)


def take_video(video_name=None, timeout=None):
    if video_name is None:
        video_name = str(time.time()) + '.mp4'

    if timeout is None:
        # timeout in milliseconds
        timeout = DEFAULT_VIDEO_TIMEOUT * 1000

    cmd = 'mkdir -p {1}; raspivid -n -t {0} -o {1}/{2}' \
          .format(timeout,VID_PATH, video_name)
    execute(cmd)
    return video_name


def take_pic(pic_name=None):
    if pic_name is None:
        pic_name = str(time.time()) + '.jpg'

    cmd = 'mkdir -p {0}; raspistill -n -t 3000 -o {0}/{1}'.format(PIC_PATH, pic_name)
    execute(cmd)
    return pic_name


def start_system(input, output=None, wait=None):
    if wait is None:
        wait = 0.01

    while True:
        # check true then wait and check again to confirm detection
        time.sleep(wait)
        if (check_input(input) == 1):
            time.sleep(1)
            if (check_input(input) == 1):
                send_out(1, output)
        else:
            send_out(0, output)


if __name__ == '__main__':
    inPin = 11
    outPin = 12
    wait = 0.01

    # provide outPin only if LED output required
    setup_step(inPin, outPin)
    start_system(inPin, outPin, wait=wait)
