x = int(input("Enter x : "))

n = int(input("Enter y : "))

def pow(x,n):
    if(n == 0):
        return 1
    elif(n > 0):
        return x * pow(x, n-1)

print(pow(x,n))
