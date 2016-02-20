import RPi.GPIO as GPIO
from threading import Condition, Thread
from __init__ import MIN_LED_FREQ, MAX_LED_FREQ

class LEDMode:
    Off = -1
    Success = -2
    Error = -4

class LEDController:
    def __init__(self, gpio_ids):
        GPIO.setup(gpio_ids[0], GPIO.OUT)
        GPIO.setup(gpio_ids[1], GPIO.OUT)

        self.gpio_ids = gpio_ids
        self.status = LEDMode.Off
        self.unique_status = LEDMode.Off
        self.have_new_status = True
        self.exiting = False
        self.cv = Condition()
        self.led_thread_inst = Thread(target=self.led_thread)
        self.led_thread_inst.daemon = True
        self.led_thread_inst.start()

        self.button_thread_inst = None
        if len(gpio_ids) > 2:
            GPIO.setup(gpio_ids[2], GPIO.IN)
            self.button_thread_inst = Thread(target=self.button_thread)
            self.button_thread_inst.daemon = True
            self.button_thread_inst.start()
    
    def set_status(self, new_status):
        self.cv.acquire()
        new_unique_status = new_status if new_status < 0 else 0
        self.status = new_status
        if new_unique_status != self.unique_status:
            self.have_new_status = True
            self.unique_status = new_unique_status
            self.cv.notifyAll()
        self.cv.release()
    
    def exit_thread(self):
        self.cv.acquire()
        self.exiting = True
        self.cv.notifyAll()
        self.cv.release()
        self.led_thread_inst.join()
        if self.button_thread_inst is not None:
            self.button_thread_inst.join()
    
    @staticmethod
    def get_led_period_from_cpu_usage(cpu_usage):
        cpu_usage = min(max(cpu_usage, 0), 100)
        return 0.5 / ((cpu_usage / 100.0) * (MAX_LED_FREQ - MIN_LED_FREQ)
            + MIN_LED_FREQ)
    
    def led_thread(self):
        exiting = False
        active_on = True
        while not exiting:
            self.cv.acquire()
            
            check_again = True
            while check_again and not self.have_new_status and not self.exiting:
                if self.status >= 0:
                    self.cv.wait(
                        timeout=LEDController.get_led_period_from_cpu_usage(
                            self.status))
                    check_again = False
                else:
                    self.cv.wait()

            exiting = self.exiting
            status = self.status
            have_new_status = self.have_new_status
            
            self.have_new_status = False
            self.cv.release()

            # TODO: Fix potential race condition
            if have_new_status or exiting:
                GPIO.output(self.gpio_ids[0], False)
                GPIO.output(self.gpio_ids[1], False)

            if not exiting:
                if status >= 0:
                    GPIO.output(self.gpio_ids[0], active_on)
                    active_on = not active_on
                elif status == LEDMode.Success:
                    GPIO.output(self.gpio_ids[0], True)
                    active_on = True
                elif status == LEDMode.Error:
                    GPIO.output(self.gpio_ids[1], True)
                    active_on = True

    def button_thread(self):
        exiting = False
        while not exiting:
            self.cv.acquire()
            if not self.exiting:
                self.cv.wait(timeout=0.1) # Wait at most a tenth of a second
            exiting = self.exiting
            status = self.status
            self.cv.release()

            # TODO: Fix potential race condition
            if status < 0 and GPIO.input(self.gpio_ids[2]):
                GPIO.output(self.gpio_ids[0], False)
                GPIO.output(self.gpio_ids[1], False)

class LEDState:
    def __init__(self, led_pairs):
        self.led_pairs = led_pairs
        self.led_controllers = []
        self.exiting = False
        
        #GPIO.emulator_init() # delete if using the real GPIO library
        GPIO.setmode(GPIO.BOARD)
        for led_pair in led_pairs:
            self.led_controllers.append(LEDController(led_pair))
    
    def set_status(self, index, new_status):
        self.led_controllers[index].set_status(new_status)
    
    def cleanup(self):
        for led_controller in self.led_controllers:
            led_controller.exit_thread()

        GPIO.cleanup()
        #GPIO.emulator_fini() # delete if using the real GPIO library
