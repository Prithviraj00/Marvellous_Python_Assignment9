import multiprocessing
import threading
import time

def Display():
    sum = 0
    for i in range(1,10000000):
        sum = sum + i 
    
def main():
    start_time = time.time()
    
    Display()
    
    end_time = time.time()
    print("Time required for Normal Function is : ",end_time-start_time)
    
    start_time = time.time()
    
    T1= threading.Thread(target=Display)
    T1.start()
    T1.join()
    
    end_time = time.time()
    print("Time required for Thread Function is : ",end_time-start_time)
    
    start_time = time.time()
    
    T1 = multiprocessing.Process(target=Display)
    T1.start()
    T1.join()
    
    end_time = time.time()
    print("Time required for MultiProcessing Function is : ",end_time-start_time)
    
    
    
if __name__ == "__main__":
    main()