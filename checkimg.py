import os

from PIL import Image

def get_files(dir_):
    """
    get_files(dir) -> yield filenames 
    Get files from dir and subdirectories.
    """
    for root, dirnames, filenames in os.walk(dir_):
        for fn in filenames:            
            yield os.path.join(root, fn)

def img_is_good(filename):    
    """
    img_is_good(filename) -> bool
    Return True if image file can be opened, otherwise False.
    """
    try:
        f = Image.open(filename)
    except IOError:
        return False
    else:
        return True

def check_dir(path):
    """
    check_dir(path) ->> filename, is_good
    yields tuple (filename, bool)
    bool is True if filename is readable as an image file.
    bool is False when filename appears corrupted.
    """
    good_files = []
    bad_files = []
    for pfile in get_files(path):
        if img_is_good(pfile):
            yield pfile, True
        else:
            yield pfile, False
