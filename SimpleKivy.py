
# import kivy
# print(kivy.kivy_options["video"])
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
# from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.stacklayout import StackLayout
# from kivy.base import EventLoop
# from kivy.network.urlrequest import UrlRequest
# from kivy.uix.slider import Slider
# from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.factory import Factory
Builder.load_string("""
<LabelB>:
  bcolor: 0, 0, 0, 0
  canvas.before:
    Color:
      rgba: self.bcolor
    Rectangle:
      pos: self.pos
      size: self.size
""")

class LabelB(Label):
    bcolor = ListProperty([0,0,0,0])
    pass
Factory.register('KivyB', module='LabelB')

# from kivy.uix.videoplayer import VideoPlayer

import os
# os.environ['KIVY_VIDEO'] = 'ffmpeg'
os.environ['KIVY_VIDEO'] = 'gstplayer'
os.environ['GST_REGISTRY'] = './temp/registry.bin'


def hex2rgb(hex,alpha=None,vmax=255):
    hex=hex.lstrip('#')
    rgb=list(int(hex[i:i+2], 16) for i in (0, 2, 4))
    if not alpha is None:
        rgb.append(alpha)
    
    if vmax !=255:
        rgb=[c/255 for c in rgb]


    return tuple(rgb)


class Layout(GridLayout):
    """docstring for ClassName"""

    def __init__(self, layout=None, event_manager=None,allow_repeated_keys=False,padding=[0,0,0,0], **kwargs):
        super(Layout, self).__init__(**kwargs)


        self.keys = {}
        max_cols = 0
        for row in layout:
            if len(row) > max_cols:
                max_cols = len(row)

        self.cols = max_cols
        self.pos=0, 0
        self.padding=padding
        self.allow_repeated_keys=allow_repeated_keys

        # self.padding=['padding_left', 'padding_top']

        # self.cols = 1
        # self.rows=5
        # self.row_force_default=True
        # self.row_default_height=30
        # self.key=None
        # self.eltype='main_layout'
        self.keys = {}
        self.elements = {}
        self.event_manager = event_manager
        self.values = {}
        self.by_key = {}
        self._by_key = {}
        self.add_at_the_end={}
        self.has_appmenu=False
        i = -1
        for row in layout:
            i += 1
            elnum = -1
            for el in row:
                elnum += 1
                # print(el.eltype, 'i:', i, ', j:', elnum, ', key:', el.key)
                kivy_el=self._process_element((i,elnum),el)
                self.add_widget(kivy_el)
            
            lenrow = len(row)
            addnvoids = 0
            if lenrow < max_cols:
                addnvoids = max_cols - lenrow
            for v in range(addnvoids):
                self.add_widget(Label(text='',size_hint=el.size_hint))

                
                # self.add_widget(Label(text='',size_hint=(None,el.size_hint[1]) ))
                
                # self.add_widget(Label(text=''))

        # for grid_coords in self.add_at_the_end:
        #     pass
        #     self.remove_widget(self.elements[grid_coords])
        #     # top=self.elements[grid_coords]
        #     # top.add_widget(self.add_at_the_end[grid_coords])
        #     # kvWindow.add_widget(top)
        #     self.add_widget(self.add_at_the_end[grid_coords])

    def __getitem__(self, key):
        return self.by_key[key]

    def Close(self):
        App.get_running_app().stop()
    def Start(self,event_start_key='__Start__'):
        self.event_start_key=event_start_key
        self.trigger_event(event_start_key)


    def _process_sublayout(self,grid_coords,sublayout_element):
        sublayout=sublayout_element.layout
        max_cols = 0
        for row in sublayout:
            if len(row) > max_cols:
                max_cols = len(row)
        kivy_sublayout=GridLayout(cols=max_cols,size_hint=sublayout_element.size_hint,padding=sublayout_element.padding)
        i = -1
        for row in sublayout:
            i += 1
            elnum = -1
            for el in row:
                elnum += 1
                # print(el.eltype, 'i:', i, ', j:', elnum, ', key:', el.key)
                new_coords=tuple([c for c in grid_coords]+[i,elnum])
                kivy_el=self._process_element(new_coords,el)
                kivy_sublayout.add_widget(kivy_el)
            
            lenrow = len(row)
            addnvoids = 0
            if lenrow < max_cols:
                addnvoids = max_cols - lenrow
            for v in range(addnvoids):
                kivy_sublayout.add_widget(Label(text='',size_hint=el.size_hint))

                # self.add_widget(Label(text='',size_hint=(None,el.size_hint[1]) ))
                # kivy_sublayout.add_widget(Label(text=''))
                pass

        return kivy_sublayout

    def _process_element(self,grid_coords,el):
        if el.eltype == 'text':
            label=LabelB(text=el.text,color=el.text_color,size_hint=el.size_hint,halign=el.halign,valign=el.valign,bcolor=el.background_color)
            # def bsize():
            #     return label.size
            # label.bind(text_size=bsize)
            label.bind(size=label.setter('text_size'))
            label.text_size=self.size
            self.elements[grid_coords] = label
            # self.elements[grid_coords] = LabelB(text=el.text,size_hint=el.size_hint)
        elif el.eltype == 'rst':
            from kivy.uix.rst import RstDocument
            self.elements[grid_coords] = RstDocument(text=el.text,size_hint=el.size_hint)
        elif el.eltype == 'btn':
            from kivy.uix.button import Button
            self.elements[grid_coords] = Button(
                    text=el.text, on_release=self.trigger_event,
                    size_hint=el.size_hint
                    )
        elif el.eltype == 'menubar':
            if not el.key:
                el.key = grid_coords
            import kivy_garden.contextmenu
            menu_kv=''
            tab='    '

