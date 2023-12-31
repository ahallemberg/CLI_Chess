import threading
import itertools
import time
import sys

class Spinner: 
    def __init__(self, delay: float = 0.1) -> None:
        self.spinner = itertools.cycle('/-\|')
        self.delay = delay
        self.busy = False
        self.spinner_thread = threading.Thread(target=self.spin)
    
    def spin(self) -> None:
        while self.busy:
            sys.stdout.write('\r' + next(self.spinner))
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\r')
            sys.stdout.flush()
    
    def start(self) -> None:
        self.busy = True
        self.spinner_thread.start()
    
    def stop(self) -> None:
        self.busy = False
        self.spinner_thread.join()
        sys.stdout.write('\r ')
        sys.stdout.flush()
