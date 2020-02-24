# import kivy
# print(kivy.kivy_options["video"])
# import sys
import platform
# from kivy.uix.videoplayer import VideoPlayer
import os
# os.environ['KIVY_VIDEO'] = 'ffmpeg'
os.environ['KIVY_VIDEO'] = 'gstplayer'
os.environ['GST_REGISTRY'] = './temp/registry.bin'

from kivy.app import App as _App
from kivy.uix.gridlayout import GridLayout as _GridLayout
import win32gui
import win32con
# from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.stacklayout import StackLayout
# from kivy.base import EventLoop
# from kivy.network.urlrequest import UrlRequest
# from kivy.uix.slider import Slider
# from kivy.clock import Clock
from kivy.uix.label import Label as _Label
from kivy.lang import Builder as _Builder
from kivy.properties import ListProperty as _ListProperty
from kivy.factory import Factory as _Factory


class CaseInsensitiveDict(dict):

    @classmethod
    def _k(cls, key):
        return key.lower() if isinstance(key, str) else key

    def __init__(self, *args, **kwargs):
        super(CaseInsensitiveDict, self).__init__(*args, **kwargs)
        self._convert_keys()

    def __getitem__(self, key):
        return super(CaseInsensitiveDict, self).__getitem__(self.__class__._k(key))

    def __setitem__(self, key, value):
        super(CaseInsensitiveDict, self).__setitem__(
            self.__class__._k(key), value)

    def __delitem__(self, key):
        return super(CaseInsensitiveDict, self).__delitem__(self.__class__._k(key))

    def __contains__(self, key):
        return super(CaseInsensitiveDict, self).__contains__(self.__class__._k(key))

    def has_key(self, key):
        return super(CaseInsensitiveDict, self).has_key(self.__class__._k(key))

    def pop(self, key, *args, **kwargs):
        return super(CaseInsensitiveDict, self).pop(self.__class__._k(key), *args, **kwargs)

    def get(self, key, *args, **kwargs):
        return super(CaseInsensitiveDict, self).get(self.__class__._k(key), *args, **kwargs)

    def setdefault(self, key, *args, **kwargs):
        return super(CaseInsensitiveDict, self).setdefault(self.__class__._k(key), *args, **kwargs)

    def update(self, E={}, **F):
        super(CaseInsensitiveDict, self).update(self.__class__(E))
        super(CaseInsensitiveDict, self).update(self.__class__(**F))

    def _convert_keys(self):
        for k in list(self.keys()):
            v = super(CaseInsensitiveDict, self).pop(k)
            self.__setitem__(k, v)