#             kv = """
# AnchorLayout:
#     anchor_y: 'top'
#     height: 30
#     id: layout
#     AppMenu:
#         id: app_menu
#         top: root.height
#         cancel_handler_widget: layout

#         AppMenuTextItem:
#             text: "Menu #1"
#             ContextMenu:
#                 ContextMenuTextItem:
#                     text: "Item #11"
#                     ContextMenu:
#                         ContextMenuTextItem:
#                             text: "file0"
#                         ContextMenuTextItem:
#                             text: "file1"
#                 ContextMenuTextItem:
#                     text: "Item #12"
#         AppMenuTextItem:
#             text: "Menu #2"
#             ContextMenu:
#                 id: menu2
#                 ContextMenuTextItem:
#                     text: "Item #21"
#                 ContextMenuTextItem:
#                     text: "Item #22"
#                 ContextMenuTextItem:
#                     text: "Item #23"
#                 ContextMenuTextItem:
#                     text: "Item #24"
#                     ContextMenu:
#                         ContextMenuTextItem:
#                             text: "Item #241"
#                             color: 1,1,1,0.5
#                         ContextMenuTextItem:
#                             text: "Hello, World!"
#                             on_release: app._general_event('appmenu>'+self.text)
#                             on_release: menu2.hide()
#                             # on_release: self.parent.parent.parent.hide()
#                         # ...
#                 ContextMenuTextItem:
#                     text: "Item #5"
#         AppMenuTextItem:
#             text: "Menu #3"
#             ContextMenu:
#                 ContextMenuTextItem:
#                     text: "SubMenu #31"
#                 ContextMenuDivider:
#                 ContextMenuTextItem:
#                     text: "SubMenu #32"
#                 # ...
#         AppMenuTextItem:
#             text: "Menu #4"
#     # ...
#     # The rest follows as usually
# """
            self.elements['aux_menu_void'] = Label(text='',size_hint=el.size_hint)
            self.elements[grid_coords]=self.elements['aux_menu_void']
            menu_kv=['''
AnchorLayout:
    anchor_y: 'top'
    # padding: app._menu_pos()
    height: '''+str(el.size[1])+'''
    id: layout
    AppMenu:
        id: app_menu
        top: root.height
        cancel_handler_widget: layout
''']
            def _fix_menu(kv):
                newkv=kv.split('\n')
                skv=''
                lkv=len(newkv)
                for i in range(lkv):
                    if i+1<lkv and 'ContextMenu:' in newkv[i] and not 'ContextMenuTextItem' in newkv[i+1]:
                        continue
                    skv+=newkv[i]+'\n'

                return skv
            # csub=[0]
            def _creat_submenu(data,level=1,parent='no_parent',parent_level=1,tab='    '):
                if type(data) is dict:
                    for item in data:
                        if type(data[item]) is dict:
                            if level==1:
                                menu_kv[0]+=tab*2+'AppMenuTextItem:\n'
                                menu_kv[0]+=tab*2+tab*level+'text: \"'+item+'\"\n'
                                menu_kv[0]+=tab*2+level*tab+'ContextMenu:\n'
                                # menu_kv[0]+=tab*3+level*tab+'id: submenu'+str(csub[0])+'\n'
                                # csub[0]+=1
                            else:
                                menu_kv[0]+=tab*2+level*tab+'ContextMenuTextItem:\n'
                                menu_kv[0]+=tab*3+tab*level+'text: \"'+item+'\"\n'
                                menu_kv[0]+=tab*3+level*tab+'ContextMenu: ##\n'
                                level+=1
                                # _creat_submenu(data[item],level+2,parent=item,parent_level=level,tab=tab)
                                # return
                            _creat_submenu(data[item],level+1,parent=item,parent_level=level,tab=tab)
                        else:
                            extra=tab
                            if level%2:
                                extra=''
                            if '---' == item:
                                menu_kv[0]+=tab*1+level*tab+extra+'ContextMenuDivider: #---------------\n'
                                continue
                            else:
                                menu_kv[0]+=tab*1+level*tab+extra+'ContextMenuTextItem: #<--\n'
                                menu_kv[0]+=tab*2+tab*level+extra+'text: \"'+item+'\"\n'
                            if data[item] is None:
                                menu_kv[0]+=tab*2+tab*level+extra+r"on_release: app._general_event('"+str(el.key)+ r">'+self.text)"+'\n'
                                menu_kv[0]+=tab*2+tab*level+extra+r"on_release: app_menu.close_all()"+'\n'
                            elif 'disabled' in data[item]:
                                menu_kv[0]+=tab*2+tab*level+extra+r"color: 1,1,1,0.5"+'\n'

                            
            _creat_submenu(el.menu_def)
            nkv=_fix_menu(menu_kv[0])
            # self.has_appmenu=Builder.load_string(kv)
            print(nkv)
            self.has_appmenu=Builder.load_string(nkv)


        elif el.eltype == 'input':
            from kivy.uix.textinput import TextInput
            self.elements[grid_coords] = TextInput(
                text=el.text, multiline=el.multiline, password=el.password,
                size_hint=el.size_hint,
                use_bubble=el.use_bubble,
                use_handles=el.use_handles,
                write_tab=el.write_tab
                )
            if el.enable_events:
                self.elements[grid_coords].bind(
                    text=self._general_event)
        elif el.eltype == 'spinner':
            from kivy.uix.spinner import Spinner as kivySpinner
            self.elements[grid_coords] = kivySpinner(
                text=el.default_value, values=el.values,
                size_hint=el.size_hint,
                # background_color=[0.9,0.9,1,1]
                )

            from kivy.uix.spinner import SpinnerOption
            from kivy.uix.dropdown import DropDown
            class SpinnerOptions(SpinnerOption):
                def __init__(self, **kwargs):
                    super(SpinnerOptions, self).__init__(**kwargs)
                    self.background_normal = ''
                    self.background_color = [0.9, 0.9, 0.9, 1]    # blue colour
                    self.height = 26

                    # font_color
                    self.color = [0,0,0,1]

            class SpinnerDropdown(DropDown):
                def __init__(self, **kwargs):
                    super(SpinnerDropdown, self).__init__(**kwargs)
                    # self.bar_inactive_color= hex2rgb('#141411',alpha=255)
                    self.bar_color=hex2rgb('#403E3C',alpha=200,vmax=1)
                    # self.bar_inactive_color=hex2rgb('#2A2B25',alpha=255,vmax=1)
                    self.bar_inactive_color=0.4,0.4,0.6,0.6
                    self.bar_width=8
                    self.effect_cls= 'ScrollEffect'
                    self.scroll_type= ['bars', 'content']
                    # self.auto_width = False
                    # self.width = 150

            self.elements[grid_coords].dropdown_cls = SpinnerDropdown        
            self.elements[grid_coords].option_cls=SpinnerOptions
            # self.elements[grid_coords].color=[0,0,0,1]
            # self.elements[grid_coords].background_normal=''
            # self.elements[grid_coords].background_color=[0.6,0.6,0.6,1]


            if el.enable_events:
                self.elements[grid_coords].bind(
                    text=self._general_event)
        elif el.eltype == 'pb':
            from kivy.uix.progressbar import ProgressBar
            self.elements[grid_coords] = ProgressBar(max=el.max_value,value=el.value,
                size_hint=el.size_hint
                )
        elif el.eltype == 'slider':
            from kivy.uix.slider import Slider
            self.elements[grid_coords] = Slider(min=el.min_value,max=el.max_value,value=el.value,
                orientation=el.orientation,
                cursor_size=el.cursor_size,
                size_hint=el.size_hint
                )
        elif el.eltype == 'vdp':
            from kivy.uix.videoplayer import VideoPlayer
            self.elements[grid_coords] = VideoPlayer(source=el.source,options=el.options,state=el.state,
                size_hint=el.size_hint
                )
        elif el.eltype == 'video':
            from kivy.uix.videoplayer import Video
            self.elements[grid_coords] = Video(source=el.source,state=el.state,options=el.options,
                size_hint=el.size_hint
                )
            # self.elements[grid_coords].bind(position=self._general_event)
        elif el.eltype == 'void':
            self.elements[grid_coords] = Label(text='',size_hint=el.size_hint)
        elif el.eltype == 'box':
            from kivy.uix.boxlayout import BoxLayout
            self.elements[grid_coords] = BoxLayout(size_hint=el.size_hint)
        elif el.eltype == 'img':
            if el.async_load:
                from kivy.uix.image import AsyncImage
                self.elements[grid_coords] = AsyncImage(source=el.source,size_hint=el.size_hint)
            else:
                from kivy.uix.image import Image
                self.elements[grid_coords] = Image(source=el.source,size_hint=el.size_hint)
        elif el.eltype == 'switch':
            from kivy.uix.switch import Switch
            self.elements[grid_coords] = Switch(active=el.active,size_hint=el.size_hint)
            if el.enable_events:
                self.elements[grid_coords].bind(
                    active=self._general_event)
        elif el.eltype == 'checkbox':
            from kivy.uix.checkbox import CheckBox
            self.elements[grid_coords] = CheckBox(active=el.active,size_hint=el.size_hint)
            if el.group_id:
                self.elements[grid_coords].group=el.group_id
            if el.enable_events:
                self.elements[grid_coords].bind(active=self._general_event)

        elif el.eltype == 'subl':
            self.elements[grid_coords] = self._process_sublayout(grid_coords,el)
        elif el.eltype == 'tabgroup':
            from kivy.uix.tabbedpanel import TabbedPanel,TabbedPanelItem

            self.elements[grid_coords]=TabbedPanel(do_default_tab= False,tab_pos = el.tabs_position,
                tab_height=el.tab_height,
                tab_width=el.tab_width
                )
            
            c=-1
            for tabitem in el.tab_items:
                c+=1
                try:
                    tabhead=el.tab_headers[c]
                except:
                    tabhead='Tab'+str(c)
                tab_kivy=TabbedPanelItem(text=tabhead)
                new_coords=tuple([c for c in grid_coords]+['tab'+str(c)])
                tab_kivy.add_widget(self._process_sublayout(new_coords,tabitem))
                self.elements[grid_coords].add_widget(tab_kivy)
            if el.enable_events:
                self.elements[grid_coords].bind(current_tab=self._general_event)
        elif el.eltype == 'screens':
            from kivy.uix.screenmanager import ScreenManager, Screen
            self.elements[grid_coords]=ScreenManager()
            if el.transition!='Slide':
                transition=el.transition+'Transition'
                exec('from kivy.uix.screenmanager import '+transition+' as new_transition',globals())
                self.elements[grid_coords].transition=new_transition()

            
            c=-1
            for tabitem in el.screen_list:
                c+=1
                try:
                    tabhead=el.screen_names[c]
                except:
                    tabhead='Screen'+str(c)
                print(tabhead)
                tab_kivy=Screen(name=tabhead)
                new_coords=tuple([c for c in grid_coords]+['screen'+str(c)])
                tab_kivy.add_widget(self._process_sublayout(new_coords,tabitem))
                self.elements[grid_coords].add_widget(tab_kivy)
            # if el.enable_events:
            #     self.elements[grid_coords].bind(current_tab=self._general_event)


        # Assign a key 
        if el.eltype is 'btn' and not el.key and el.text:
                el.key = el.text
        if not el.key:
            el.key = grid_coords

        if not self.allow_repeated_keys:
            while el.key in self._by_key:
                el.key=el.key+'-'

        if el.eltype is 'menubar':
            self.keys[self.has_appmenu] = el.key
            self.by_key[el.key] = self.has_appmenu
            self._by_key[el.key] = el
        else:
            self.keys[self.elements[grid_coords]] = el.key
            self.by_key[el.key] = self.elements[grid_coords]
            self._by_key[el.key] = el

        # self.add_widget(self.elements[grid_coords])
        try:
            if el.size[0]:
                self.elements[grid_coords].width=el.size[0]
            if el.size[1]:
                self.elements[grid_coords].height=el.size[1]
        except:
            pass

        return self.elements[grid_coords]


    def _general_event(self, instance, value):
        self.trigger_event(instance)

    def trigger_event(self, event):
        # print('event',event)
        # print('key',self.keys[event])
        for key in self.by_key:
            if self._by_key[key].eltype in ['input', 'spinner']:
                self.values[key] = self.by_key[key].text
            elif self._by_key[key].eltype in ['switch']:
                self.values[key] = self.by_key[key].active
            elif self._by_key[key].eltype in ['tabgroup']:
                self.values[key] = self.by_key[key].current_tab.text
            elif self._by_key[key].eltype in ['screens']:
                self.values[key] = self.by_key[key].current

        if self.event_manager:
            # if event is self.event_start_key or type(event) is str:# and event in self.by_key:
            if type(event) is str:
                self.event_manager(self, event, self.values)            
            else:
                self.event_manager(self, self.keys[event], self.values)

            # try:
            #     self.event_manager(self, self.keys[event], self.values)
            
            # except Exception as error:
            #     print('¡¡¡### Error ###!!!')
            #     print(error)
            #     print('¡¡¡### Error ###!!!')
            #     self.event_manager(self, event, self.values)

            # if from_bind:
            #     self.event_manager(self, self.keys[event], self.values)

            # else:
            #     self.event_manager(self, event, self.values)

    def Resize(self, width, height):
        self.get_parent_window().size = (width, height)

    def UpdateTitle(self, title):
        self.get_parent_window().set_title(title)


