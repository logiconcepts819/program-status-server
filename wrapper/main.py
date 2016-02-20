import sys
from subprocess import Popen
from psutil import Process, NoSuchProcess
import time
from exit_code_client import ExitCodeClient
from led_state import LEDMode

def main(argv):
    p = Popen(argv[1:])
    
    try:
        client = ExitCodeClient()
        try:
            proc = Process(pid=p.pid)
            while p.poll() is None:
                total_cpu_percent = proc.get_cpu_percent(interval=0)
                for child_proc in proc.get_children(recursive=True):
                    total_cpu_percent += child_proc.get_cpu_percent(interval=0)
                client.send_status(total_cpu_percent)
                time.sleep(0.1) # recommended waiting period from psutil docs
        except NoSuchProcess:
            pass
    except KeyboardInterrupt:
        try:
            p.terminate()
        except OSError:
            pass
    
    client.send_status(LEDMode.Success if p.returncode == 0 else LEDMode.Error)
    time.sleep(0.5) # Give server time to read value before connection closes
    client.shutdown()
    
    return p.returncode

if __name__ == '__main__':
    sys.exit(main(sys.argv))