# multithreading = Used to perform multiple tasks concurrently (multitasking)
# Good for I/O bound tasks like reading files or fetching data from APIs
# threading.Thread(target = my_function)

import threading
import time

def walk_dog():
    time.sleep(8)
    print("You finish walking the dog")

