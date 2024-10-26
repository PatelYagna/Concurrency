from CriticalSection import CriticalSection
from BoundedBuffer import BoundedBuffer
import threading

# testing critical section

def test_critical_section():
    # create an instance of Critical Section
    cs = CriticalSection()
    # create threads to simulate multiple process/threads
    threads = []

    for i in range(10):
        t = threading.Thread(target = cs.critical_selection(i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

def test_bounded_buffer():
    bb = BoundedBuffer(3)

    #create the producer threads
    producer_threads = threading.Thread(target = lambda: [bb.producer(i) for i in range(10)])
    consumer_threads = threading.Thread(target = lambda: [bb.consumer() for _ in range(10)])

    producer_threads.start()
    consumer_threads.start()

    producer_threads.join()
    consumer_threads.join()

print('Testing Bounded Buffer: ')
test_bounded_buffer()