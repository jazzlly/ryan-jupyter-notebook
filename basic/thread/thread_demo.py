#%%

import threading
import time
from threading import  current_thread

def my_thread(a,b):
    print(current_thread().getName(), 'start')
    print("a: %s, b: %s" % (a,b))
    time.sleep(1)
    print(current_thread().getName(),'stop')

threads = []
for i in range(10):
    # my_thread(i, i+1)
    t1 = threading.Thread(target=my_thread, args=(i, i+1))
    t1.start()
    threads.append(t1)

for t in threads:
    t.join()

#%%

class MyThread(threading.Thread):
    def run(self):
        print(current_thread().getName(),'start')
        time.sleep(1)
        print(current_thread().getName(), 'stop')

t = MyThread()
t.start()
t.join()

print(current_thread().getName(), 'end')

#%%
import queue

q = queue.Queue()
q.put(1)
q.put(2)
print(q.get())

#%%

import time
import random
import threading
from queue import Queue
from threading import  current_thread

queue = Queue(5)

class ProducerThread(threading.Thread):
    def run(self):
        global queue
        num = range(1000)

        for i in range(5):
            queue.put(random.choice(num))
            time.sleep(random.randint(1,3))

class ConsumerTheard(threading.Thread):
    def run(self):
        cnt = 0
        while True:
            e = queue.get()
            queue.task_done()
            print(e)
            cnt += 1
            if (cnt >= 3):
                break

producer = ProducerThread()
consumer = ConsumerTheard()

producer.start()
consumer.start()

producer.join()
print('producer join done')

consumer.join()
print('consumer join done')
