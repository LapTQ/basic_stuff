"""
https://projecteuler.net/problem=105

Let S(A) represent the sum of elements in set A. 
At a special set if for any two non-empty disjoint subsets, B and C, the following properties are true:

i.  S(B) ≠ S(C); that is, sums of subsets cannot be equal.
ii. If B contains more elements than C then S(B) > S(C).

For example, {81, 88, 75, 42, 87, 84, 86, 65} is not a special sum set because 65 + 87 + 88 = 75 + 81 + 84, 
             {157, 150, 164, 119, 79, 159, 161, 139, 158} satisfies both rules for all possible subset pair combinations.
             
Identify all the special sum sets, A1, A2, ..., Ak, and find the value of S(A1) + S(A2) + ... + S(Ak)
"""



from math import ceil

def overlap(B, C):
    for i in B:
        if i in C:
            return True
    return False
    
def subset(A):
    subsets = [[]]
    for i in range(len(A)):
        j = 0
        cur_len = len(subsets)
        while j < cur_len:
            new_subset = subsets[j] + [A[i]]
            subsets.append(new_subset)
            j += 1
    return subsets

def check_first(A):
    """Return True if all S(B) is different from S(C)."""
    Subset = subset(A)
    for i in range(len(Subset) - 1):
        for j in range(i + 1, len(Subset)):
            if not(overlap(Subset[i], Subset[j])) and sum(Subset[i]) == sum(Subset[j]):
                return False                	   
    return True
            
def check_second(A):
    """Return True if with any sub B and C such that len(B) > len(C), we have sum(B) > sum(C)"""
    A.sort()
    #print(A)
    sep = len(A)//2 + 1         # B (max length) = A[:sep], C (max length) = A[sep:]
    for i in range(len(A) - sep):
        if sum(A[:i + 2]) <= sum(A[len(A) - 1 - i:]):   
            return False
    return True

def is_special(A):
    """Return sum(A) if A is special, 0 otherwise."""
    return sum(A) if check_second(A) and check_first(A) else 0
    
def main():
    infile = open("input.txt", "r")
    S = 0
    for line in infile:
        A = eval('[' + line + ']')
        S += is_special(A)
    print(S)
    infile.close()

    
main()


"""
With the second constraint, we sort A in increasing order and assume that len(B) > len(C).
If B = A[0:2], C = A[-1] then all 2-element B and 1-element C will satisfy.
Likewise with (n + 1)-element B and n-element C.

With the first constraint, we create a list of S[D], with D is any possible subset of A.
If there is any duplicate in that list, A is not special.

Check the second constraint first because it's simpler.
"""

-------------------------------------------------------------------------------