Colors = CaseInsensitiveDict({'clear': (0, 0, 0, 0), 'b': (0, 0, 1, 1), 'g': (0, 0.5, 0, 1), 'r': (1, 0, 0, 1), 'c': (0, 0.75, 0.75, 1), 'm': (0.75, 0, 0.75, 1), 'y': (0.75, 0.75, 0, 1), 'k': (0, 0, 0, 1), 'w': (1, 1, 1, 1), 'aliceblue': (0.9411764705882353, 0.9725490196078431, 1.0, 1.0), 'antiquewhite': (0.9803921568627451, 0.9215686274509803, 0.8431372549019608, 1.0), 'aqua': (0.0, 1.0, 1.0, 1.0), 'aquamarine': (0.4980392156862745, 1.0, 0.8313725490196079, 1.0), 'azure': (0.9411764705882353, 1.0, 1.0, 1.0), 'beige': (0.9607843137254902, 0.9607843137254902, 0.8627450980392157, 1.0), 'bisque': (1.0, 0.8941176470588236, 0.7686274509803922, 1.0), 'black': (0.0, 0.0, 0.0, 1.0), 'blanchedalmond': (1.0, 0.9215686274509803, 0.803921568627451, 1.0), 'blue': (0.0, 0.0, 1.0, 1.0), 'blueviolet': (0.5411764705882353, 0.16862745098039217, 0.8862745098039215, 1.0), 'brown': (0.6470588235294118, 0.16470588235294117, 0.16470588235294117, 1.0), 'burlywood': (0.8705882352941177, 0.7215686274509804, 0.5294117647058824, 1.0), 'cadetblue': (0.37254901960784315, 0.6196078431372549, 0.6274509803921569, 1.0), 'chartreuse': (0.4980392156862745, 1.0, 0.0, 1.0), 'chocolate': (0.8235294117647058, 0.4117647058823529, 0.11764705882352941, 1.0), 'coral': (1.0, 0.4980392156862745, 0.3137254901960784, 1.0), 'cornflowerblue': (0.39215686274509803, 0.5843137254901961, 0.9294117647058824, 1.0), 'cornsilk': (1.0, 0.9725490196078431, 0.8627450980392157, 1.0), 'crimson': (0.8627450980392157, 0.0784313725490196, 0.23529411764705882, 1.0), 'cyan': (0.0, 1.0, 1.0, 1.0), 'darkblue': (0.0, 0.0, 0.5450980392156862, 1.0), 'darkcyan': (0.0, 0.5450980392156862, 0.5450980392156862, 1.0), 'darkgoldenrod': (0.7215686274509804, 0.5254901960784314, 0.043137254901960784, 1.0), 'darkgray': (0.6627450980392157, 0.6627450980392157, 0.6627450980392157, 1.0), 'darkgreen': (0.0, 0.39215686274509803, 0.0, 1.0), 'darkgrey': (0.6627450980392157, 0.6627450980392157, 0.6627450980392157, 1.0), 'darkkhaki': (0.7411764705882353, 0.7176470588235294, 0.4196078431372549, 1.0), 'darkmagenta': (0.5450980392156862, 0.0, 0.5450980392156862, 1.0), 'darkolivegreen': (0.3333333333333333, 0.4196078431372549, 0.1843137254901961, 1.0), 'darkorange': (1.0, 0.5490196078431373, 0.0, 1.0), 'darkorchid': (0.6, 0.19607843137254902, 0.8, 1.0), 'darkred': (0.5450980392156862, 0.0, 0.0, 1.0), 'darksalmon': (0.9137254901960784, 0.5882352941176471, 0.47843137254901963, 1.0), 'darkseagreen': (0.5607843137254902, 0.7372549019607844, 0.5607843137254902, 1.0), 'darkslateblue': (0.2823529411764706, 0.23921568627450981, 0.5450980392156862, 1.0), 'darkslategray': (0.1843137254901961, 0.30980392156862746, 0.30980392156862746, 1.0), 'darkslategrey': (0.1843137254901961, 0.30980392156862746, 0.30980392156862746, 1.0), 'darkturquoise': (0.0, 0.807843137254902, 0.8196078431372549, 1.0), 'darkviolet': (0.5803921568627451, 0.0, 0.8274509803921568, 1.0), 'deeppink': (1.0, 0.0784313725490196, 0.5764705882352941, 1.0), 'deepskyblue': (0.0, 0.7490196078431373, 1.0, 1.0), 'dimgray': (0.4117647058823529, 0.4117647058823529, 0.4117647058823529, 1.0), 'dimgrey': (0.4117647058823529, 0.4117647058823529, 0.4117647058823529, 1.0), 'dodgerblue': (0.11764705882352941, 0.5647058823529412, 1.0, 1.0), 'firebrick': (0.6980392156862745, 0.13333333333333333, 0.13333333333333333, 1.0), 'floralwhite': (1.0, 0.9803921568627451, 0.9411764705882353, 1.0), 'forestgreen': (0.13333333333333333, 0.5450980392156862, 0.13333333333333333, 1.0), 'fuchsia': (1.0, 0.0, 1.0, 1.0), 'gainsboro': (0.8627450980392157, 0.8627450980392157, 0.8627450980392157, 1.0), 'ghostwhite': (0.9725490196078431, 0.9725490196078431, 1.0, 1.0), 'gold': (1.0, 0.8431372549019608, 0.0, 1.0), 'goldenrod': (0.8549019607843137, 0.6470588235294118, 0.12549019607843137, 1.0), 'gray': (0.5019607843137255, 0.5019607843137255, 0.5019607843137255, 1.0), 'green': (0.0, 0.5019607843137255, 0.0, 1.0), 'greenyellow': (0.6784313725490196, 1.0, 0.1843137254901961, 1.0), 'grey': (0.5019607843137255, 0.5019607843137255, 0.5019607843137255, 1.0), 'honeydew': (0.9411764705882353, 1.0, 0.9411764705882353, 1.0), 'hotpink': (1.0, 0.4117647058823529, 0.7058823529411765, 1.0), 'indianred': (0.803921568627451, 0.3607843137254902, 0.3607843137254902, 1.0), 'indigo': (0.29411764705882354, 0.0, 0.5098039215686274, 1.0), 'ivory': (1.0, 1.0, 0.9411764705882353, 1.0), 'khaki': (0.9411764705882353, 0.9019607843137255, 0.5490196078431373, 1.0), 'lavender': (0.9019607843137255, 0.9019607843137255, 0.9803921568627451, 1.0), 'lavenderblush': (1.0, 0.9411764705882353, 0.9607843137254902, 1.0), 'lawngreen': (0.48627450980392156, 0.9882352941176471, 0.0, 1.0), 'lemonchiffon': (1.0, 0.9803921568627451, 0.803921568627451, 1.0), 'lightblue': (0.6784313725490196, 0.8470588235294118, 0.9019607843137255, 1.0), 'lightcoral': (0.9411764705882353, 0.5019607843137255, 0.5019607843137255, 1.0), 'lightcyan': (0.8784313725490196, 1.0, 1.0, 1.0), 'lightgoldenrodyellow': (0.9803921568627451, 0.9803921568627451, 0.8235294117647058, 1.0), 'lightgray': (0.8274509803921568, 0.8274509803921568, 0.8274509803921568, 1.0), 'lightgreen': (0.5647058823529412, 0.9333333333333333, 0.5647058823529412, 1.0), 'lightgrey': (0.8274509803921568,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    0.8274509803921568, 0.8274509803921568, 1.0), 'lightpink': (1.0, 0.7137254901960784, 0.7568627450980392, 1.0), 'lightsalmon': (1.0, 0.6274509803921569, 0.47843137254901963, 1.0), 'lightseagreen': (0.12549019607843137, 0.6980392156862745, 0.6666666666666666, 1.0), 'lightskyblue': (0.5294117647058824, 0.807843137254902, 0.9803921568627451, 1.0), 'lightslategray': (0.4666666666666667, 0.5333333333333333, 0.6, 1.0), 'lightslategrey': (0.4666666666666667, 0.5333333333333333, 0.6, 1.0), 'lightsteelblue': (0.6901960784313725, 0.7686274509803922, 0.8705882352941177, 1.0), 'lightyellow': (1.0, 1.0, 0.8784313725490196, 1.0), 'lime': (0.0, 1.0, 0.0, 1.0), 'limegreen': (0.19607843137254902, 0.803921568627451, 0.19607843137254902, 1.0), 'linen': (0.9803921568627451, 0.9411764705882353, 0.9019607843137255, 1.0), 'magenta': (1.0, 0.0, 1.0, 1.0), 'maroon': (0.5019607843137255, 0.0, 0.0, 1.0), 'mediumaquamarine': (0.4, 0.803921568627451, 0.6666666666666666, 1.0), 'mediumblue': (0.0, 0.0, 0.803921568627451, 1.0), 'mediumorchid': (0.7294117647058823, 0.3333333333333333, 0.8274509803921568, 1.0), 'mediumpurple': (0.5764705882352941, 0.4392156862745098, 0.8588235294117647, 1.0), 'mediumseagreen': (0.23529411764705882, 0.7019607843137254, 0.44313725490196076, 1.0), 'mediumslateblue': (0.4823529411764706, 0.40784313725490196, 0.9333333333333333, 1.0), 'mediumspringgreen': (0.0, 0.9803921568627451, 0.6039215686274509, 1.0), 'mediumturquoise': (0.2823529411764706, 0.8196078431372549, 0.8, 1.0), 'mediumvioletred': (0.7803921568627451, 0.08235294117647059, 0.5215686274509804, 1.0), 'midnightblue': (0.09803921568627451, 0.09803921568627451, 0.4392156862745098, 1.0), 'mintcream': (0.9607843137254902, 1.0, 0.9803921568627451, 1.0), 'mistyrose': (1.0, 0.8941176470588236, 0.8823529411764706, 1.0), 'moccasin': (1.0, 0.8941176470588236, 0.7098039215686275, 1.0), 'navajowhite': (1.0, 0.8705882352941177, 0.6784313725490196, 1.0), 'navy': (0.0, 0.0, 0.5019607843137255, 1.0), 'oldlace': (0.9921568627450981, 0.9607843137254902, 0.9019607843137255, 1.0), 'olive': (0.5019607843137255, 0.5019607843137255, 0.0, 1.0), 'olivedrab': (0.4196078431372549, 0.5568627450980392, 0.13725490196078433, 1.0), 'orange': (1.0, 0.6470588235294118, 0.0, 1.0), 'orangered': (1.0, 0.27058823529411763, 0.0, 1.0), 'orchid': (0.8549019607843137, 0.4392156862745098, 0.8392156862745098, 1.0), 'palegoldenrod': (0.9333333333333333, 0.9098039215686274, 0.6666666666666666, 1.0), 'palegreen': (0.596078431372549, 0.984313725490196, 0.596078431372549, 1.0), 'paleturquoise': (0.6862745098039216, 0.9333333333333333, 0.9333333333333333, 1.0), 'palevioletred': (0.8588235294117647, 0.4392156862745098, 0.5764705882352941, 1.0), 'papayawhip': (1.0, 0.9372549019607843, 0.8352941176470589, 1.0), 'peachpuff': (1.0, 0.8549019607843137, 0.7254901960784313, 1.0), 'peru': (0.803921568627451, 0.5215686274509804, 0.24705882352941178, 1.0), 'pink': (1.0, 0.7529411764705882, 0.796078431372549, 1.0), 'plum': (0.8666666666666667, 0.6274509803921569, 0.8666666666666667, 1.0), 'powderblue': (0.6901960784313725, 0.8784313725490196, 0.9019607843137255, 1.0), 'purple': (0.5019607843137255, 0.0, 0.5019607843137255, 1.0), 'rebeccapurple': (0.4, 0.2, 0.6, 1.0), 'red': (1.0, 0.0, 0.0, 1.0), 'rosybrown': (0.7372549019607844, 0.5607843137254902, 0.5607843137254902, 1.0), 'royalblue': (0.2549019607843137, 0.4117647058823529, 0.8823529411764706, 1.0), 'saddlebrown': (0.5450980392156862, 0.27058823529411763, 0.07450980392156863, 1.0), 'salmon': (0.9803921568627451, 0.5019607843137255, 0.4470588235294118, 1.0), 'sandybrown': (0.9568627450980393, 0.6431372549019608, 0.3764705882352941, 1.0), 'seagreen': (0.1803921568627451, 0.5450980392156862, 0.3411764705882353, 1.0), 'seashell': (1.0, 0.9607843137254902, 0.9333333333333333, 1.0), 'sienna': (0.6274509803921569, 0.3215686274509804, 0.17647058823529413, 1.0), 'silver': (0.7529411764705882, 0.7529411764705882, 0.7529411764705882, 1.0), 'skyblue': (0.5294117647058824, 0.807843137254902, 0.9215686274509803, 1.0), 'slateblue': (0.41568627450980394, 0.35294117647058826, 0.803921568627451, 1.0), 'slategray': (0.4392156862745098, 0.5019607843137255, 0.5647058823529412, 1.0), 'slategrey': (0.4392156862745098, 0.5019607843137255, 0.5647058823529412, 1.0), 'snow': (1.0, 0.9803921568627451, 0.9803921568627451, 1.0), 'springgreen': (0.0, 1.0, 0.4980392156862745, 1.0), 'steelblue': (0.27450980392156865, 0.5098039215686274, 0.7058823529411765, 1.0), 'tan': (0.8235294117647058, 0.7058823529411765, 0.5490196078431373, 1.0), 'teal': (0.0, 0.5019607843137255, 0.5019607843137255, 1.0), 'thistle': (0.8470588235294118, 0.7490196078431373, 0.8470588235294118, 1.0), 'tomato': (1.0, 0.38823529411764707, 0.2784313725490196, 1.0), 'turquoise': (0.25098039215686274, 0.8784313725490196, 0.8156862745098039, 1.0), 'violet': (0.9333333333333333, 0.5098039215686274, 0.9333333333333333, 1.0), 'wheat': (0.9607843137254902, 0.8705882352941177, 0.7019607843137254, 1.0), 'white': (1.0, 1.0, 1.0, 1.0), 'whitesmoke': (0.9607843137254902, 0.9607843137254902, 0.9607843137254902, 1.0), 'yellow': (1.0, 1.0, 0.0, 1.0), 'yellowgreen': (0.6039215686274509, 0.803921568627451, 0.19607843137254902, 1.0)})
Fonts = CaseInsensitiveDict({
    'DejaVusans': 'DejaVuSans.ttf',
    'Roboto': 'Roboto-Regular.ttf',
    'Roboto it': 'Roboto-Italic.ttf',
    'Roboto b': 'Roboto-Bold.ttf',
    'Roboto itb': 'Roboto-BoldItalic.ttf',
    'Roboto bit': 'Roboto-BoldItalic.ttf',
    'Mono': 'RobotoMono-Regular.ttf',
})

