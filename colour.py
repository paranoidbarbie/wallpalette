from colorthief import ColorThief
import os

def importColour(wallpaper = ""):
    ct = ColorThief("{}".format(wallpaper))
    colours = ct.get_palette(color_count=18, quality=10)
    palette = []
    for colour in colours: 
        colour = palette.append(f"#{colour[0]:02x}{colour[1]:02x}{colour[2]:02x}")
    changeColour(palette)


def changeColour(palette):
    #you may wish to change path of your kitty config, in that case replace /.config/kitty/themes/
    path = f"/home/{os.getlogin()}/.config/kitty/themes/"
    #if you wish to use a different name for theme file change colour.conf to your wish, but change it in your kitty.conf too. 
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


