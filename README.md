# SimpleKivy
A new way to make Kivy apps using a PySimpleGUI approach

# Installation
You need to install the latest version of `Kivy`. Installation instructions can be found [here](https://kivy.org/doc/stable/gettingstarted/installation.html).
## Garden widgets
The kivy widget library is always being expanded by the `kivy-garden` widgets. This python library also aims to include the most common ones for more complete and faster development of complex apps.

You need to install these `kivy-garden` widgets:

* ```context_menu: pip install kivy_garden.contextmenu```

## SimpleKivy.py
At the moment, you only need the `SimpleKivy.py` file to use this library. You can either keep it in the same directory as your main code or place it in your `.../Lib` directory . You can download it from this branch.
Other means of installation are not supported at the moment. 

**This project is in the early stages of development and is expected to change in the future.**

**Use at you own risk.**

# Usage

### This Code

```python
import SimpleKivy as sk

# All the stuff inside your window.
layout = [[sk.Text('Some text on Row 1')],
          [sk.Text('Enter something on Row 2'), sk.InputText(key='input')],
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

and returns the value input as well as the button clicked.

![hello_world_window](https://github.com/SuperMechaDeathChrist/SimpleKivy/raw/master/hello_world_window.PNG)




