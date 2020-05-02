import mystack

def is_matched_parentheses(expr):
    """Return True if all delimeters are properly match."""
    lefty  = '({['
    righty = ')}]'
    S = mystack.ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()
    
    
def is_matched_html_tags(raw):
    """Return True if all HTML tags are properly match."""
    S = mystack.ArrayStack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j + 1)
        if k == -1:
            return False
        tag = raw[j + 1: k].strip()
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if not S.pop().startswith(tag[1:])):
                return False
        j = raw.find('<', k + 1)
    return S.is_empty()