class T:

    def __init__(self, text='', key=None,halign='center',valign='middle',background_color=(0,0,0,0),text_color=[1,1,1,1],
        size_hint=(1,1),
        size=(None,None),
        ):
        self.size=size
        if size[0]:
            size_hint=None,size_hint[1]
        if size[1]:
            size_hint=size_hint[0],None
        self.size_hint=size_hint

        self.text = text
        self.eltype = 'text'
        self.key = key
        self.halign=halign
        self.valign=valign
        if not background_color is None:
            self.background_color=background_color
        self.text_color=text_color

class T_markup:

    def __init__(self, text='', key=None,
        size_hint=(1,1),
        size=(None,None),
        ):
        self.size=size
        if size[0]:
            size_hint=None,size_hint[1]
        if size[1]:
            size_hint=size_hint[0],None
        self.size_hint=size_hint

        self.text = text
        self.eltype = 'rst'
        self.key = key


class B:

    def __init__(self, button_text='', key=None,
        size_hint=(1,1),
        size=(None,None),
        ):
        self.size=size
        if size[0]:
            size_hint=None,size_hint[1]
        if size[1]:
            size_hint=size_hint[0],None
        self.size_hint=size_hint

        self.text = button_text
        self.eltype = 'btn'
        self.key = key


class Void:

    def __init__(self,
        size_hint=(1,1),
        size=(None,None),
        ):
        self.size=size
        if size[0]:
            size_hint=None,size_hint[1]
        if size[1]:
            size_hint=size_hint[0],None
        self.size_hint=size_hint
        self.eltype = 'void'
        self.key = None

