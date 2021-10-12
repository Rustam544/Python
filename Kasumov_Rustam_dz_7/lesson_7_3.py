import os
import shutil

root_dir = 'my_project'
dts = r'my_project\templates'
if not os.path.exists(dts):
    os.mkdir(dts)
for root, dirs, files in os.walk(root_dir):
    pos_slash = root.find('templates')
    if root[pos_slash:] == 'templates':
        for dir_elem in dirs:
            if not os.path.exists(os.path.join(dts, dir_elem)):
                shutil.copytree(os.path.join(root, dir_elem), os.path.join(dts, dir_elem))
print('Operation completed successfully.')