TimeFormats = CaseInsensitiveDict({
    'DD': '%d',
    'MM': '%m',
    'YY': '%y',
    'YYYY': '%Y',
    'Mon': '%a',
    'Monday': '%A',
    'Sun': '%a',
    'Sunday': '%A',
    'Jan': '%b',
    'January': '%B',
    'sec': '%S',
    'min': '%M',
    'hour12': '%I',
    'hour24': '%H',
    'am': '%p',
    'a.m.': '%r',
    'time': '%X',
    'time12': '%I:%M %p',
    'time24': '%H:%M',
    'date': '%x',
    'timezone': '%Z',
    '12:00 AM': '%I:%M %p',
    '12:00:00 AM': '%I:%M:%S %p',
    '24:00': '%H:%M',
    '24:00:00': '%H:%M:%S',
    'MM/DD/YY': '%m/%d/%y',
    'MM/DD/YYYY': '%m/%d/%Y',
    'DD/MM/YY': '%d/%m/%y',
    'DD/MM/YYYY': '%d/%m//%Y'
})


def sum_str(*largs, sep='', end=''):
    ans = ''
    cm = len(largs)
    c = 0
    for l in largs:
        c += 1
        s = end if c == cm else sep
        ans += l + s
    return ans

# from kivy.uix.button import Button as _Button
# _Builder.load_string("""
# <_RoundedButton@Button>:
#     background_color: 0,0,0,0  # the last zero is the critical on, make invisible
#     canvas.before:
#         Color:
#             rgba: (.4,.4,.4,1) if self.state=='normal' else (0,.7,.7,1)  # visual feedback of press
#         RoundedRectangle:
#             pos: self.pos
#             size: self.size
#             radius: [50,]
# """)
# class _RoundedButton(_Button):
#     pass
# _Factory.register('KivyB', module='_RoundedButton')


_Builder.load_string("""
<_LabelB>:
  bcolor: 0, 0, 0, 0
  canvas.before:
    Color:
      rgba: self.bcolor
    Rectangle:
      pos: self.pos
      size: self.size
""")


class _LabelB(_Label):
    bcolor = _ListProperty([0, 0, 0, 0])
    pass
_Factory.register('KivyB', module='_LabelB')

# from kivy.uix.textinput import TextInput
# from kivy.properties import StringProperty

# DEFAULT_PADDING = 6

# class _AlignedTextInput(TextInput):

#     halign = StringProperty('left')
#     valign = StringProperty('top')

#     def __init__(self, **kwargs):
#         self.halign = kwargs.get("halign", "left")
#         self.valign = kwargs.get("valign", "top")

#         self.bind(on_text=self.on_text)

#         super().__init__(**kwargs)

#     def on_text(self, instance, value):
#         self.redraw()

#     def on_size(self, instance, value):
#         self.redraw()

#     def redraw(self):
#         """
#         Note: This methods depends on internal variables of its TextInput
#         base class (_lines_rects and _refresh_text())
#         """

#         self._refresh_text(self.text)

#         max_size = max(self._lines_rects, key=lambda r: r.size[0]).size
#         num_lines = len(self._lines_rects)

#         px = [DEFAULT_PADDING, DEFAULT_PADDING]
#         py = [DEFAULT_PADDING, DEFAULT_PADDING]

#         if self.halign == 'center':
#             d = (self.width - max_size[0]) / 2.0 - DEFAULT_PADDING
#             px = [d, d]
#         elif self.halign == 'right':
#             px[0] = self.width - max_size[0] - DEFAULT_PADDING

#         if self.valign == 'middle':
#             d = (self.height - max_size[1] * num_lines) / 2.0 - DEFAULT_PADDING
#             py = [d, d]
#         elif self.valign == 'bottom':
#             py[0] = self.height - max_size[1] * num_lines - DEFAULT_PADDING

#         self.padding_x = px
#         self.padding_y = py


def hex2rgb(hex, alpha=None, vmax=255):
    hex = hex.lstrip('#')
    rgb = list(int(hex[i:i + 2], 16) for i in (0, 2, 4))
    if not alpha is None:
        rgb.append(alpha)

    if vmax != 255:
        rgb = [c / 255 for c in rgb]

    return tuple(rgb)


def rgb2hex(rgb):
    if type(rgb) == tuple or type(rgb) == list and False not in[0 <= c <= 255 for c in rgb]:
        if len(rgb) == 3:
            hex_ = '#%02x%02x%02x' % tuple([int(i) for i in rgb])
        elif len(rgb) > 3:
            hex_ = '#%02x%02x%02x' % tuple([int(i) for i in rgb[0:3]])
        elif len(rgb) == 2:
            hex_ = '#%02x%02x00' % tuple([int(i) for i in rgb[0:2]])
        elif len(rgb) == 1:
            hex_ = '#%02x0000' % tuple(int(rgb))
    elif type(rgb) == int and 0 <= rgb <= 255:
        hex_ = '#%02x%02x%02x' % (rgb, rgb, rgb)
    else:
        hex_ = '#000000'
    return hex_


