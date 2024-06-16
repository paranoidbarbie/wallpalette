import os
import time
from colour import importColour

#wallpaper directory, change it according to your needs. change only from the Pictures. 
#for example directory = f'/home/{os.getlogin()}/<Path to your image folder>' 
directory = f'/home/{os.getlogin()}/Pictures/wallpaper/' 
os.chdir(directory)

def changeImage():
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
    time.sleep(3)
    os.system(f'hyprctl hyprpaper wallpaper "eDP-1,{wallpaper}"')
    os.system('hyprctl dispatch exec hyprpaper')
    importColour(wallpaper)
    

def takeEffect():
    while True:
        time.sleep(3)
        changeImage()

if __name__ == "__main__":
    takeEffect()
