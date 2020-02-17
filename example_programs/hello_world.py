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
