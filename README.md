<div align='center'>
  <h1>WallPalette</h1>
  <p>A project to auto change the wallpaper and the respective colourcheme of the terminal. (for Hyprland)</p>
</div>

## How to get it to work

1. Clone this repository. 
2. Create a folder called wallpaper in your ~/Pictures ```mkdir ~/Pictures/wallpaper```
   - put your wallpapers in that folder[^1]
     - create a kitty config folder where will be the basic config ```mkdir ~/.config/kitty/themes/```

3. cd into the git repository ```cd wallpalette```
   - enable venv
     - install colorthief ```python -m pip install colorthief```
5. run the main.py ```python main.py```

[^1]: only png or jpg