class Layout(_GridLayout):
    """docstring for ClassName"""

    def __init__(self, layout=None, event_manager=None, allow_repeated_keys=False, padding=[0, 0, 0, 0], **kwargs):
        super(Layout, self).__init__(**kwargs)

        self.keys = {}
        max_cols = 0
        for row in layout:
            if len(row) > max_cols:
                max_cols = len(row)

        self.cols = max_cols
        self.pos = 0, 0
        self.padding = padding
        self.allow_repeated_keys = allow_repeated_keys

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
        self._values_old = {}
        self.by_key = {}
        self._by_key = {}
        # self._cprops=['background_color','text_color','tab_text_color','tab_background_color']
        self._cprops = ['background_color', 'text_color',
                        'cursor_color', 'selection_color', 'font_name']
        self._tabcprops = ['tab_text_color', 'tab_background_color']
        self.add_at_the_end = {}
        self.event_counter = -1
        self.has_appmenu = False
        i = -1
        for row in layout:
            i += 1
            elnum = -1
            for el in row:
                elnum += 1
                # print(el.eltype, 'i:', i, ', j:', elnum, ', key:', el.key)
                kivy_el = self._process_element((i, elnum), el)
                self.add_widget(kivy_el)

            lenrow = len(row)
            addnvoids = 0
            if lenrow < max_cols:
                addnvoids = max_cols - lenrow
            for v in range(addnvoids):
                self.add_widget(_Label(text='', size_hint=el.size_hint))

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

    def Start(self, event_start_key='__Start__'):
        self.event_start_key = event_start_key
        self.trigger_event(event_start_key)

    def _process_sublayout(self, grid_coords, sublayout_element):
        sublayout = sublayout_element.layout
        max_cols = 0
        for row in sublayout:
            if len(row) > max_cols:
                max_cols = len(row)
        if sublayout_element.eltype == 'ssubl':
            kivy_sublayout = _GridLayout(cols=max_cols, size_hint=sublayout_element.content_size_hint,
                                         padding=sublayout_element.padding, spacing=sublayout_element.spacing)
        else:
            kivy_sublayout = _GridLayout(cols=max_cols, size_hint=sublayout_element.size_hint,
                                         padding=sublayout_element.padding, spacing=sublayout_element.spacing)
        i = -1
        for row in sublayout:
            i += 1
            elnum = -1
            for el in row:
                elnum += 1
                # print(el.eltype, 'i:', i, ', j:', elnum, ', key:', el.key)
                new_coords = tuple([c for c in grid_coords] + [i, elnum])
                kivy_el = self._process_element(new_coords, el)
                kivy_sublayout.add_widget(kivy_el)

            lenrow = len(row)
            addnvoids = 0
            if lenrow < max_cols:
                addnvoids = max_cols - lenrow
            for v in range(addnvoids):
                kivy_sublayout.add_widget(
                    Label(text='', size_hint=el.size_hint))

                # self.add_widget(Label(text='',size_hint=(None,el.size_hint[1]) ))
                # kivy_sublayout.add_widget(Label(text=''))
                pass

        return kivy_sublayout

    def _process_element(self, grid_coords, el):
        for p in self._cprops:
            try:
                if 'font' in p:
                    setattr(el, p, Fonts[getattr(el, p)])
                if type(getattr(el, p)) is str:
                    setattr(el, p, Colors[getattr(el, p)])
            except:
                pass
        if el.eltype == 'text':
            label = _LabelB(text=el.text, color=el.text_color, size_hint=el.size_hint, halign=el.halign, valign=el.valign, bcolor=el.background_color, markup=el.markup,
                            font_name=el.font_name,
                            font_size=el.font_size,
                            )
            label.bind(size=label.setter('text_size'))
            label.text_size = self.size
            self.elements[grid_coords] = label

        elif el.eltype == 'rst':
            from kivy.uix.rst import RstDocument
            self.elements[grid_coords] = RstDocument(
                text=el.text, size_hint=el.size_hint)
        elif el.eltype == 'kvel':
            self.elements[grid_coords] = el.kv_element
            el.kv_element.size_hint = el.size_hint
            if not type(el.event_bind[0]) is type:
                el.event_bind[0].bind(
                    **{el.event_bind[1]: lambda *largs: self.trigger_event(self.elements[grid_coords])}
                )
        elif el.eltype == 'watch':
            el.widget.size_hint = el.size_hint
            el.widget.size = el.size
            el.widget.key = el.key
            watch = self._process_element(None, el.widget)
            fmt = el.format if el.format not in TimeFormats else TimeFormats[
                el.format]

            def update(*largs):
                watch.text = time.strftime(fmt)
            import time
            from kivy.clock import Clock
            Clock.schedule_interval(update, 1)
            self.elements[grid_coords] = watch

            if el.event_bind != str:
                watch.bind(
                    **{el.event_bind: lambda *largs: self.trigger_event(self.elements[grid_coords])}
                )
            if el.value_bind != str:
                el.value_bind = watch, el.value_bind
            else:
                el.value_bind = object, el.value_bind

        elif el.eltype == 'combo':
            from kivy.uix.boxlayout import BoxLayout
            from kivy.uix.dropdown import DropDown

            class SpinnerDropdown(DropDown):

                def __init__(self, **kwargs):
                    super(SpinnerDropdown, self).__init__(**kwargs)
                    self.bar_color = hex2rgb('#403E3C', alpha=200, vmax=1)
                    self.bar_inactive_color = 0.4, 0.4, 0.6, 0.6
                    self.bar_width = 8
                    self.effect_cls = 'ScrollEffect'
                    self.scroll_type = ['bars', 'content']

            from kivy.uix.button import Button

            box = BoxLayout(size_hint=el.size_hint)
            if el.size[0]:
                box.width = el.size[0]
            if el.size[1]:
                box.height = el.size[1]
            text_val = self._process_element(None, el.input_text)
            text_val.disabled = el.disabled

            main_btn = self._process_element(None, el.main_button)
            # main_btn.font_name='DejaVuSans'
            # main_btn.size_hint_x=None
            # main_btn.size_width=30
            # main_btn.text=el.main_btn_text

            # dropdown = DropDown()
            dropdown = SpinnerDropdown()
            c = 0
            for v in el.values:
                # for v in range(30):
                c += 1
                bg = [.75, .75, .75, 1] if c % 2 else [1, 1, 1, 1]
                btn = Button(text=str(v),
                             color=[0, 0, 0, 1],
                             size_hint_y=None,
                             height=26,
                             background_color=bg,
                             background_normal='',
                             )

                btn.bind(on_release=lambda btn: dropdown.select(btn.text))
                dropdown.add_widget(btn)

            def open_dd(*largs):
                try:
                    # dropdown.open(text_val)
                    dropdown.open(box)
                except:
                    pass

            main_btn.disabled = el.disabled
            if el.read_only:
                text_val.disabled = True
            main_btn.bind(on_release=open_dd)

            dropdown.bind(on_select=lambda instance,
                          x: setattr(text_val, 'text', x))
            if el.enable_events:
                text_val.bind(
                    text=lambda *largs: self.trigger_event(
                        self.elements[grid_coords])
                )

            box.add_widget(
                text_val
            )
            box.add_widget(
                main_btn
            )

            self.elements[grid_coords] = box
            el.value_bind = text_val, 'text'
            # if not type(el.event_bind[0]) is type:
            #     el.event_bind[0].bind(
            #         **{el.event_bind[1]:lambda *largs:self.trigger_event(self.elements[grid_coords])}
            #         )

        elif 'btn' in el.eltype:
            if el.eltype == 'tbtn':
                from kivy.uix.togglebutton import ToggleButton as kvButton
                el.key = el.text if not el.key else el.key
            else:
                from kivy.uix.button import Button as kvButton
            self.elements[grid_coords] = kvButton(
                # element = Button(
                text=el.button_text,
                color=el.text_color,
                markup=el.markup,
                disabled=el.disabled,
                background_color=el.background_color,
                background_normal=el.image_normal,
                background_down=el.image_pressed,
                background_disabled_normal=el.image_disabled_normal,
                background_disabled_down=el.image_disabled_pressed,


                # size_hint_x=None, width=40,
            )
            if el.eltype == 'tbtn' and el.group_id:
                self.elements[grid_coords].group = el.group_id
                self.elements[
                    grid_coords].state = 'down' if el.pressed else 'normal'
            if el.width:
                self.elements[grid_coords].size_hint_x = None
                self.elements[grid_coords].width = el.width
            if el.height:
                self.elements[grid_coords].size_hint_y = None
                self.elements[grid_coords].height = el.height
            if el.font_name:
                self.elements[grid_coords].font_name = el.font_name
            if el.enable_events and grid_coords:
                self.elements[grid_coords].bind(on_release=self.trigger_event)
                # element.bind(on_release=self.trigger_event)

        elif el.eltype == 'menubar':
            if not el.key:
                el.key = grid_coords
            import kivy_garden.contextmenu
            menu_kv = ''
            tab = '    '
            self.elements['aux_menu_void'] = Label(
                text='', size_hint=el.size_hint)
            self.elements[grid_coords] = self.elements['aux_menu_void']
            menu_kv = ['''
AnchorLayout:
    anchor_y: 'top'
    # padding: app._menu_pos()
    height: ''' + str(el.size[1]) + '''
    id: layout
    AppMenu:
        id: app_menu
        top: root.height
        cancel_handler_widget: layout
''']

            def _fix_menu(kv):
                newkv = kv.split('\n')
                skv = ''
                lkv = len(newkv)
                for i in range(lkv):
                    if i + 1 < lkv and 'ContextMenu:' in newkv[i] and not 'ContextMenuTextItem' in newkv[i + 1]:
                        continue
                    skv += newkv[i] + '\n'

                return skv
            # csub=[0]

            def _creat_submenu(data, level=1, parent='no_parent', parent_level=1, tab='    '):
                if type(data) is dict:
                    for item in data:
                        if type(data[item]) is dict:
                            if level == 1:
                                menu_kv[0] += tab * 2 + 'AppMenuTextItem:\n'
                                menu_kv[0] += tab * 2 + tab * \
                                    level + 'text: \"' + item + '\"\n'
                                menu_kv[0] += tab * 2 + level * \
                                    tab + 'ContextMenu:\n'
                                # menu_kv[0]+=tab*3+level*tab+'id: submenu'+str(csub[0])+'\n'
                                # csub[0]+=1
                            else:
                                menu_kv[0] += tab * 2 + level * \
                                    tab + 'ContextMenuTextItem:\n'
                                menu_kv[0] += tab * 3 + tab * \
                                    level + 'text: \"' + item + '\"\n'
                                menu_kv[0] += tab * 3 + level * \
                                    tab + 'ContextMenu: ##\n'
                                level += 1
                                # _creat_submenu(data[item],level+2,parent=item,parent_level=level,tab=tab)
                                # return
                            _creat_submenu(
                                data[item], level + 1, parent=item, parent_level=level, tab=tab)
                        else:
                            extra = tab
                            if level % 2:
                                extra = ''
                            if '---' == item:
                                menu_kv[0] += tab * 1 + level * tab + extra + \
                                    'ContextMenuDivider: #---------------\n'
                                continue
                            else:
                                menu_kv[0] += tab * 1 + level * tab + \
                                    extra + 'ContextMenuTextItem: #<--\n'
                                menu_kv[0] += tab * 2 + tab * level + \
                                    extra + 'text: \"' + item + '\"\n'
                            if data[item] is None:
                                menu_kv[0] += tab * 2 + tab * level + extra + \
                                    r"on_release: app._general_event('" + str(
                                        el.key) + r":'+self.text)" + '\n'
                                menu_kv[0] += tab * 2 + tab * level + extra + \
                                    r"on_release: app_menu.close_all()" + '\n'
                            elif 'disabled' in data[item]:
                                menu_kv[0] += tab * 2 + tab * level + \
                                    extra + r"color: 1,1,1,0.4" + '\n'

            _creat_submenu(el.menu_def)
            nkv = _fix_menu(menu_kv[0])
            # self.has_appmenu=Builder.load_string(kv)
            print(nkv)
            self.has_appmenu = Builder.load_string(nkv)

        elif el.eltype == 'input':
            from kivy.uix.textinput import TextInput
            self.elements[grid_coords] = TextInput(
                # self.elements[grid_coords] = _AlignedTextInput(
                # element = TextInput(
                text=el.text, multiline=el.multiline, password=el.password,
                size_hint=el.size_hint,
                use_bubble=el.use_bubble,
                use_handles=el.use_handles,
                write_tab=el.write_tab,
                disabled=el.disabled,
                hint_text=el.hint_text,
                halign=el.halign,

                foreground_color=el.text_color,
                background_color=el.background_color,
                cursor_color=el.cursor_color,
                font_name=el.font_name,
                font_size=el.font_size,
                selection_color=el.selection_color
            )
            if el.enable_events and grid_coords:
                self.elements[grid_coords].bind(
                    # element.bind(
                    text=self._general_event)
            text_val = self.elements[grid_coords]
            if el.valign == 'center':
                def center_align(*largs):
                    d0, d1, d2, d3, = text_val.padding  # DEFAULT_PADDING
                    num_lines = len(text_val._lines_rects)

                    d = (text_val.height - text_val.line_height *
                         num_lines) / 2.0 - (d1 + d3) / 2
                    setattr(text_val, 'padding', [d0, d, d2, d])
                text_val.bind(size=center_align)
            elif el.valign == 'bottom':
                def bottom_align(*largs):
                    d0, d1, d2, d3, = text_val.padding  # DEFAULT_PADDING
                    num_lines = len(text_val._lines_rects)
                    d = text_val.height - text_val.line_height * num_lines - d1
                    setattr(text_val, 'padding', [d0, d, d2, d3])
                text_val.bind(size=bottom_align)

            # elif el.valign=='bottom':
            #     # text_val.bind(size=lambda *largs: setattr(text_val,'padding', [0,49.5]))
        elif el.eltype == 'spinner':
            from kivy.uix.spinner import Spinner as kivySpinner
            self.elements[grid_coords] = kivySpinner(
                text=el.default_value, values=el.values,
                color=el.text_color,
                markup=el.markup,
                disabled=el.disabled,
                background_color=el.background_color,
                background_normal=el.image_normal,
                background_down=el.image_pressed,
                background_disabled_normal=el.image_disabled_normal,
                background_disabled_down=el.image_disabled_pressed,
            )

            from kivy.uix.spinner import SpinnerOption
            from kivy.uix.dropdown import DropDown

            class SpinnerOptions(SpinnerOption):

                def __init__(self, **kwargs):
                    super(SpinnerOptions, self).__init__(**kwargs)
                    self.background_normal = ''
                    # self.background_color = [0.9, 0.9, 0.9, 1]
                    self.background_color = [1, 1, 1, 1]
                    self.height = 26

                    # font_color
                    self.color = [0, 0, 0, 1]

            class SpinnerDropdown(DropDown):

                def __init__(self, **kwargs):
                    super(SpinnerDropdown, self).__init__(**kwargs)
                    # self.bar_inactive_color= hex2rgb('#141411',alpha=255)
                    self.bar_color = hex2rgb('#403E3C', alpha=200, vmax=1)
                    # self.bar_inactive_color=hex2rgb('#2A2B25',alpha=255,vmax=1)
                    self.bar_inactive_color = 0.4, 0.4, 0.6, 0.6
                    self.bar_width = 8
                    self.effect_cls = 'ScrollEffect'
                    self.scroll_type = ['bars', 'content']
                    # self.auto_width = False
                    # self.width = 150

            self.elements[grid_coords].dropdown_cls = SpinnerDropdown
            self.elements[grid_coords].option_cls = SpinnerOptions
            # self.elements[grid_coords].color=[0,0,0,1]
            # self.elements[grid_coords].background_normal=''
            # self.elements[grid_coords].background_color=[0.6,0.6,0.6,1]

            if el.enable_events:
                self.elements[grid_coords].bind(
                    text=self._general_event)
        elif el.eltype == 'pb':
            from kivy.uix.progressbar import ProgressBar
            self.elements[grid_coords] = ProgressBar(max=el.max_value, value=el.value,
                                                     size_hint=el.size_hint
                                                     )
        elif el.eltype == 'slider':
            from kivy.uix.slider import Slider
            self.elements[grid_coords] = Slider(min=el.min_value, max=el.max_value, value=el.value,
                                                orientation=el.orientation,
                                                cursor_size=el.cursor_size,
                                                size_hint=el.size_hint
                                                )
        elif el.eltype == 'vdp':
            from kivy.uix.videoplayer import VideoPlayer
            self.elements[grid_coords] = VideoPlayer(source=el.source, options=el.options, state=el.state,
                                                     size_hint=el.size_hint
                                                     )
        elif el.eltype == 'video':
            from kivy.uix.videoplayer import Video
            self.elements[grid_coords] = Video(source=el.source, state=el.state, options=el.options,
                                               size_hint=el.size_hint
                                               )
            # self.elements[grid_coords].bind(position=self._general_event)
        elif el.eltype == 'void':
            self.elements[grid_coords] = _Label(
                text='', size_hint=el.size_hint)
        elif el.eltype == 'box':
            from kivy.uix.boxlayout import BoxLayout
            self.elements[grid_coords] = BoxLayout(size_hint=el.size_hint)
        elif el.eltype == 'img':
            if el.async_load:
                from kivy.uix.image import AsyncImage
                self.elements[grid_coords] = AsyncImage(
                    source=el.source, size_hint=el.size_hint)
            else:
                from kivy.uix.image import Image
                self.elements[grid_coords] = Image(
                    source=el.source, size_hint=el.size_hint)
        elif el.eltype == 'switch':
            from kivy.uix.switch import Switch
            self.elements[grid_coords] = Switch(
                active=el.active, size_hint=el.size_hint)
            if el.enable_events:
                self.elements[grid_coords].bind(
                    active=self._general_event)
        elif el.eltype == 'checkbox':
            from kivy.uix.checkbox import CheckBox
            self.elements[grid_coords] = CheckBox(
                active=el.active, size_hint=el.size_hint)
            if el.group_id:
                self.elements[grid_coords].group = el.group_id
            if el.enable_events:
                self.elements[grid_coords].bind(active=self._general_event)

        elif el.eltype == 'subl':
            self.elements[grid_coords] = self._process_sublayout(
                grid_coords, el)
        elif el.eltype == 'ssubl':
            from kivy.uix.scrollview import ScrollView
            subl = self._process_sublayout(grid_coords, el)
            ssubl = ScrollView(
                size_hint=el.size_hint,
                do_scroll_x=el.scroll_x,
                do_scroll_y=el.scroll_y,

            )
            ssubl.add_widget(subl)
            if el.content_size[0]:
                subl.width = el.content_size[0]
            if el.content_size[1]:
                subl.height = el.content_size[1]
            self.elements[grid_coords] = ssubl
        elif el.eltype == 'tabgroup':
            for p in self._tabcprops:
                try:
                    getattr
                    if type(getattr(el, p)) is str:
                        setattr(el, p, Colors[getattr(el, p)])
                except:
                    pass
            from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem, TabbedPanelStrip

            self.elements[grid_coords] = TabbedPanel(do_default_tab=False, tab_pos=el.tabs_position,
                                                     tab_height=el.tab_height,
                                                     tab_width=el.tab_width,
                                                     background_color=el.background_color,
                                                     background_image=el.background_image,
                                                     # strip_background_color=[1,0,0,1]

                                                     # background_color=(0, 0,0,1),
                                                     # border = [1, 1, 1, 1],
                                                     # background_image = 'simplekivy_logo.png'
                                                     )

            c = -1
            for tabitem in el.tab_items:
                c += 1
                try:
                    tabhead = el.tab_headers[c]
                except:
                    tabhead = 'Tab' + str(c)
                tab_kivy = TabbedPanelItem(text=tabhead, background_color=el.tab_background_color,
                                           background_normal=el.tab_background_normal,
                                           color=el.tab_text_color)
                new_coords = tuple([c for c in grid_coords] + ['tab' + str(c)])
                tab_kivy.add_widget(
                    self._process_sublayout(new_coords, tabitem))
                self.elements[grid_coords].add_widget(tab_kivy)
            if el.enable_events:
                self.elements[grid_coords].bind(
                    current_tab=self._general_event)
        elif el.eltype == 'screens':
            from kivy.uix.screenmanager import ScreenManager, Screen
            self.elements[grid_coords] = ScreenManager()
            if el.transition != 'Slide':
                transition = el.transition + 'Transition'
                exec('from kivy.uix.screenmanager import ' +
                     transition + ' as new_transition', globals())
                self.elements[grid_coords].transition = new_transition()

            c = -1
            for tabitem in el.screen_list:
                c += 1
                try:
                    tabhead = el.screen_names[c]
                except:
                    tabhead = 'Screen' + str(c)
                print(tabhead)
                tab_kivy = Screen(name=tabhead)
                new_coords = tuple(
                    [c for c in grid_coords] + ['screen' + str(c)])
                tab_kivy.add_widget(
                    self._process_sublayout(new_coords, tabitem))
                self.elements[grid_coords].add_widget(tab_kivy)
            # if el.enable_events:
            #     self.elements[grid_coords].bind(current_tab=self._general_event)

        if grid_coords is None:
            return self.elements[grid_coords]

        # Assign a key
        if el.eltype is 'btn' and not el.key and el.button_text:
            el.key = el.button_text
        if not el.key:
            el.key = grid_coords

        if not self.allow_repeated_keys:
            while el.key in self._by_key:
                if type(el.key) is str:
                    el.key = el.key + '-'
                else:
                    el.key = str(el.key) + '-'

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
            if el.eltype is 'btn':
                raise Exception
            if el.size[0]:
                self.elements[grid_coords].width = el.size[0]
            if el.size[1]:
                self.elements[grid_coords].height = el.size[1]
        except:
            pass

        return self.elements[grid_coords]

    def _general_event(self, instance, value):
        self.trigger_event(instance)

    def trigger_event(self, event):

        # print('event',event)
        # print('key',self.keys[event])
        self.event_counter += 1
        for key in self.by_key:
            if self._by_key[key].eltype in ['input', 'spinner']:
                self.values[key] = self.by_key[key].text
            elif self._by_key[key].eltype in ['switch']:
                self.values[key] = self.by_key[key].active
            elif self._by_key[key].eltype in ['tabgroup']:
                self.values[key] = self.by_key[key].current_tab.text
            elif self._by_key[key].eltype in ['screens']:
                self.values[key] = self.by_key[key].current
            elif self._by_key[key].eltype in ['kvel', 'combo', 'watch']:
                obj, prop = self._by_key[key].value_bind
                if not type(obj) is type:
                    self.values[key] = getattr(obj, prop)
            elif self._by_key[key].eltype in ['tbtn']:
                self.values[key] = True if self.by_key[
                    key].state == 'down' else False

                # exec('self.values[key] = self._by_key[key].value_prop',locals())
        if self.values:
            self._values_old = self.values.copy()
        if self.event_manager:
            # if event is self.event_start_key or type(event) is str:# and
            # event in self.by_key:
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


