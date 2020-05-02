
def subset(S, i, sub):
    """Produce a nother subset of S from ith element and given subset sub."""
    if i == len(s):         # if the last element was reached
        print(sub)     
    else:
         subset(S, i + 1, sub)              # clone subset of super-subset
         subset(S, i + 1, [*sub, S[i]])     # new subset by adding S[i] to super-subset
        
        
def main():
    pass
    
if __name__ == '__main__':
    main()
