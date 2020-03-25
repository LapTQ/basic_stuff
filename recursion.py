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
        

        
import os

def disk_usage(path):
    """Return the cumulative disk space used by a file/folder and any descendents."""
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)
            
    print("{0:<7}".format(total), path)
    return total



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
 
 
def binary_sum(S, start, stop):
    """Return the sum of S[start:stop]."""
    if start >= stop:
        return 0
    elif start == stop - 1:
        return S[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)

print(binary_sum([1, 2, 3, 4, 6, 7], 0, 5))