class Text:

    def __init__(self, text='', key=None, halign='center', valign='middle',
                 background_color=(0, 0, 0, 0), text_color=[1, 1, 1, 1], markup=False,
                 size_hint=(1, 1),
                 size=(None, None),

                 font_name='Roboto',
                 font_size=15,

                 ):
        self.font_name = font_name
        self.font_size = font_size
        self.size = size
        if size[0]:
            size_hint = None, size_hint[1]
        if size[1]:
            size_hint = size_hint[0], None
        self.size_hint = size_hint

        self.text = text
        self.eltype = 'text'
        self.key = key
        self.halign = halign
        self.valign = valign
        self.background_color = background_color
        self.text_color = text_color
        self.markup = markup


class TextMarkup:

    def __init__(self, text='', key=None,
                 size_hint=(1, 1),
                 size=(None, None),
                 ):
        self.size = size
        if size[0]:
            size_hint = None, size_hint[1]
        if size[1]:
            size_hint = size_hint[0], None
        self.size_hint = size_hint

        self.text = text
        self.eltype = 'rst'
        self.key = key


class Button:

    def __init__(self, button_text='', key=None,
                 text_color=[1, 1, 1, 1],
                 background_color=[1, 1, 1, 1],
                 size=(None, None),
                 size_hint=(1, 1),
                 markup=False,
                 disabled=False,
                 enable_events=True,
                 font_name=None,
                 image_normal='atlas://data/images/defaulttheme/button',
                 image_pressed='atlas://data/images/defaulttheme/button_pressed',
                 image_disabled_normal='atlas://data/images/defaulttheme/button_disabled',
                 image_disabled_pressed='atlas://data/images/defaulttheme/button_disabled_pressed',
                 ):
        self.text_color = text_color
        self.background_color = background_color
        self.image_normal = image_normal
        self.image_pressed = image_pressed
        self.image_disabled_normal = image_disabled_normal
        self.image_disabled_pressed = image_disabled_pressed
        self.disabled = disabled
        self.size = size
        if size[0]:
            size_hint = None, size_hint[1]
        if size[1]:
            size_hint = size_hint[0], None
        self.size_hint = size_hint

        self.button_text = button_text
        self.eltype = 'btn'
        self.key = key
        self.markup = markup
        self.font_name = font_name
        self.height = size[1]
        self.width = size[0]
        self.markup = markup
        self.enable_events = enable_events


