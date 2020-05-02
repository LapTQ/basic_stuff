def move(degs, i, j, n):
    """Move n top disks from peg i to peg j."""
    if n > 0:
        temp = 3 - i - j
        move(degs, i, temp, n - 1)   
        degs[j].append(degs[i].pop(-1))
        print(degs)
        move(degs, temp, j, n - 1)

def towel_of_hanoi(n):
    """Solve towel of Hanoi problem with 100 dishes."""
    degs = [[n - i for i in range(n)], [], []]
    move(degs, 0, 2, n)

towel_of_hanoi(4)


        

