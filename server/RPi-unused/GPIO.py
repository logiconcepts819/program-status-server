from threading import Condition, Thread
import copy
import sys

BOARD = 0
BCM = 1
OUT = 2

class GPIOEmulation:
    def __init__(self):
        self.cv = Condition()
        self.output_gpios = [False]*15
        self.gpios = [False]*15
        self.gpio_change = False
        self.exiting = False
        self.thread = Thread(target=self.printing_thread)
        self.thread.daemon = True
        sys.stdout.write('\n')
    
    def setup_gpio(self, gpio_id, operation):
        self.cv.acquire()
        self.output_gpios[gpio_id] = (operation == OUT)
        if operation != OUT:
            self.gpios[gpio_id] = False
            self.cv.notifyAll()
        self.cv.release()
    
    def set_output(self, gpio_id, active):
        self.cv.acquire()
        if self.output_gpios[gpio_id]:
            self.gpios[gpio_id] = active
            self.gpio_change = True
            self.cv.notifyAll()
        self.cv.release()
    
    def start_thread(self):
        self.thread.start()
    
    def stop_thread(self):
        self.cv.acquire()
        self.exiting = True
        self.cv.notifyAll()
        self.cv.release()
        self.thread.join()
    
    def printing_thread(self):
        gpio_change = True
        while gpio_change:
            self.cv.acquire()
            while not self.gpio_change and not self.exiting:
                self.cv.wait()
            gpio_change = self.gpio_change
            gpios = copy.deepcopy(self.gpios)
            self.gpio_change = False
            self.cv.release()
            
            if gpio_change:
                sys.stdout.write('\033[A\033[K')
                for gpio_active in gpios:
                    sys.stdout.write('X' if gpio_active else ' ')
                sys.stdout.write('\n')

emulator = GPIOEmulation()
def emulator_init():
    emulator.start_thread()
def emulator_fini():
    emulator.stop_thread()

def setmode(the_mode):
    pass

def setup(gpio_id, operation):
    emulator.setup_gpio(gpio_id, operation)

def output(gpio_id, active):
    emulator.set_output(gpio_id, active)

def cleanup():
    pass