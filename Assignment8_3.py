import threading
def even(n):
    sum =0
    for i in n:
        if i % 2 == 0:
            sum = sum + i
    print ("Addition of Evenlist is :",sum)

def odd(n):
    sum =0
    for i in n:
        if i % 2 != 0:
            sum = sum + i
    print ("Addition of oddlist is :",sum)
    
def main():
    data=[]
    print("Enter your Number :")
    value1 = int(input())
    
    print("Enter your list numbers: ")
    for i in range (value1):
        no = int (input())
        data.append(no)
    print("Input data",data)
    
    T1= threading.Thread(target=even(data))
    T2= threading.Thread(target=odd(data))
    T1.start()
    T1.join()
    T2.start()
    T2.join()
    
    
if __name__ == '__main__':
    main()