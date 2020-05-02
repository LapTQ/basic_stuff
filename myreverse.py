import mystack

def reverse_file(filename):
    """Overwrite given file with its contents line-by-line reversed."""
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n'))
    original.close()
    
    output = open(filename, 'w')
    while not S.is_empty():
        output.write(S.pop() + '\n')
    output.close()
    

def _transfer(S, T):
    """Move element from stack S to stack T in reserved order."""
    while not S.is_empty():
        T.push(S.pop())
        
def reverse_stack(S):
    """Replace content in stack S in reversed order."""
    temp1 = mystack.ArrayStack()
    temp2 = mystack.ArrayStack()
    _transfer(S, temp1)
    _transfer(temp1, temp2)
    _transfer(temp2, S)
    
    
def main():
        
    
if __name__ == '__main__':
    main()