class ToggleButton(Button):

    def __init__(self, button_text='', pressed=False, group_id=None, key=None,
                 text_color=[1, 1, 1, 1],
                 background_color=[1, 1, 1, 1],
                 size=(None, None),
                 size_hint=(1, 1),
                 markup=False,
                 disabled=False,
                 enable_events=False,
                 font_name=None,
                 image_normal='atlas://data/images/defaulttheme/button',
                 image_pressed='atlas://data/images/defaulttheme/button_pressed',
                 image_disabled_normal='atlas://data/images/defaulttheme/button_disabled',
                 image_disabled_pressed='atlas://data/images/defaulttheme/button_disabled_pressed',
                 ):

        self.pressed = pressed
        self.group_id = group_id
        super(ToggleButton, self).__init__(button_text=button_text, key=key, background_color=background_color,
                                           text_color=text_color,
                                           size_hint=size_hint,
                                           size=size,
                                           markup=markup,
                                           disabled=disabled,
                                           enable_events=enable_events,
                                           font_name=font_name,
                                           image_normal=image_normal,
                                           image_pressed=image_pressed,
                                           image_disabled_normal=image_disabled_normal,
                                           image_disabled_pressed=image_disabled_pressed
                                           )
        self.eltype = 'tbtn'


class Void:

    def __init__(self,
                 size_hint=(1, 1),
                 size=(None, None),
                 ):
        self.size = size
        if size[0]:
            size_hint = None, size_hint[1]
        if size[1]:
            size_hint = size_hint[0], None
        self.size_hint = size_hint
        self.eltype = 'void'
        self.key = None


class In:

    def __init__(self, text='',
                 password=False, key=None, multiline=False, enable_events=False, use_bubble=False,
                 use_handles=False,
                 write_tab=False,
                 size_hint=(1, 1),
                 size=(None, None),
                 disabled=False,
                 hint_text='',
                 halign='left',
                 valign='top',
                 text_color=[0, 0, 0, 1],
                 background_color=[1, 1, 1, 1],
                 cursor_color=[0, 0, 0, 1],
                 selection_color=[0.1843, 0.6549, 0.8313, .5],
                 font_name='Roboto',
                 font_size=15,
                 ):
        self.selection_color = selection_color
        self.text_color = text_color
        self.background_color = background_color
        self.cursor_color = cursor_color
        self.font_name = font_name
        self.font_size = font_size

        self.valign = valign
        self.halign = halign
        self.hint_text = hint_text
        self.disabled = disabled
        self.size = size
        if size[0]:
            size_hint = None, size_hint[1]
        if size[1]:
            size_hint = size_hint[0], None
        self.size_hint = size_hint

        self.text = text
        self.eltype = 'input'
        self.password = password
        self.key = key
        self.multiline = multiline
        self.use_bubble = use_bubble
        self.enable_events = enable_events
        self.use_handles = use_handles
        self.write_tab = write_tab


class Multiline(In):

    def __init__(self, text='',
                 key=None,
                 multiline=True,
                 enable_events=False,
                 use_bubble=False,
                 use_handles=False,
                 password=False,
                 write_tab=True,
                 size_hint=(1, 1),
                 size=(None, None),
                 disabled=False,
                 hint_text='',
                 halign='left',
                 valign='top',
                 text_color=[0, 0, 0, 1],
                 background_color=[1, 1, 1, 1],
                 cursor_color=[0, 0, 0, 1],
                 selection_color=[0.1843, 0.6549, 0.8313, .5],
                 font_name='Roboto',
                 font_size=15,
                 ):
        super(Multiline, self).__init__(
            text=text,
            key=key,
            multiline=multiline,
            enable_events=enable_events,
            use_bubble=use_bubble,
            use_handles=use_handles,
            password=password,
            write_tab=write_tab,
            size_hint=size_hint,
            size=size,
            disabled=disabled,
            hint_text=hint_text,
            halign=halign,
            valign=valign,
            text_color=text_color,
            background_color=background_color,
            cursor_color=cursor_color,
            font_name=font_name,
            font_size=font_size,
        )


