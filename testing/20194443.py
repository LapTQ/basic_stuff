# 73702

from math import ceil

def overlap(B, C):   # (O(n^2))
    for i in B:
        if i in C:
            return True
    return False
    
def subset(A):     # O(n^2)
    subsets = [[]]
    for i in range(len(A)):
        j = 0
        cur_len = len(subsets)
        while j < cur_len:
            new_subset = subsets[j] + [A[i]]
            subsets.append(new_subset)
            j += 1
    return subsets

def check_first(A): #O(n^4)
    """Return True if all S(B) is different from S(C)."""
    Subset = subset(A)
    for i in range(len(Subset) - 1):
        for j in range(i + 1, len(Subset)):
            if not(overlap(Subset[i], Subset[j])) and sum(Subset[i]) == sum(Subset[j]):
                return False                	   
    return True
            
def check_second(A): #O(nlogn)
    """Return True if with any sub B and C such that len(B) > len(C), we have sum(B) > sum(C)"""
    A.sort()
    sep = len(A)//2 + 1         # B = A[:sep], C = A[sep:]
    for i in range(len(A) - sep):
        if sum(A[:i + 2]) <= sum(A[len(A) - 1 - i:]):   
            return False
    return True

def is_special(A):
    """Return sum(A) if A is special, 0 otherwise."""
    return sum(A) if check_second(A) and check_first(A) else 0
    
def main():
    infile = open("input.txt", "r")
    outfile = open("output.txt", "w")    
    S = 0
    for line in infile:
        A = eval('[' + line + ']')
        S += is_special(A)
               
    print(S)
    infile.close()
    outfile.close()
    
def testing():
    infile = open("input.txt", "r")
    outfile = open("output.txt", "w")    
    S = 0
    for line in infile:
        A = eval('[' + line + ']')
        check_second(A)
               
    
    infile.close()
    outfile.close()
    
    

main()


