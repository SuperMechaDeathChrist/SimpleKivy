import SimpleKivy as sk

########################################################################
# Pure kivy widget (works in the same way for garden widgets).
from kivy.uix.filechooser import FileChooserIconView
import os

filec = FileChooserIconView(path=os.getcwd(),multiselect=True)
########################################################################

# All the stuff inside your window.
layout=[
[sk.kvElement(
	filec, # the pure kivy element or garden widget.
	value_bind=[filec,'selection'], # which property assign to the values dictionary.
	event_bind=[filec,'path'], # which callback or property change produces an event.
	key='filechooser'
	)],
[sk.B('Read',size=(None,40))]
]

# Your main program must be inside a function with 3 arguments (app,event,values) and 
# should be added as the event_manager argument of the Window class.
def main(app,event,values):
    print('#',event,'#')
    print(values)

    if event is 'filechooser':
    	window.title=app['filechooser'].path

# Create the Window
window = sk.Window(title=filec.path,layout=layout, event_manager=main,
    size=(600,400),
    )
# Start the Window
window.Run()
