from Semaphore import Semaphore
class BoundedBuffer:
    def __init__(self, size):
        # empty slots
        self.semaphore_empty = Semaphore(size)

        # full slots
        self.semaphore_full = Semaphore(0)
        self.buffer = []

    def producer(self, item):
        # wait until there is space in the buffer
        self.semaphore_empty.P()
        # produce the item and then add it to the buffer
        self.buffer.append(item)
        print(f'Produced {item}')
        # signal that a slot is full
        self.semaphore_full.V()

    def consumer(self):
        # wait until there is at least one item in the buffer
        self.semaphore_full.P()
        # consumer the first item in the buffer
        item = self.buffer.pop(0)
        print(f'Consumed {item}')
        # signal that a slot is empty
        self.semaphore_empty.V()
        #return item