import SimpleKivy as sk

# All the stuff inside your window.
layout = [[sk.Text('Multiline Text input:',size=(None,60)),sk.Text('Markup text:',size=(None,60))],
          [sk.Multiline(
text='''.. _top:

Hello world
===========

This is an **emphased text**, some ``interpreted text``.
And this is a reference to top_::

    $ print("Hello world")
''',
            key='input',enable_events=True),sk.T_markup(key='tmark')],
          # [sk.Button('Ok',size=(None,60)), sk.Button('Cancel',size=(None,60))],
          ]

# Your main program must be inside a function with 3 arguments (app,event,values) and 
# should be added as the event_manager argument of the Window class.
def main(app, event, values):
        # The main program will be called every time the user interacts with
        # the window.    

    if event in ['Cancel']:  # close the app if user clicks Cancel
        app.Close()
        # window.Close() # this works too (just comment "app.Close()")
    
    elif event is 'input': # detect the 'Ok' button click
    	app['tmark'].text=values['input']


# Create the Window
window = sk.Window(title='reStructuredText renderer',layout=layout, event_manager=main)

# Start the Window
window.Run()