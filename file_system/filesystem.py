import os

def find(path, filename):
    """Return entries of the file system rooted at the given path having the given name."""
    for entry in os.listdir(path):
        childpath = os.path.join(path, entry)
        if entry == filename:
            print(childpath)
        if os.path.isdir(childpath):
            find(childpath, filename)
  
  
def disk_usage(path):
    """Return the cumulative disk space used by a file/folder and any descendents."""
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)
            
    print("{0:<7}".format(total), path)
    return total
    
            

find("/home/ad/Workspace/trivial_projects", "filesystem.py")