class In:

    def __init__(self, text='', password=False, key=None, multiline=False,enable_events=False,use_bubble=False,
        use_handles=False,
        write_tab=False,
        size_hint=(1,1),
        size=(None,None),
        ):
        self.size=size
        if size[0]:
            size_hint=None,size_hint[1]
        if size[1]:
            size_hint=size_hint[0],None
        self.size_hint=size_hint

        self.text = text
        self.eltype = 'input'
        self.password = password
        self.key = key
        self.multiline = multiline
        self.use_bubble=use_bubble
        self.enable_events = enable_events
        self.use_handles=use_handles
        self.write_tab=write_tab


class Multiline:

    def __init__(self, text='', password=False, key=None, multiline=True,enable_events=False,use_bubble=False,
        use_handles=False,
        write_tab=True,
        size_hint=(1,1),
        size=(None,None),
        ):
        self.size=size
        if size[0]:
            size_hint=None,size_hint[1]
        if size[1]:
            size_hint=size_hint[0],None
        self.size_hint=size_hint

        self.text = text
        self.eltype = 'input'
        self.password = password
        self.key = key
        self.multiline = multiline
        self.enable_events = enable_events
        self.use_bubble=use_bubble
        self.use_handles=use_handles
        self.write_tab=write_tab


class Spinner:

    def __init__(self, values=['...','choice0','choice1'], default_value='...', key=None, enable_events=False,
        size_hint=(1,1),
        size=(None,None),
        ):
        self.size=size
        if size[0]:
            size_hint=None,size_hint[1]
        if size[1]:
            size_hint=size_hint[0],None
        self.size_hint=size_hint

        self.eltype = 'spinner'
        self.key = key
        self.default_value = default_value
        self.values = values
        self.enable_events = enable_events