# class Spinner:

#     def __init__(self, values=['...','choice0','choice1'], default_value='...', key=None, enable_events=False,
#         size_hint=(1,1),
#         size=(None,None),
#         ):
#         self.size=size
#         if size[0]:
#             size_hint=None,size_hint[1]
#         if size[1]:
#             size_hint=size_hint[0],None
#         self.size_hint=size_hint

#         self.eltype = 'spinner'
#         self.key = key
#         self.default_value = default_value
#         self.values = values
#         self.enable_events = enable_events
class Spinner(Button):

    def __init__(self, values=['...', 'choice0', 'choice1'], default_value='...',
                 key=None,
                 text_color=[1, 1, 1, 1],
                 background_color=[1, 1, 1, 1],
                 size=(None, None),
                 size_hint=(1, 1),
                 markup=False,
                 disabled=False,
                 enable_events=False,
                 font_name=None,
                 image_normal='atlas://data/images/defaulttheme/spinner',
                 image_pressed='atlas://data/images/defaulttheme/spinner_pressed',
                 image_disabled_normal='atlas://data/images/defaulttheme/spinner_disabled',
                 image_disabled_pressed='atlas://data/images/defaulttheme/button_disabled_pressed',
                 ):

        self.default_value = default_value
        self.values = values
        super(Spinner, self).__init__(button_text=default_value, key=key, background_color=background_color,
                                      text_color=text_color,
                                      size_hint=size_hint,
                                      size=size,
                                      markup=markup,
                                      disabled=disabled,
                                      enable_events=enable_events,
                                      font_name=font_name,
                                      image_normal=image_normal,
                                      image_pressed=image_pressed,
                                      image_disabled_normal=image_disabled_normal,
                                      image_disabled_pressed=image_disabled_pressed
                                      )
        self.eltype = 'spinner'


class ProgressBar:

    def __init__(self, value=0, max_value=100, key=None,
                 size_hint=(1, 1),
                 size=(None, None),
                 ):
        self.size = size
        if size[0]:
            size_hint = None, size_hint[1]
        if size[1]:
            size_hint = size_hint[0], None
        self.size_hint = size_hint

        self.eltype = 'pb'
        self.max_value = max_value
        self.value = value
        self.key = key


class VideoPlayer:

    def __init__(self, source='', state='stop', key=None,
                 options={'allow_stretch': True},
                 size_hint=(1, 1),
                 size=(None, None),
                 ):
        self.size = size
        if size[0]:
            size_hint = None, size_hint[1]
        if size[1]:
            size_hint = size_hint[0], None
        self.size_hint = size_hint

        self.eltype = 'vdp'
        self.source = source
        self.state = state
        self.options = options
        self.key = key


class Video:

    def __init__(self, source='', state='stop', key=None,
                 options={'allow_stretch': True},
                 size_hint=(1, 1),
                 size=(None, None),
                 ):
        self.size = size
        if size[0]:
            size_hint = None, size_hint[1]
        if size[1]:
            size_hint = size_hint[0], None
        self.size_hint = size_hint

        self.eltype = 'video'
        self.source = source
        self.state = state
        self.options = options
        self.key = key


class Sublayout:

    def __init__(self, layout=None, key=None,
                 size_hint=(1, 1),
                 size=(None, None),
                 padding=[0, 0, 0, 0],
                 spacing=[0, 0],
                 ):
        self.size = size
        if size[0]:
            size_hint = None, size_hint[1]
        if size[1]:
            size_hint = size_hint[0], None
        self.size_hint = size_hint

        self.layout = layout
        self.eltype = 'subl'
        self.key = key
        self.padding = padding
        self.spacing = spacing


class ScrollSublayout:

    def __init__(self, layout=None, key=None,
                 size_hint=(1, 1),
                 size=(None, None),
                 content_size_hint=(1, 1),
                 content_size=(None, None),
                 padding=[0, 0, 0, 0],
                 spacing=[0, 0],
                 scroll_x=True,
                 scroll_y=True,
                 ):
        self.size = size
        if size[0]:
            size_hint = None, size_hint[1]
        if size[1]:
            size_hint = size_hint[0], None
        self.size_hint = size_hint

        self.content_size = content_size
        if content_size[0]:
            content_size_hint = None, content_size_hint[1]
        if content_size[1]:
            content_size_hint = content_size_hint[0], None
        self.content_size_hint = content_size_hint

        self.layout = layout
        self.eltype = 'ssubl'
        self.key = key
        self.padding = padding
        self.spacing = spacing
        self.scroll_x = scroll_x
        self.scroll_y = scroll_y

# DefaultWindowSize=(800,600)
class Window(_App):

    def __init__(self, title='App Title', layout=None, event_manager=None,
                 size=(800,600),
                 resizable=True,
                 no_titlebar=False,
                 fullscreen=False,
                 allow_repeated_keys=False,
                 padding=[0, 0, 0, 0],
                 exit_on_escape=True,
                 location=(None, None),
                 rotation=[0, 90, 180, 270][0],
                 start_maximized=False,
                 start_minimized=False,
                 show_cursor=True,
                 keep_on_top=False,
                 icon=None,
                 background_color=[0, 0, 0, 0],
                 alpha=1,
                 **kwargs):
        super(Window, self).__init__(**kwargs)

        self.title = title
        # self.set_title(title)
        self.layout = layout
        self.event_manager = event_manager
        self.allow_repeated_keys = allow_repeated_keys
        self.padding = padding
        self.Run = self.run
        self.icon = icon

        # Config.set('graphics', 'borderless', no_titlebar)
        # Config.set('graphics', 'fullscreen', 'fake')
        # Config.write()

        from kivy.config import Config
        if size[0]:
            Config.set('graphics', 'width', size[0])
        if size[1]:
            Config.set('graphics', 'height', size[1])

        if location[0] != None and location[1] != None:
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

        if size[0]:
            kvWindow.size=size[0],kvWindow.size[1]
        if size[1]:
            kvWindow.size=kvWindow.size[0],size[1]
        
        if type(background_color) is str:
            kvWindow.clearcolor = Colors[background_color]
        else:
            kvWindow.clearcolor = background_color

        # keep_on_top
        self.platform = platform.system()
        self._is_windows = True if 'windows' in self.platform.lower() else False

        # from KivyOnTop import register_topmost, unregister_topmost
        # register_topmost(kvWindow, title)
        if keep_on_top:
            if self._is_windows:
                import win32gui
                import win32con
                kvWindow.bind(on_draw=lambda *args: self.set_always_on_top())
            else:
                print('The on_top behavior only works in Windows platforms.')
        if alpha != 1:
            if self._is_windows:
                import win32gui
                import win32con

                kvWindow.bind(on_draw=lambda *args: self.set_alpha(alpha))
            else:
                print('The transparent behavior only works in Windows platforms.')

        self.app = Layout(self.layout, self.event_manager,
                          self.allow_repeated_keys, self.padding)

    def set_alpha(self, alpha):
        alpha = int(alpha * 255)
        import win32api
        # Get the window
        handle = win32gui.FindWindow(None, self.title)

        # Make it a layered window
        win32gui.SetWindowLong(handle, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(
            handle, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)

        # make it transparent (alpha between 0 and 255)
        win32gui.SetLayeredWindowAttributes(
            handle, win32api.RGB(0, 0, 0), alpha, win32con.LWA_ALPHA)

    def set_always_on_top(self):
        '''
        Sets the HWND_TOPMOST flag for the current Kivy Window.
        This behavior will be overwritten by setting position of the window from kivy.
        If you want the window to stay on top of others even after changing the position or size from kivy, 
        use the register_topmost function instead.
        '''
        if not self._is_windows:
            print('The on top behavior only works in Windows platforms.')
            return

        hwnd = win32gui.FindWindow(None, self.title)

        rect = win32gui.GetWindowRect(hwnd)
        x = rect[0]
        y = rect[1]
        w = rect[2] - x
        h = rect[3] - y

        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, x, y, w, h, 0)

    def set_not_always_on_top(self):
        '''
        Sets the HWND_NOTOPMOST flag for the current Kivy Window.
        '''
        if not self._is_windows:
            print('The on_top behavior only works in Windows platforms.')
            return

        hwnd = win32gui.FindWindow(None, self.title)

        rect = win32gui.GetWindowRect(hwnd)
        x = rect[0]
        y = rect[1]
        w = rect[2] - x
        h = rect[3] - y

        win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, x, y, w, h, 0)

    def trigger_event(self, value):
        self.app.trigger_event(value)

    def Close(self):
        self.get_running_app().stop()

    def build(self):
        if self.app.has_appmenu:
            from kivy.uix.floatlayout import FloatLayout
            self.with_menu = FloatLayout()
            self.app.pos = (0, 0)
            self.with_menu.add_widget(self.app)
            self.with_menu.add_widget(self.app.has_appmenu)
            return self.with_menu
        else:
            from kivy.uix.floatlayout import FloatLayout
            self.level_zero = FloatLayout()
            self.app.pos = (0, 0)
            self.level_zero.add_widget(self.app)
            return self.level_zero
        return self.app


