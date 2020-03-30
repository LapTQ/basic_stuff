def binary_search(data, target, low, high):
    """Return True if target is found in indicated portion of a Python list:
    
    The search only consider the portion from data[low] to data[high] inlusie.
    """
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)
            
            
def draw_line(tick_length, tick_label=''):
    """Draw one line with given tick length (follwed by optional label)."""
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)
    
def draw_interval(center_length):
    """Draw tick interval based on a central tick length."""
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)
        
def draw_ruler(num_inches, major_length):
    """Draw ruler with given number of inches, major tick length."""
    draw_line(major_length, '0')
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))
        

     





def factorial_recursion(n):
    return 1 if n == 0 else n * factorial_recursion(n - 1)
    

def unique3(S, start, stop):
    """Return True if there are no duplicates in slice S[start:stop]."""
    if stop - start <= 1:
        return True
    elif not unique3(S, start + 1, stop):
        return False
    elif not unique3(S, start, stop - 1): 
        return False
    else:
        return S[start] != S[stop - 1]
        
        
def bad_fibonacci(n):
    """Return the nth Fibonacci number."""
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n - 2) + bad_fibonacci(n - 1)
        
def good_fibonacci(n):
    """Return pair of Fibonacci numbers, F(n) and F(n - 1)."""
    if n <= 1:
        return n, 0
    else:
        a, b = good_fibonacci(n - 1)
        return a + b, a


def reverse(S, start, stop):
    """Reverse element in implicit slice S[start:stop]."""
    if start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        reverse(S, start + 1, stop - 1)

def power(x, n):
    """Compute the value x**n for integer n."""
    if n == 0:
        return 1
    partial = power(x, n// 2)
    return partial * partial if n % 2 == 0 else x* partial * partial
 
def power_non_recursive(a, n):
    """Non-recursive function to compute a^n."""
    result = 1
    while n != 0:
        t = n % 2
        n = n // 2 
        if t == 1:
            result *= a
        a = a * a
    return result
    
def binary_sum(S, start, stop):
    """Return the sum of S[start:stop]."""
    if start >= stop:
        return 0
    elif start == stop - 1:
        return S[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)



def max_recursion_1(S, start, stop):
    """Return the max element of a slice S[start:stop] in O(n) time."""
    if start >= stop - 1:
        return S[start]
    else:
        candidate = max_recursion_1(S, start + 1, stop)
        return S[start] if S[start] >= candidate else candidate
        
def max_recursion_2(S, start, stop):
    """Return the max element of a slice S[start:stop] in O(n) time."""
    if start >= stop - 1:
        return S[start]
    else:
        mid = (start + stop) // 2
        candidate_1 = max_recursion_1(S, start, mid)
        candidate_2 = max_recursion_2(S, mid, stop)
        return candidate_1 if candidate_1 > candidate_2 else candidate_2

def str_to_int(s, start, stop):
    """Convert a string of digits into the integer."""
    if start > stop - 1:
        return 0
    else:
        return str_to_int(s, start, stop - 1) * 10 + ord(s[stop - 1]) - 48

def min_max_1(S, start, stop):
    """Return a tuple (min, max) of a slice S[start:stop]."""
    if start == stop - 1:
        return S[start], S[start]
    elif start == stop - 2:
        return S[start], S[stop - 1] if S[start] < S[stop - 1] else S[stop - 1], S[start]
    else:
        mid = (start + stop) // 2
        candidate_1 = min_max_1(S, start, mid)
        candidate_2 = min_max_1(S, mid, stop)
        return candidate_1[0] if candidate_1[0] < candidate_2[0] else candidate_2[0], candidate_1[1] if candidate_1[1] > candidate_2[1] else candidate_2[1]
        
def min_max_2(S, start, stop):
    """Return a tuple (min, max) of a slice S[start:stop]."""
    if start == stop - 2:
        return S[start], S[stop - 1] if S[start] < S[stop - 1] else S[stop - 1], S[start]
    else:
        return 


def logarithm(n):
    """Return the interger part of the base-two logarithm of n."""
    if n < 2:
        return 0
    else:
        return 1 + logarithm(n / 2)
        

        
        
        
        
        
        
        
        
        
        
        

