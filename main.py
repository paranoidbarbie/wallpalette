import os
import time
from colour import importColour
import argparse


def changeImage(directory):
    os.chdir(directory)
    image_format = ["png", "jpg"]
    images = [image for image in os.listdir() if image.endswith(tuple(image_format))]
    for image_name in images:
        wallpaper = os.path.join(directory, image_name)
        setImage(wallpaper)


#if for some reason wallpaper doesn't change please check your monitor settings and 
#change the eDP-1 in line 22 to the displayed monitor name. 
#check your monitor settings by typing hyprctl monitors
def setImage(wallpaper):
    os.system(f'hyprctl hyprpaper preload "{wallpaper}"')
    time.sleep(t)
    os.system(f'hyprctl hyprpaper wallpaper "eDP-1,{wallpaper}"')
    os.system('hyprctl dispatch exec hyprpaper')
    importColour(wallpaper, kittyDir)
    

def takeEffect():
    parser = argparse.ArgumentParser(description="Auto Colour Scheme Changer.")
    parser.add_argument('-d', '--directory', default=f"/home/{os.getlogin()}/Pictures/wallpaper/", help="Type the wallpaper directory. Default is your Pictures/wallpaper/") #change the default value to your wallpaper location, change only from /Pictures
    parser.add_argument('-t', '--time', type=int, default=5, help="Type interval between image change, default is 5 seconds, unit is second.")
    parser.add_argument('-c', '--config', default=f"/home/{os.getlogin()}/.config/kitty/colour.conf", help="Kitty config file path") #change the default value to your path, change only from /.config 
    args = parser.parse_args()
    global t, kittyDir
    t = args.time
    kittyDir = args.config
    while True:
        time.sleep(3)
        changeImage(args.directory)

if __name__ == "__main__": 
    takeEffect()