class PB:

    def __init__(self, max_value=100, value=0, key=None,
        size_hint=(1,1),
        size=(None,None),
        ):
        self.size=size
        if size[0]:
            size_hint=None,size_hint[1]
        if size[1]:
            size_hint=size_hint[0],None
        self.size_hint=size_hint

        self.eltype = 'pb'
        self.max_value = max_value
        self.value = value
        self.key = key

class VDP:
    def __init__(self, source='', state='stop',key=None,
    options={'allow_stretch': True},
    size_hint=(1,1),
        size=(None,None),
        ):
        self.size=size
        if size[0]:
            size_hint=None,size_hint[1]
        if size[1]:
            size_hint=size_hint[0],None
        self.size_hint=size_hint

        self.eltype = 'vdp'
        self.source = source
        self.state = state
        self.options=options
        self.key = key

class Video_element:
    def __init__(self, source='', state='stop',key=None,
    options={'allow_stretch': True},
    size_hint=(1,1),
        size=(None,None),
        ):
        self.size=size
        if size[0]:
            size_hint=None,size_hint[1]
        if size[1]:
            size_hint=size_hint[0],None
        self.size_hint=size_hint

        self.eltype = 'video'
        self.source = source
        self.state = state
        self.options=options
        self.key = key

class Sublayout:
    def __init__(self, layout=None,key=None,
        size_hint=(1,1),
        size=(None,None),
        padding=[0,0,0,0],
        ):
        self.size=size
        if size[0]:
            size_hint=None,size_hint[1]
        if size[1]:
            size_hint=size_hint[0],None
        self.size_hint=size_hint

        self.layout=layout
        self.eltype='subl'
        self.key = key
        self.padding=padding


