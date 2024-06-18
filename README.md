<div align='center'>
  <img src="https://i.imgur.com/QAkTNfr.gif" width="600px">
  <h1>WallPalette</h1>
  <p>A project to auto change the wallpaper and the respective colourcheme of the terminal. (for Hyprland)</p>
</div>

## Requirements
1. Python, colorthief
2. Kitty 

## Quick settings
> Just follow the default pattern to not run into issues.

1. Create a colour.conf file in your ~/.config/kitty/ (mandatory)
2. In your kitty.conf add a line ```include colour.conf```
3. Create a folder called wallpaper in ~/Pictures/ and put some wallpapers in there.

## Make things default

After you're done Quick settings follow these steps

1. cd into the git repository ```cd wallpalette```
   - activate venv ```python -m venv venv && source venv/bin/activate```
     - install requirements ```pip install -r requirements.txt```
2. run the main.py ```python main.py```

## Usage (no need if you have condifgured files and directories as it's stated above)
1. ```-d --directory Write the wallpaper directory, default is ~/Pictures/wallpaper```
2. ```-t --time      Write the time interval between changing of wallpapers, default is 5sec, unit is seconds```
3. ```-c --config    Write the kitty config file, but make sure to include the config file in your kitty.conf also.```


[^1]: only png or jpg

<details>

<summary>A good advanced tip</summary>

### Run it in the background
> while being in the wallpalette directory

```
nohup python main.py &
```
> To stop the process 

```
ps ax | grep main.py
```
> kill the pid of the main.py process.

</details>

## How to configure the folders according to your needs

1. To if you have wallpapers in some other directory please specify it in the line 29 of main.py
2. To change monitor please check line 24 and replace eDP-1 with your monitorname ```hyprctl monitors```
3. Change kitty config path replace ```/.config/kitty/colour.conf``` to your fav path in line 31, for example ```/.config/<yourpathtoconfigfolder>``` 
    - Also specify the file inside the directory , change colour.conf to your choice , in that case put the file path in your kitty.conf


#### Note: This project is based on [colourthief](https://github.com/fengsp/color-thief-py)

#### This project is still under development, future updates will include better colour generation and faster colour change and futher improvement. Thanks. Keep an eye on testing branch for referrence. 
