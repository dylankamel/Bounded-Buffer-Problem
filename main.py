import threading
import time
import random

# creating the global variables
n = 20
# creating semaphores
empty = threading.Semaphore(n)
full = threading.Semaphore(0)
mutex = threading.Semaphore(1)
buffer = [-1 for i in range(n)] # creating an empty buffer of size n with values of -1
in_index = 0
out_index = 0
randomvalue = 0

# producer thread
def producer():
    counter = 0
    global in_index, buffer, full, empty, mutex
    while(counter < 100):
        randomvalue = random.randint(1,10) # made a random val to be added
        print("Producer is waiting to write")
        empty.acquire() # wait function
        mutex.acquire()
        time.sleep(1) # for show on the console
        print("Producer has access")
        buffer[in_index] = randomvalue # adding value
        print("Producer added item of value {} at index {}".format(randomvalue, in_index))
        in_index = (in_index + 1) % n # moving the index over
        counter += 1 # while loop counter
        mutex.release() # signal function
        full.release()
        print("Producer has disconnected")
        time.sleep(1) # to give some delay for the consumer to consume an actual value

# consumer thread
def consumer():
    consumed = 0
    global out_index, buffer, emptyt, full, mutex
    while (consumed < 100):
        print("Consumer is waiting to consume")
        full.acquire()
        mutex.acquire()
        time.sleep(1) # for show on the console
        print("Consumer has access")
        value = buffer[out_index] # getting the value that was consumed
        buffer[out_index] = -1 # reseting the value back to -1
        print("Consumer has consumed item of value {} at the index {}".format(value,out_index))
        out_index = (out_index + 1) % n # moving the index along
        consumed += 1 # updating the whole loop counter
        mutex.release()
        empty.release()
        print("Consumer has disconnected")
        time.sleep(2) # to give the producer some time to add some actual values

# creating threads and the target function
p1 = threading.Thread(target = producer, args = ())
c1 = threading.Thread(target = consumer, args = ())
#starting the threads
p1.start()
c1.start()
# joining the threads to the main class thread that way the main class doesnt finsih before the p1 and c1 threads
p1.join()
c1.join()


