import threading

class Semaphore:
    def __init__(self, initial):
        # create a condition variable to associate with a lock
        # this will be used to synchronize threads that are 
        # waiting for the semaphore
        self.lock = threading.Condition(threading.Lock())

        # the initial valye of the semaphore
        self.value = initial

    def P(self):
        # we use the context manager to ensure that
        # the lock is acquired before we proceed
        # and release automatically
        with self.lock:
            # if the semaphore value is zero or less, 
            # then we wait until it becomes positive
            while self.value <= 0:
                self.lock.wait() # block the process or thread.
                self.value -= 1

    def V(self):
        with self.lock:
            # increment the semaphore value to indicate resource release.
            self.value += 1 
            # we notify the waiting threads that the sempahore value has changed.
            self.lock.notify()
