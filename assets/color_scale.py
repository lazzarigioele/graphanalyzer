# This is the code to generate the ./assets/color_scale.png. 

from bokeh.io import show
from bokeh.plotting import figure
from bokeh.io import curdoc


curdoc().theme = 'dark_minimal'


# generate data
max_weight = 300.0
x = list(range(1, 300, 10))
top = [i/300.0 for i in x]
alpha = [0.3 if (i / 300) < 0.3 else 1.0 for i in x ]
color = []
width = []
for i in x: # (nodeA, nodeB, weight)
    width.append(i / max_weight *3)
    factor = int(round(i /max_weight * (255*2)))
    if (factor <= 255): color.append("#%02x%02x%02x" % (factor, 255, 255-factor))
    else: color.append("#%02x%02x%02x" % (255, 255-(factor-255), 0))


# create plot
p = figure(width=500, height=250)
# create circle renderer with color mapper
p.circle(x, top, width=10, color=color, alpha=alpha)
p.circle(x, top, width=2, color=color)

show(p)

