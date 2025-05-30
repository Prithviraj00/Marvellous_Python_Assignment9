import multiprocessing

def Square(n):
    ans= []
    for i in n:
        ans.append(i**2)
    print("Output data",ans)
    
def main():
    data=[]
    print("Enter your number :")
    n = int(input())
    
    print("Enter your elements:")
    for i in range(n):
        no = int(input())
        data.append(no)
    print("Input Data :",data)
    
    T1 = multiprocessing.Process(target=Square(data))
    T1.start()
    
    
if __name__ == "__main__":
    main()