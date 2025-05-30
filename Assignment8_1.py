import threading
def even(n):
    for i in range(2,n+1,2):
        print(i)

def odd(n):
    for i in range(1,n+1,2):
        print(i)



def main():
    T1 = threading.Thread(target = even, args =(10,))
    T2 = threading.Thread(target = odd,args =(10,))
    
    T1.start()
    T1.join()
    T2.start()
    T2.join()

if __name__ == '__main__':
    main()