class Switch:

    def __init__(self, active=False, key=None,
                 size_hint=(1, 1),
                 enable_events=False,
                 size=(None, None),
                 ):
        self.size = size
        if size[0]:
            size_hint = None, size_hint[1]
        if size[1]:
            size_hint = size_hint[0], None
        self.size_hint = size_hint
        self.enable_events = enable_events
        self.eltype = 'switch'
        self.key = key
        self.active = active


class CheckBox:

    def __init__(self, active=False, key=None, group_id=None,
                 size_hint=(1, 1),
                 enable_events=False,
                 size=(None, None),
                 ):
        self.size = size
        if size[0]:
            size_hint = None, size_hint[1]
        if size[1]:
            size_hint = size_hint[0], None
        self.size_hint = size_hint
        self.enable_events = enable_events
        self.eltype = 'checkbox'
        self.key = key
        self.active = active
        self.group_id = group_id


class TabPanel:

    def __init__(self, tab_items=[],
                 tab_headers=[],
                 tabs_position='top_left',
                 tab_size=(None, None),
                 tab_background_color=[1, 1, 1, 1],
                 tab_text_color=[1, 1, 1, 1],
                 tab_image_normal='atlas://data/images/defaulttheme/tab_btn',
                 key=None,
                 size_hint=(1, 1),
                 enable_events=False,
                 size=(None, None),
                 background_color=[1, 1, 1, 1],
                 background_image='atlas://data/images/defaulttheme/tab',
                 ):
        self.size = size
        if size[0]:
            size_hint = None, size_hint[1]
        if size[1]:
            size_hint = size_hint[0], None
        self.size_hint = size_hint
        self.enable_events = enable_events
        self.eltype = 'tabgroup'
        self.key = key
        self.tab_items = tab_items
        self.tab_headers = tab_headers
        self.tabs_position = tabs_position
        self.tab_background_color = tab_background_color
        self.tab_text_color = tab_text_color
        self.background_image = background_image if background_image else ''
        self.tab_background_normal = tab_image_normal if tab_background_normal else ''
        self.background_color = background_color

        tab_width, tab_height = 100, 40

        if tab_size[0]:
            tab_width = tab_size[0]
        if tab_size[1]:
            tab_height = tab_size[1]

        self.tab_height = tab_height
        self.tab_width = tab_width


class Slider:

    def __init__(self, min_value=0, max_value=100, value=0, key=None,
                 cursor_size=(32, 32),
                 orientation='horizontal',
                 size_hint=(1, 1),
                 size=(None, None),
                 ):
        self.size = size
        if size[0]:
            size_hint = None, size_hint[1]
        if size[1]:
            size_hint = size_hint[0], None
        self.size_hint = size_hint

        self.eltype = 'slider'
        self.max_value = max_value
        self.min_value = min_value
        self.value = value
        self.key = key
        self.cursor_size = cursor_size
        self.orientation = orientation


class MenuBar:

    def __init__(self, menu_def={
        'File': {
            'New': None,
            'Recent': {'file1': None, 'file2': None},
            '---': None,
            'Exit': None},
        'Tools': {},
        'Help': {
            'Support': 'disabled',
            'About': None,
            'Extras': {'extra1': None, 'extra2': None}},
    },
        key=None,
        size_hint=(1, 1),
        size=[None, None],
    ):
        if not size[1]:
            size[1] = 30
        self.size = size
        if size[0]:
            size_hint = None, size_hint[1]
        if size[1]:
            size_hint = size_hint[0], None
        self.size_hint = size_hint
        self.eltype = 'menubar'
        self.key = key
        self.menu_def = menu_def


class ScreenManager:

    def __init__(self, screen_list=[], screen_names=[], transition='Slide',
                 transition_list=['No', 'Slide', 'Card', 'Swap', 'Fade', 'Wipe',
                                  'FallOut', 'RiseIn'],
                 key=None,
                 size_hint=(1, 1),
                 enable_events=False,
                 size=(None, None),
                 ):
        self.size = size
        if size[0]:
            size_hint = None, size_hint[1]
        if size[1]:
            size_hint = size_hint[0], None
        self.size_hint = size_hint
        self.enable_events = enable_events
        self.eltype = 'screens'
        self.key = key
        self.screen_list = screen_list
        self.screen_names = screen_names
        self.transition = transition
        self.transition_list = transition_list


class Box:

    def __init__(self, key=None,
                 size_hint=(1, 1),
                 enable_events=False,
                 size=(None, None),
                 ):
        self.size = size
        if size[0]:
            size_hint = None, size_hint[1]
        if size[1]:
            size_hint = size_hint[0], None
        self.size_hint = size_hint
        self.enable_events = enable_events
        self.eltype = 'box'
        self.key = key


class Image:

    def __init__(self, source='', async_load=False,
                 key=None,
                 size_hint=(1, 1),
                 enable_events=False,
                 size=(None, None),
                 ):
        self.size = size
        if size[0]:
            size_hint = None, size_hint[1]
        if size[1]:
            size_hint = size_hint[0], None
        self.size_hint = size_hint
        self.enable_events = enable_events
        self.eltype = 'img'
        self.key = key
        self.source = source
        self.async_load = async_load


class kvElement:

    def __init__(self, kv_element,
                 value_bind=[object, str],
                 event_bind=[object, str],
                 key=None,
                 size_hint=(1, 1),
                 size=(None, None),
                 ):
        self.size = size
        if size[0]:
            size_hint = None, size_hint[1]
        if size[1]:
            size_hint = size_hint[0], None
        self.size_hint = size_hint

        self.kv_element = kv_element
        self.event_bind = event_bind
        self.value_bind = value_bind
        self.eltype = 'kvel'
        self.key = key


class ComboBox:

    def __init__(self, input_text=In(),
                 main_button=Button('▼', font_name='DejaVuSans',
                                    text_color=[0, 0, 0, 1],
                                    background_color=[.75, .75, .75, 1], size=(32, None),
                                    image_normal=''
                                    ),
                 enable_events=False,
                 size=(None, None),
                 size_hint=(1, 1),
                 key=None,
                 default_value='',
                 values=['', 'choice0', 'choice1'],
                 hint_text='Select:',
                 disabled=False,
                 read_only=False,
                 ):
        self.read_only = read_only
        self.disabled = disabled
        self.size = size
        if size[0]:
            size_hint = None, size_hint[1]
        if size[1]:
            size_hint = size_hint[0], None
        self.size_hint = size_hint
        self.eltype = 'combo'
        self.key = key
        self.enable_events = enable_events
        self.input_text = input_text
        self.input_text.text = default_value
        self.input_text.hint_text = hint_text
        self.main_button = main_button
        self.values = values
        self.value_bind = None


class Watch:

    def __init__(self, widget=Text(),
                 size=(None, None),
                 size_hint=(1, 1),
                 key=None,
                 value_bind='text',
                 event_bind=str,
                 format='12:00 AM',
                 ):
        self.key = key
        self.size = size
        if size[0]:
            size_hint = None, size_hint[1]
        if size[1]:
            size_hint = size_hint[0], None
        self.size_hint = size_hint
        self.eltype = 'watch'
        self.widget = widget
        self.format = format
        self.event_bind = event_bind
        self.value_bind = value_bind

# Element Alternate names
Column = Sublayout
T = Text
B = Button
TB = ToggleButton
InputText = In
Spin = Spinner
PB = ProgressBar
DropDown = DD = Combo = ComboBox
CB = Check = CheckBox
Subl = Sublayout
VDP = VideoPlayer
VD = Video
SSubl = SSublayout = ScrollSublayout
TabGroup = TabPanel
TMarkup = TextMarkup