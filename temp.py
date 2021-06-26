import os
os.system("ls")
os.system("cd ")
os.system("ls")
try:
    os.makedirs('my_folder')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise