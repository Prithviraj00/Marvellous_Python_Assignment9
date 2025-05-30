import threading
import time

def display():
    for i in range (1,6):
        print(i)
        time.sleep(1)
                

def main():
    T1 = threading.Thread(target=display)
    T2 = threading.Thread(target=display)
    T3 = threading.Thread(target=display)
    
    T1.start()
    T1.join()
    T2.start()
    T2.join()
    T3.start()
    T3.join()

if __name__ == "__main__":
    main()
        