class Window(App):

    def __init__(self, title='App Title', layout=None, event_manager=None,
                 size=(None, None),
                 resizable=True,
                 no_titlebar=False,
                 fullscreen=False,
                 allow_repeated_keys=False,
                 padding=[0,0,0,0],
                 exit_on_escape=True,
                 location=(None,None),
                 rotation=[0,90,180,270][0],
                 start_maximized=False,
                 start_minimized=False,
                 show_cursor=True,
                 **kwargs):
        super(Window, self).__init__(**kwargs)

        self.title = title
        self.layout = layout
        self.event_manager = event_manager
        self.allow_repeated_keys=allow_repeated_keys
        self.padding=padding
        self.Run=self.run
        
        # Config.set('graphics', 'borderless', no_titlebar)
        # Config.set('graphics', 'fullscreen', 'fake')
        # Config.write()

        from kivy.config import Config
        if size[0]:
            Config.set('graphics', 'width', size[0])
        if size[1]:
            Config.set('graphics', 'height', size[1])

        if location[0]!= None and location[1]!= None:
            Config.set('graphics', 'position', 'custom')
            Config.set('graphics', 'left', location[0])
            Config.set('graphics', 'top', location[1])
        Config.set('graphics', 'rotation', rotation)

        if fullscreen:
            Config.set('graphics', 'fullscreen', 'auto')

        Config.set('kivy', 'exit_on_escape', int(exit_on_escape))
        Config.set('graphics', 'resizable', int(resizable))
        if start_maximized:
            Config.set('graphics', 'window_state', 'maximized')
        if start_minimized:
            Config.set('graphics', 'window_state', 'minimized')
        if not show_cursor:
            Config.set('graphics', 'show_cursor', 0)
        from kivy.core.window import Window as kvWindow
        kvWindow.borderless = no_titlebar

        self.app=Layout(self.layout, self.event_manager,self.allow_repeated_keys,self.padding)
    def _general_event(self,value):
        self.app.trigger_event(value)

    def Close(self):
        self.get_running_app().stop()


    def build(self):
        if self.app.has_appmenu:
            from kivy.uix.floatlayout import FloatLayout
            self.with_menu=FloatLayout()
            self.app.pos=(0,0)
            self.with_menu.add_widget(self.app)
            self.with_menu.add_widget(self.app.has_appmenu)
            return self.with_menu
        return  self.app




