import threading
def Small(n):
    ans=0
    for i in n:
        if(i >='a'and i<= 'z'):
            ans = ans +1
    print("Number of Small Characters :",ans)
    print("Thread ID is : ",threading.get_ident())
    print("Thread Name is :",threading.current_thread().name)
        

def Capital(n):
    ans=0
    for i in n:
        if(i >= 'A' and i <= 'Z'):
            ans = ans +1
    print("Number of Upper Characters: ",ans)
    print("Thread ID is : ",threading.get_ident())
    print("Thread Name is :",threading.current_thread().name)

def digit(n):
    ans = 0
    for i in n:
        if i.isdigit():
            ans = ans + 1
    print("Number of Digits :",ans)
    print("Thread ID is : ",threading.get_ident())
    print("Thread Name is :",threading.current_thread().name)


def main():
    print("Enter your String :")
    value1 = input()
    
    T1= threading.Thread(target=Small(value1))
    T2= threading.Thread(target=Capital(value1))
    T3= threading.Thread(target=digit(value1))
    T1.start()
    T1.join()
    T2.start()
    T2.join()
    T3.start()
    T3.join()
    
if __name__ == '__main__':
    main()