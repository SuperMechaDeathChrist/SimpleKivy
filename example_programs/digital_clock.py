import SimpleKivy as sk

# All the stuff inside your window.
layout=[
[sk.Watch(
	widget=sk.Text(font_size=28,font_name='mono'), # widget to wich the current time will be binded (binds to the text property)
	format='12:00:00 AM' # time format: "12 Hours:Minutes:Seconds PM/AM"
	)
],
]

# Your main program must be inside a function with 3 arguments (app,event,values) and 
# should be added as the event_manager argument of the Window class.
def main(app,event,values):
    print('#',event,'#')
    print(values)


# Create the Window
window = sk.Window(title='Clock',layout=layout, event_manager=main,
    size=(200,40),
    resizable=False,
    keep_on_top=True,
    alpha=0.5,
    )
# Start the Window
window.Run()
