import time

def countdown(n):
    while n > 0:
        print(n)
        n -= 1
        time.sleep(1)
    print('Timer completed!')
    
n=input("How many seconds: ")

countdown(int(n))

