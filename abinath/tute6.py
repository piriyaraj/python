A = [] # this is the way to create an array

for i in range(4):
    A.append(int(input("Enter the number : ")))

def new_insertionsort(A):
    for j in range(1, len(A)): # 1,2,3,4,5,..len(A)-1
        i = 0
       
        while (A[j] > A[i]):
            i = i + 1
            
        key = A[j]

        print(j-i)
        for k in range(0,j-i):

           
            A[j-k] = A[j-k-1]


        A[i] = key

new_insertionsort(A)
print(list(A))
