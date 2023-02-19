import os, sys

def print_dirs(catalog='.', depth=0):
    if depth < 0:
        return
    
    if not os.path.isdir(catalog):
        return

    dirs = os.listdir(catalog)
    
    for dir in dirs:
        print(f"{catalog}/{dir}")
    
        print_dirs(f"{catalog}/{dir}", depth - 1)

if __name__ == '__main__':
    catalog = '.' if len(sys.argv) < 2 else sys.argv[1]
    depth = 0 if len(sys.argv) < 3 else int(sys.argv[2])
    print_dirs(catalog, depth)