import os
os.system("ls")
os.system("cd $HOME")
os.system("ls")
try:
    os.makedirs('my_folder')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise