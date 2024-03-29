
def selection_sort(A):
    for i in range(len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j

        A[i], A[min_idx] = A[min_idx], A[i]
    return A


A = [64, 25, 12, 22, 11]
print("\nInitial array")
for i in range(len(A)):
    print(A[i], end=" ")

print("\nSorted array")
sorted_A = selection_sort(A)
for i in range(len(sorted_A)):
    print(sorted_A[i], end=" ")


