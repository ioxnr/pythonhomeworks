import os
from shutil import copy2

root_dir = os.path.join(os.getcwd(), 'my_project')

path_dir = os.path.join(root_dir, 'templates')

if not os.path.exists(path_dir):
    os.mkdir(path_dir)

for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.html'):
            subdir = os.path.join(path_dir, os.path.split(root)[-1])
            file_path = os.path.join(root, file)
            if not os.path.exists(subdir):
                os.mkdir(subdir)
            if not os.path.exists(os.path.join(subdir, file)):
                copy2(file_path, subdir)
