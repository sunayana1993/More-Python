import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2) #sleep for 2 sec
        print(f"no is {i}")

def print_letter():
    for i in 'abcde':
        time.sleep(2) #sleep for 2 sec
        print(f"letter is {i}")

t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letter)

t=time.time()
t1.start()
t2.start()
t1.join()
t2.join()
finished_time=time.time()-t
print(finished_time)