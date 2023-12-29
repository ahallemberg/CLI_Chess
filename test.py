import threading
import itertools
import time
import sys

# Function for the loading spinner
def spinner() -> None:
    for c in itertools.cycle('/-\|'):
        sys.stdout.write('\r' + c)
        sys.stdout.flush()
        time.sleep(0.1)

# Function to perform your main task
def long_running_task() -> None:
    # Replace this with your actual task
    time.sleep(5)  # Simulating a long task

# Main program
if __name__ == "__main__":
    # Start the spinner in a separate thread
    spin_thread = threading.Thread(target=spinner)
    spin_thread.start()

    try:
        # Perform your main task here
        long_running_task()
    finally:
        # Stop the spinner
        spin_thread.do_run = False
        spin_thread.join()
        sys.stdout.write('\rDone! ')
        sys.stdout.flush()
