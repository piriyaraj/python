def merge(A,l,q,r):
    i = 0
    j = q + 1
    k = -1
    Temp = []
    print("r ",r)
    print("q ",q)
    for n in range(0,r+1):
        Temp.append(0)

    while((i <= q) and (j<=r)):
        k = k + 1

        if A[i] <= A[j]:
            Temp[k] = A[i]
            i = i+1

        else :
            Temp[k] = A[j]
            j = j+1

    if j > r:
        for t in range(0,q-i+1):
            print("t inside ",t)
            A[r-t] = A[q-t]

    print("k ",k)
    for t in range(0,k):
        print(l+t)
        A[l + t] = Temp[t]


def mergesort(A,l,r):
    if l < r:
        q = (l +r)//2

        mergesort(A,l,q)
        mergesort(A,q+1,r)
        merge(A,l,q,r)

A = [6,4,8,1,7,2,5,3]

mergesort(A,0,7)

print(list(A))

    
