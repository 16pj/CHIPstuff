from flask import Flask
import VenusFly as fly
import threading
import time

app = Flask(__name__)

inPin = 11
outPin = 12
wait = 0.01
lock = 'unlocked'

# provide outPin only if LED output required
fly.setup_step(inPin, outPin)


exitFlag = 0


class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.inPin = inPin
        self.outPin = outPin
        self.wait = wait

    def run(self):
        fly.log("Unholstering " + self.name)
        fireitup(self.name, self.inPin, self.outPin, self.wait)
        fly.log("Holstering  " + self.name)


def fireitup(threadName, inPin, output=None, wait=None):

    global exitFlag
    exitFlag = 0
    global lock

    if wait is None:
        wait = 0.01
    if lock == 'locked':
        exit()

    fly.log('Firing Engines up!')

    while True:
        lock = 'locked'
        if exitFlag:
            fly.send_out(0, output)
            lock = 'unlocked'
            exit()
        # check true then wait and check again to confirm detection
        time.sleep(wait)
        if (fly.check_input(inPin) == 1):
            time.sleep(1)
            if (fly.check_input(inPin) == 1):
                fly.send_out(1, output)
        else:
            fly.send_out(0, output)

    return


def start_system():
    fly.log('Starting VenusFly system')

    # Create new threads
    thread1 = myThread(1, "Thread-1", 1)
    thread1.start()
    return True


def stop_system():
    fly.log('Stopping VenusFly system')
    global exitFlag
    exitFlag = 1
    return True


@app.route("/")
def welcome():
    return "Welcome to VenusFly!"


@app.route("/start")
def start():
    if start_system():
        return "Started System"
    else:
        return "Something went wrong starting!"


@app.route("/stop")
def stop():
    if stop_system():
        return "Stopped system"
    else:
        return "Something went wrong stopping!"


@app.route("/click")
def click():
    global lock
    startFlag = False
    if lock == 'locked':
        startFlag = True
        lock == 'unlocked'
    stop_system()
    name = fly.take_pic()
    fly.log('pic {0} taken'.format(name))
    if startFlag is True:
        start_system()
    return "Picture Taken!"


@app.route("/record")
def video():
    global lock
    startFlag = False
    if lock == 'locked':
        startFlag = True
        lock == 'unlocked'
    stop_system()
    name = fly.take_video()
    fly.log('video {0} taken'.format(name))
    if startFlag is True:
        start_system()
    return "Video Recorded!"


@app.route("/status")
def status():
    global lock
    if lock == 'locked':
            return "System is Fired Up"
    else:
        return "System is not Fired Up"


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
