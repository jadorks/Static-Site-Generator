import os
import shutil

def copy_source_to_destination(source, destination):
    if not os.path.exists(source):
        raise ValueError("Source directory does not exist")
    
    if not os.path.exists(destination):
        os.mkdir(destination)
    else:
        shutil.rmtree(destination)
        os.mkdir(destination)

    static_files = os.listdir(source)

    for entry in static_files:
        path = os.path.join(source, entry)

        if os.path.isfile(path):
            shutil.copy(path, destination)
        else:
            dst = os.path.join(destination, entry)
            copy_source_to_destination(path, dst)
    

def main():
    copy_source_to_destination('static', 'public')


main()
