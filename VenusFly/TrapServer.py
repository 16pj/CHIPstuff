from flask import Flask
import VenusFly as fly
import threading
import time

app = Flask(__name__)

inPin = 11
outPin = 12
wait = 0.01

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
        print "Starting " + self.name
        start_system(self.name, self.inPin, self.outPin, self.wait)
        print "Exiting " + self.name


@app.route("/")
def welcome():
    return "Welcome to VenusFly!"


def start_system(threadName, input, output=None, wait=None):
    global exitFlag
    exitFlag = 0

    if wait is None:
        wait = 0.01

    while True:
        if exitFlag:
            fly.send_out(0, output)
            exit()
        # check true then wait and check again to confirm detection
        time.sleep(wait)
        if (fly.check_input(input) == 1):
            time.sleep(1)
            if (fly.check_input(input) == 1):
                fly.send_out(1, output)
        else:
            fly.send_out(0, output)

    return


@app.route("/start")
def start():

    fly.log('starting VenusFly system')

    # Create new threads
    thread1 = myThread(1, "Thread-1", 1)
    thread1.start()
    return "Started System"


@app.route("/stop")
def stop_system():
    global exitFlag
    exitFlag = 1
    return "stopped system"


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
