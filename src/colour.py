#from colorthief import ColorThief
import os
from palette import generate_palette

def importColour(wallpaper = "tests/testimage.png"): 
    colours = generate_palette(wallpaper)
    palette = []
    for colour in colours: 
        colour = palette.append(f"#{colour[0]:02x}{colour[1]:02x}{colour[2]:02x}")
    #print(colours)
    #print(palette[1])
    changeColour(palette)


def changeColour(palette):
    path = f"/home/{os.getlogin()}/.config/kitty/themes/"
    filename = os.path.join(path, 'colour.conf')
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


