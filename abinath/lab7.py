A = []

for i in range(10,21):
    print("loop number ",i)
    A.append(int(input("Enter a number ; ")))


def insertionsort(A):

    n = len(A)
    for j in range(1,n):
        print(j)
        key = A[j]
        i = j-1

        while (i >= 0) and (A[i] > key):
            A[i+1] = A[i]
            i = i-1

        A[i + 1] = key


insertionsort(A)

print(list(A))
