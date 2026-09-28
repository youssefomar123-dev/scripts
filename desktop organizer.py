# A Python script that moves all desktop items to one folder named 'Home', while leaving your games folder alone

# Tested only on Windows 11 by manually running it in PowerShell

import os
import shutil
import time

path_user = os.path.expanduser('~')

path_home = os.path.join(path_user, 'Desktop', 'Home')

path_desktop = os.path.join(path_user, 'Desktop',)

os.makedirs(path_home, exist_ok=True)

# print(path_user)

# print(path_home)

# print(path_desktop)

# print(os.listdir(path_desktop))

the_stuff = os.listdir(path_desktop)

# shutil.move(the_stuff, path_home) (this is worng because the_stuff here is only an array of strings)

for s in the_stuff:

    source_path = os.path.join(path_desktop, s)

    if s == 'Home' or s == 'desktop.ini' or s == 'desktop organizer.py' or s == 'desktop organizer.exe' or s == 'Games' or s == 'games' or s == 'GAMES':
        continue

    shutil.move(source_path, path_home)
    print('Moved:', s)

time.sleep(0.5)
print('Done')

# if you read this, you are awesome

# I added 'desktop organizer.exe' in the exception parameters, so it runs fine if you bundle or compile it