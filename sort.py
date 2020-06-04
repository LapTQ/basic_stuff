from math import*
S = [2, 4, 5, 2, 0, 0 ,11]

def selection_sort(S):
    n = len(S)
    while n != 0:
        max_index = 0
        for i in range(n):
            if S[max_index] < S[i]:
                max_index = i
        S[n - 1], S[max_index] = S[max_index], S[n - 1]
        n -= 1


def bubble_sort(S):
    for t in range(len(S)):
        for i in range(len(S) - 1):
            if S[i] > S[i + 1]:
                S[i], S[i + 1] = S[i + 1], S[i]


def insertion_sort(a):
    for i in range(1, len(a)):
        cur = a[i]
        j = i
        while j > 0 and a[j - 1] > cur:
            a[j - 1], a[j] = a[j], a[j - 1]
            j -= 1


def merge_sort(S, start, stop):
    if start < stop - 1:
        mid = (start + stop) // 2
        
        merge_sort(S, start, mid)
        merge_sort(S, mid, stop)
        
        def merge(S, start, stop, mid):
            S1 = S[start:mid]
            S2 = S[mid:stop]
            i = 0
            j = 0
            k = start
            while i < len(S1) and j < len(S2):
                if S1[i] < S2[j]:
                    S[k] = S1[i]
                    i += 1
                    k += 1
                else:
                    S[k] = S2[j]
                    j += 1
                    k += 1
            S[k:stop] = S1[i:] if i < len(S1) else S2[j:]
            
        merge(S, start, stop, mid)

def quick_sort(S, start, stop):
    if start < stop - 1:
        
        def partition(S, start, stop):
            pivot = stop - 1
            candidate = start
            while True:
                while candidate < pivot and S[pivot] >= S[candidate]:
                    candidate += 1
                if candidate == pivot:
                    break
                S[pivot], S[candidate] = S[candidate], S[pivot]
                pivot, candidate = candidate, pivot - 1

                while candidate > pivot and S[pivot] <= S[candidate]:
                    candidate -= 1
                if candidate == pivot:
                    break
                S[pivot], S[candidate] = S[candidate], S[pivot]
                pivot, candidate = candidate, pivot + 1
            return pivot
            
        pivot = partition(S, start, stop)
        quick_sort(S, start, pivot)
        quick_sort(S, pivot + 1, stop)
        

merge_sort(S, 0, len(S))

print(S)
