
def subset(S, i, sub):
    """Produce a nother subset of S from ith element and given subset sub."""
    if i == len(s):         # if the last element was reached
        print(sub)
    else:
         subset(S, i + 1, sub)              # clone subset of super-subset
         subset(S, i + 1, [*sub, S[i]])     # new subset by adding S[i] to super-subset
         
def overlap(s1, s2):
    """Return position j indicating overlap substring.

    Iterate j downward to advoid subtle error (eg: gogg, ggne)
    """
    j = len(s2) - 1
    while j >= 0 and not s1.endswith(s2[:j + 1]):
        j -= 1
    return j



def main():
    subset([1, 2, 3, 4], 0, [[]])

if __name__ == '__main__':
    main()
