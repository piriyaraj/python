def bubblesort(A):

    n = len(A)
    for i in range(0,n-1):
        print("I ",i)
        for j in range(n-1,i,-1):
            print("J ",j)
            if A[j] < A[j-1]:
                temp = A[j]
                temp2 = A[j-1]

                A[j] = temp2
                A[j-1] = temp


A = []
for k in range(8):
    A.append(int(input("Input a number : ")))

bubblesort(A)
print(list(A))
