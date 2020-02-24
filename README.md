# SimpleKivy
A new way to make Kivy apps using a **PySimpleGUI** approach and with all the power of **Kivy**

# Installation
##### SimpleKivy has only been tested on **Windows 10** and Python 3
### Kivy
You need to install the latest version of `Kivy`. Installation instructions can be found [here](https://kivy.org/doc/stable/gettingstarted/installation.html).

### Garden widgets
The kivy widget library is always being expanded by the `kivy-garden` widgets. This python library also aims to include the most common ones for more complete and faster development of complex apps.

You need to install these `kivy-garden` widgets:

* context_menu: ```pip install kivy_garden.contextmenu```

### SimpleKivy.py
At the moment, you only need the `SimpleKivy.py` file to use this library. You can either keep it in the same directory as your main code or place it in your `.../Lib` directory . You can download it from this branch.
Other means of installation are not supported at the moment. 

* **This project is in the early stages of development and is expected to change in the future.**

* **Use it at your own risk.**

# Usage

### This Code

```python
import SimpleKivy as sk

# All the stuff inside your window.
layout = [[sk.Text('Some text on Row 1')],
          [sk.Text('Enter something on Row 2:'), sk.InputText(key='input')],
          [sk.Button('Ok'), sk.Button('Cancel')]]

# Your main program must be inside a function with 3 arguments (app,event,values) and 
# should be added as the event_manager argument of the Window class.
def main(app, event, values):
        # The main program will be called every time the user interacts with
        # the window.    
    print('#',event,'#')

    if event in ['Cancel']:  # close the app if user clicks Cancel
        app.Close()
        # window.Close() # this works too (just comment "app.Close()")
    
    elif event is 'Ok': # detect the 'Ok' button click
    	print('You entered:', values['input'])


# Create the Window
window = sk.Window(layout=layout, event_manager=main,size=(600,200))

# Start the Window
window.Run()
```

### Makes This Window

![hello_world_window](https://github.com/SuperMechaDeathChrist/SimpleKivy/raw/master/images/hello_world_window.PNG)

and returns the value input as well as the button clicked.

# New Features
- **Renamed some element classes for consistency.**
- **New widgets: Watch, ScrollableSublayout, ToggleButton, ComboBox.**
- **More customization options for all widgets.**
- **Keep-on-top and alpha (transparency) options for the window (only Windows platforms).**
- **Expanded Text customization (background color).**
- **Expanded InputText customization (vertical aligment).**
- **All color options can be entered as keywords (see SimpleKivy.Colors): ```Text('Hello World', background_color='blue')```.**
- **Default fonts can be entered as keywords (see SimpleKivy.Fonts): ```Text('Hello World', font_name='roboto it')```.**
- **Default options (Fonts, Colors, ...) are case-insensitive: 'red'=='Red'**
- **kvElement: New in-between class that integrates pure kivy widgets into the SimpleKivy architecture. No more waiting for developer implementation to use all the kivy features!!!** *(Go to documentation to know how to use it)*

# In Development
- **Popup implementation.**
- **File-chooser implementation.**
- **Examples and documentation.**

# Supported Elements
This is a list of the supported elements that you can use in your window layouts right now:

***Type**: Class_name = Alias*
* **Text**: T = Text
* **Text markdown renderer**: TMarkup = TextMarkup
* **Buttons**: B = Button
* **ToggleButtons (used in a group with the same graoup_id)**: TB = ToggleButton
* **Voids**: Void
* **Text inputs**: In = InputText
* **Multiline text input**: Multiline
* **Combo box (input text and dropdown values)**: DropDown = DD = CB = ComboBox
* **Spinner**: Spin = Spinner
* **Progress bar**: PB = ProgressBar
* **Image**: Image
* **Box**: Box
* **MenuBar**: MenuBar
* **Slider**: Slider
* **CheckBox (becomes radiobutton when setting a group_id)**: Check = CheckBox
* **Switch on/off**: Switch
* **Video**: Video = VD
* **Video player**: VideoPlayer = VDP
* **Tabbed Panel**: TabGroup = TabPanel
* **Multiple screens (with transition animations)**: ScreenManager
* **Sublayouts (used as standalone widgets or tab and screen items)**: Column = Subl = Sublayout
* **Scrollable sublayouts (same as sublayouts but with scrollable optinos )**: SSubl = SSublayout = ScrollSublayout
* **Watch. Binds current time to a widget (see SimpleKivy.TimeFormats)**: Watch
* **kvElement (in-between class that integrates pure kivy widgets into the SimpleKivy architecture)**: kvElement

Don't use these inside layouts:
* **Window**: Window
* **Layout**: Layout

**Customization (colors/style) of these elements is a work in progress**

# Donate
The best way to encourage future development and maintenance of this project is by donating.


[![paypal](https://www.paypalobjects.com/en_US/MX/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=339JUWC5BY6UN&source=url)

![paypal_QR](https://github.com/SuperMechaDeathChrist/SimpleKivy/raw/master/images/paypal_QR.png)

Either way, **SimpleKivy is free to use!**
