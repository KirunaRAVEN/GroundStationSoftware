import matplotlib.pyplot as plt
import matplotlib.patches as ptc
from matplotlib.text import Text

class indicatorLight:
    def __init__(self, title, state=0, fontSize=20):
        self.title     = title.replace(' ', '\n')
        self.state     = state
        self.fontSize  = fontSize
        self.color     = [['dimgray', 'gray'], ['orangered', 'lightcoral']]
        self.label     = Text(0.5, 0.48, self.title, horizontalalignment='center', verticalalignment='center', fontsize=self.fontSize)
        self.outline   = plt.Circle((0.5, 0.5), 0.49, color='black')
        self.outer     = plt.Circle((0.5, 0.5), 0.48, color=self.color[state][0])
        self.highlight = plt.Circle((0.5, 0.5), 0.44, color=self.color[state][1])
        self.inner     = plt.Circle((0.5, 0.5), 0.40, color=self.color[state][0])
        self.objects   = [self.outline, self.outer, self.highlight, self.inner, self.label]


    def setState(self, state):
        self.state = state
        self.outer.set_color(self.color[state][0])
        self.highlight.set_color(self.color[state][1])
        self.inner.set_color(self.color[state][0])

# rename this value display
class valueBox:
    def __init__(self, title, unit, titleFontSize=12, value=0, valueFontSize=24):
        self.titleFontSize  = titleFontSize
        self.valueFontSize = valueFontSize
        self.title   = title
        self.unit    = unit
        self.value   = value
        self.display = Text(1.25, 0.5, self.value, horizontalalignment='center', verticalalignment='center', fontsize=self.valueFontSize, weight='bold')
        self.outline = plt.Rectangle((0, 0), 2.5, 1.0, color='black')
        self.inner = plt.Rectangle((0.05, 0.025), 2.4, 0.95, color='white')
        self.objects = [self.outline, self.inner, self.display] 

    def setValue(self, value):
        self.value = value
        self.display.set_text('%.1f %s' %(self.value, self.unit))

class textBox:
    def __init__(self, title, titleFontSize=12, text='TEXT', textFontSize=12):
        self.titleFontSize  = titleFontSize
        self.textFontSize = textFontSize
        self.title = title
        self.text = text
        self.display = Text(1.75, 0.5, self.text, horizontalalignment='center', verticalalignment='center', fontsize=self.textFontSize, weight='bold')
        self.outline = plt.Rectangle((0, 0), 3.5, 1.0, color='black')
        self.inner = plt.Rectangle((0.025, 0.025), 3.45, 0.95, color='white')
        self.objects = [self.outline, self.inner, self.display]
    
    def setText(self, text):
        self.text = text
        self.display.set_text(self.text)

class logBox:
    def __init__(self):
        self.maxLines = 16
        self.log = [''] * self.maxLines 
        self.display = Text(0.025, 3.375, '', wrap=False, horizontalalignment='left', verticalalignment='top', fontsize=9)
        self.outline = plt.Rectangle((0, 0), 4.8, 3.4, color='black')
        self.inner  = plt.Rectangle((0.025, 0.025), 4.75, 3.35, color='white')
        self.objects = [self.outline, self.inner, self.display]
    
    def updateLog(self, msg):
        self.log.append(msg)
        self.log.pop(0)
        self.display.set_text('\n'.join('{:s}'.format(_msg) for _msg in self.log))
