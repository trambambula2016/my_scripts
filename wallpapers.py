import os
import random
import ctypes

wallpapers_dir = "C:\\Users\\marcin\\Downloads\\tapety\\"
wallpapers_list = []
for root, dirs, files in os.walk(wallpapers_dir):
    for file in files:
        if file.endswith('.jpg'):
            wallpapers_list.append(file)
        if file.endswith('.jpeg'):
            wallpapers_list.append(file)
			
print(wallpapers_list)
wallp = wallpapers_dir+random.choice(wallpapers_list)

SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, wallp, 3)

