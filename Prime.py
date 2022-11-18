num_max = int(input("Enter max val :"))
odd_number = str(input("Enter O/E/B (odd or even or Both): "))
onlyprime = str(input("Enter Y/N [onlyprime?] : "))

flag = False

def prcprime(i,a = 2):
    if num_max > 1:
        for i in range(2, num_max):
            if (num_max % i) == 0:
                flag = True
                  
def number(x,con1,num,N,con):

    if con1 == 'Y':
        if prcprime(x):
            print(" prime " (x))
    elif con1 == 'N':
        if prcprime(x):
            print(" prime "(x))
        else:
            print("n't prime "(x))
        
    if num == 'O':
        for x in range(prcprime):
            print("num")       
    if num == 'E':
        for x in range(prcprime):
               print(num)
    if num == 'B':
        for x in range(prcprime):
               print(x)+(con)
if flag:
    print (num_max, "is not a prime number")
else:
    print(num_max, "is a prime number")