import multiprocessing
import time
import os
import sys

def func(total, id):
    os.system("python uncensor_preprocess_new.py " + str(id) " " + str(total))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print ("Format: python run_task.py number_of_core")
        return
    number = int(sys.argv[1])
    pool = (processes = number)
    
    pool = []
    for id in range(number):
        p = multiprocessing.Process(func, (number, id))
        pool.append(p)
        p.start()

    print "Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~"
    pool.close()
    pool.join()    # behind close() or terminate()
    print "Sub-process(es) done."