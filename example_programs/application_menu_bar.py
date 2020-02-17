import SimpleKivy as sk

# The menu definition is a dictionary like this:
menu_definition={
'File':{
    'New':None,
    'Recent':{
    	'file1':None,
    	'file2':None},
    '---':None,
    'Exit':None},
'Tools':{},
'Help':{
    'Support':'disabled',
    'About':None,
    'Extras':{
    	'extra1':None,
    	'extra2':None}},
}

# All the stuff inside your window.
layout = [[sk.MenuBar(key='menubar',menu_def=menu_definition)],
		  [sk.Sublayout([
		  	[sk.T('Enter some text:'),sk.InputText(key='input')],
		  	[sk.B('Ok'),sk.B('Cancel')]
		  	])]
          ]

# Your main program must be inside a function with 3 arguments (app,event,values) and 
# should be added as the event_manager argument of the Window class.
def main(app, event, values):
        # The main program will be called every time the user interacts with the window.
    print('#',event,'#')

    if event in ['Cancel','menubar:Exit']:  # close the app if user clicks Cancel or selects Exit in menu
        app.Close()
        # window.Close() # this works too (just comment "app.Close()")
    
    elif event is 'Ok': # detect the 'Ok' button click
    	print('You entered:', values['input'])


# Create the Window
window = sk.Window(title='App With Menu',layout=layout, event_manager=main,size=(600,150))

# Start the Window
window.Run()