import sys, os, shutil

def copy_files(files):
    if len(files) <= 2:
        return

    destination = files[1]
    for file in files[2:]:
        shutil.copy(f"./{file}", os.path.join(os.getcwd(), destination, file))

if __name__ == '__main__':
    copy_files(sys.argv)