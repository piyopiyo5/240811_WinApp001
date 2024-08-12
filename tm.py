import time

def func1():
    print("1")
    
def func2():
    print("2")
    
    
funcList = [func1, func2]


funcList[0]()
time.sleep(3)
funcList[1]()

print("3")