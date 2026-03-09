print("Fibonacci Sequence Generator,choose one of the following options:print 1 or 2")
choise=input("1. Generate Fibonacci numbers up to a certain count\n2. Generate Fibonacci numbers up to a certain value\n")      
if choise == '1':
    maxs=int(input("Enter the number of Fibonacci numbers to generate: "))
    a,b=0,1
    fib=[0,1]
    for i in range(maxs):
        nexts=fib[i]+fib[i+1]
        fib.append(nexts)
    print(fib[:maxs])
elif choise == '2':
    maxs=int(input("Enter the number of Fibonacci numbers to generate: "))
    a,b=0,1
    fib=[0,1]
    while fib[-1]<maxs:
        nexts=fib[-1]+fib[-2]
        fib.append(nexts)
    print(fib[:maxs])
else:    print("Invalid option, please choose 1 or 2")


