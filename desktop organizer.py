# A Python script that moves all desktop items to one folder named 'Home', while leaving your games folder alone

# Tested on Windows 11 by manually running it in PowerShell and by directly opening the script file

# Please don't change the file name because it's hardcoded in the exceptions list

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

# The exceptions list:
# Basically a for loop that has an if statement that checks for the given file/folder names and skip them if found, then move the rest
for s in the_stuff:

    source_path = os.path.join(path_desktop, s)

    if s == 'Home' or s == 'desktop.ini' or s == 'desktop organizer.py' or s == 'desktop organizer.exe' or s == 'Games' or s == 'games' or s == 'GAMES':
        continue

    shutil.move(source_path, path_home)
    # The essence is done
    # The rest is making the final experience more interactive/intuitive for normal users
    print('Moved:', s)

time.sleep(0.5)
print('Done')
time.sleep(1)
input('Press Enter to exit')

# I also added 'desktop organizer.exe' in the exceptions list, so it runs fine if you bundle or compile it