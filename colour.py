from colorthief import ColorThief
import os

def importColour(wallpaper = "/home/yoru/Pictures/wallpaper/sunsetwindow.png"):
    ct = ColorThief("{}".format(wallpaper))
    colours = ct.get_palette(color_count=18)
    palette = []
    for colour in colours: 
        colour = palette.append(f"#{colour[0]:02x}{colour[1]:02x}{colour[2]:02x}")
    changeColour(palette)


def changeColour(palette):
    path = f"/home/{os.getlogin()}/.config/kitty/themes/"
    filename = os.path.join(path, 'night.conf')
    colourSteps = 16
    colourDict = {}

    colourOne = palette[0]
    colourTwo = palette[1]

    basicDict = {
        'background' : colourOne,
        'foreground' : colourTwo
            }
    
    for i in range(2,colourSteps):
        key1 = f'color{i-2}'
        key2 = palette[i]
        colourDict[key1] = key2
    
    with open(filename, 'w') as file:
        for key, value in basicDict.items():
            file.write(f'{key} {value}\n')

        for colour, palette in colourDict.items():
            file.write(f'{colour} {palette}\n')
    os.system("kill -s USR1 $(pidof kitty)") 

if __name__ == "__main__":
    importColour()


