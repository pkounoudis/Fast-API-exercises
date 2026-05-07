import time

def task1():
    print("Task 1 started")
    time.sleep(2)
    print("Task 1 finished")

def task2():
    print("Task 2 started")
    time.sleep(1)
    print("Task 2 finished")

"Run tasks sequentially"
task1()
task2()