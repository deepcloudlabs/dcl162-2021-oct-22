import logging
import os
import threading
import time

logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO, datefmt="%H:%M:%S")

logging.info(f"number of logical processors is {os.cpu_count()}.")


def task(name, delay):
    logging.info(f"Thread {name} has started")
    count = 0  # stack
    while count < 3:
        time.sleep(delay)
        count += 1
        logging.info(f"Thread {name} is running for {count} time...")
    logging.info(f"Thread {name} has finished.")


t1 = threading.Thread(target=task, args=('elma', 5))
t2 = threading.Thread(target=task, args=('armut', 3))

t1.start()
t2.start()

t1.join()
logging.info(f"t1.join() returns!")
t2.join()
logging.info(f"t2.join() returns!")
logging.info(f"application is done.")


