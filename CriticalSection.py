import time
from Semaphore import Semaphore

class CriticalSection:
    def __init__(self):
        # we create a semaphore with initial value 1
        # to ensure mutual exclusion
        self.semaphore = Semaphore(1)

    def critical_selection(self, p):
        # entry section: ensure mutual exlcusion
        self.semaphore.P() # Entering critical section
        print (f'Process {p} is entering the cirtical section')

        # Critical section
        print (f'Process {p} is running the cirtical section')

        #time.sleep(5) # for simulating time

        #exit section
        print (f'Process {p} is exiting the cirtical section')
        self.semaphore.V() # release the semaphore