class Switch:

    def __init__(self,active=False,key=None,
        size_hint=(1,1),
        enable_events=False,
        size=(None,None),
        ):
        self.size=size
        if size[0]:
            size_hint=None,size_hint[1]
        if size[1]:
            size_hint=size_hint[0],None
        self.size_hint=size_hint
        self.enable_events=enable_events
        self.eltype = 'switch'
        self.key = key
        self.active=active

class CheckBox:

    def __init__(self,active=False,key=None,group_id=None,
        size_hint=(1,1),
        enable_events=False,
        size=(None,None),
        ):
        self.size=size
        if size[0]:
            size_hint=None,size_hint[1]
        if size[1]:
            size_hint=size_hint[0],None
        self.size_hint=size_hint
        self.enable_events=enable_events
        self.eltype = 'checkbox'
        self.key = key
        self.active=active
        self.group_id=group_id

class TabPannel:

    def __init__(self,tab_items=[],tab_headers=[],tabs_position='top_left',tab_size=(None,None),
        key=None,
        size_hint=(1,1),
        enable_events=False,
        size=(None,None),
        ):
        self.size=size
        if size[0]:
            size_hint=None,size_hint[1]
        if size[1]:
            size_hint=size_hint[0],None
        self.size_hint=size_hint
        self.enable_events=enable_events
        self.eltype = 'tabgroup'
        self.key = key
        self.tab_items=tab_items
        self.tab_headers=tab_headers
        self.tabs_position=tabs_position

        tab_width, tab_height=100,40

        if tab_size[0]:
            tab_width=tab_size[0]
        if tab_size[1]:
            tab_height=tab_size[1]


        self.tab_height=tab_height
        self.tab_width=tab_width

