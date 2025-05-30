import threading
def display(n):
    for i in range(1,n+1,1):
        print(i)

def reverse(n):
    for i in range(n,0,-1):
        print(i)
    
def main():
    print("Enter your Number :")
    value1 = int(input())
    
    T1= threading.Thread(target=display(value1))
    T2= threading.Thread(target=reverse(value1))
    T1.start()
    T1.join()
    T2.start()
    T2.join()
    
    
if __name__ == '__main__':
    main()