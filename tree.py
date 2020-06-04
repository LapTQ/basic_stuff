# table of content for document

def preorder_indent(T, p, d):
    """Print preorder representation of subtree of T rooted at p at depth d."""
    print(2*d*' ' + str(p.element()))
    for c in T.children(p):
        preorder_indent(T, c, d + 1)

def preorder_label(T, p, d, path):
    """Print labeled representation of subtree of T rooted at p at depth d."""
    label = '.'.join(str(j + 1) for j in path)
    print(2*d*' ' + label, p.element())
    path.append(0)                          # path entries are zero-indexed
    for c in T.children(p):
        preorder_label(T, c, d + 1, path)
        path[-1] += 1
    path.pop()


# parenthetic representation of a tree that is computer-friendly
""" Parentetic string representation of a tree is defined as follows
If T consists of a single position p
P(T) = str(p.element())
otherwise,
P(T) = str(p.element()) + '(' + P(T1) + ', ' + ... + P(Tk) + ')'
where p is the root of T and T1, ... Tk are the subtree rooted at the children of p.
"""
def parenthesize(T, p):
    """Print parenthesized representation of subtree of T rooted at p."""
    print(p.element(), end='')
    if not T.is_leaf(p):
        first_time = True
        for c in T.children(p):
            sep = ' (' if first_time else ', '
            print(sep, end='')
            first_time = False
            parenthesize(T, c)
        print(')', end='')


# computing disk space
def disk_space(T, p):
    subtotal = p.element().space()       # assume that a space() method of each element reports the local space used at that position
    for c in T.children(p):
        subtotal += disk_space(T, c)
    return subtotal