class Slider:

    def __init__(self,min_value=0, max_value=100, value=0, key=None,
        cursor_size=(32,32),
        orientation='horizontal',
        size_hint=(1,1),
        size=(None,None),
        ):
        self.size=size
        if size[0]:
            size_hint=None,size_hint[1]
        if size[1]:
            size_hint=size_hint[0],None
        self.size_hint=size_hint

        self.eltype = 'slider'
        self.max_value = max_value
        self.min_value = min_value
        self.value = value
        self.key = key
        self.cursor_size=cursor_size
        self.orientation=orientation

class MenuBar:

    def __init__(self,menu_def={
    'File':{
        'New':None,
        'Recent':{'file1':None,'file2':None},
        '---':None,
        'Exit':None},
    'Tools':{},
    'Help':{
        'Support':'disabled',
        'About':None,
        'Extras':{'extra1':None,'extra2':None}},
},
        key=None,
        size_hint=(1,1),
        size=[None,None],
        ):
        if not size[1]:
            size[1]=30
        self.size=size
        if size[0]:
            size_hint=None,size_hint[1]
        if size[1]:
            size_hint=size_hint[0],None
        self.size_hint=size_hint
        self.eltype = 'menubar'
        self.key = key
        self.menu_def=menu_def

class Screen_Manager:
    def __init__(self,screen_list=[],screen_names=[],transition='Slide',
        transition_list=['No','Slide','Card','Swap','Fade','Wipe',
        'FallOut','RiseIn'],
        key=None,
        size_hint=(1,1),
        enable_events=False,
        size=(None,None),
        ):
        self.size=size
        if size[0]:
            size_hint=None,size_hint[1]
        if size[1]:
            size_hint=size_hint[0],None
        self.size_hint=size_hint
        self.enable_events=enable_events
        self.eltype = 'screens'
        self.key = key
        self.screen_list=screen_list
        self.screen_names=screen_names
        self.transition=transition
        self.transition_list=transition_list

class Box:
    def __init__(self,key=None,
        size_hint=(1,1),
        enable_events=False,
        size=(None,None),
        ):
        self.size=size
        if size[0]:
            size_hint=None,size_hint[1]
        if size[1]:
            size_hint=size_hint[0],None
        self.size_hint=size_hint
        self.enable_events=enable_events
        self.eltype = 'box'
        self.key = key
class Image:
    def __init__(self,source='',async_load=False,
        key=None,
        size_hint=(1,1),
        enable_events=False,
        size=(None,None),
        ):
        self.size=size
        if size[0]:
            size_hint=None,size_hint[1]
        if size[1]:
            size_hint=size_hint[0],None
        self.size_hint=size_hint
        self.enable_events=enable_events
        self.eltype = 'img'
        self.key = key
        self.source=source
        self.async_load=async_load

# import PySimpleGUI as sg
# sg.MenuBar

# Element Alternate names
Column=Sublayout
Text=T
Button=B
InputText=In