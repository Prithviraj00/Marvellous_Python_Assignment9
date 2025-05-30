import multiprocessing

def Factorial(n):
    fact = 1
    for i in range (1, n+1):
        fact = fact*i
    return fact
    
def main():
    data=[]
    print("Enter your number :")
    n = int(input())
    
    print("Enter your elements:")
    for i in range(n):
        no = int(input())
        data.append(no)
    print("Input Data :",data)
        
    
    T1=multiprocessing.Pool()
    result = T1.map(Factorial,data)
    
    
    print("Output Data :",result)
    
if __name__ == "__main__":
    main()