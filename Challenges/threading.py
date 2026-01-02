import sys
import random
import threading
import time

from Challenges.util import pr

def print_numbers(name):
    for i in range(5):
        interval = random.uniform(.5, 1.5)
        print(f"{name}: prints {i}")
        time.sleep(0.5)
        
def basic_threading():
    t1 = threading.Thread(target=print_numbers, args=('Thread 1',))
    t2 = threading.Thread(target=print_numbers, args=('Thread 2',))
            
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('DONE')
    
def mid_threading():
    results = []
    def append_numbers(name):
        for i in range(5):
            interval = random.uniform(0.5, 1.5)
            results.append({name: i})
            print(f'Thread {name} adds index {i} to the list.')
            time.sleep(interval)
    
    threads = [threading.Thread(target=append_numbers, args=(f'Thread {x}',)) for x in range(5)]
    print(threads)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    pr(results)
    
def simulate_io(name):
    # Prints {name} starting...
    # Sleep rand(1-3)
    # Print('name' finished...)
    return

def adv_threading():
    for i in range(5):
        interval = random.uniform(0.5, 1.5)
        print('Counting ')
    # Measure time sequentially
    seq_time = 0
    
    threads = (threading.Thread(target=simulate_io, args=(f'Thread {x}',)) for x in range(5))
    for t in threads:
        t.start()
    for t in threads:
        t.join()

if __name__ == '__main__':
    exercise = 1
    try:
        exercise = None if len(sys.argv) == 1 else int(sys.argv[1])
    except:
        print('Argv[1] must be a valid integer')
    if exercise == 1:
        print('Exercise 1: Print Numbers')
        basic_threading()
    elif exercise == 2:
        print('Exercise 2: Appending Numbers')
        mid_threading()