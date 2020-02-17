import SimpleKivy as sk

# Create the layout of each individual tab.
tab0 = sk.Sublayout([
	[sk.T('Tab0')],
	[sk.B('Ok')]])
tab1 = sk.Sublayout([
	[sk.T('Tab1'),sk.In()]
	])
tab2 = sk.Sublayout([
	[sk.T('Tab2'),sk.DD()],
	[sk.T('Switch me:'),sk.Switch()]])

# All the stuff inside your window.
layout = [
	[sk.T('Example of Tab groups and Sublayouts:',size=(0,30))],
    [sk.TabPanel(tab_items=[tab0, tab1, tab2],
    	tab_headers='First tab,Second tab,Third tab'.split(','),
    	key='tabgroup'
    	)],
    [sk.Void(size=(None,60))],
    [sk.Sublayout([[sk.Void(),sk.B('Read',)]],size=(None,60))]
]

# Your main program must be inside a function with 3 arguments (app,event,values) and
# should be added as the event_manager argument of the Window class.


def main(app, event, values):
        # The main program will be called every time the user interacts with
        # the window.
    print('#', event, '#')
    print(values)


# Create the Window
window = sk.Window(title='App with Tabs Panel',size=(None,400),
                   layout=layout, event_manager=main)

# Start the Window
window.Run()
