import os, sys
import pickle
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.glyphs import ImageURL
from collections import Counter

in_file = "table.tsv"
lines = open(in_file).read().split("\n")
labels = []
cord = []
for l in lines:
	try:
		t = l.split("\t")
		labels.append(t[1])
		x = float(t[2]) * 20
		y = float(t[3]) * 20
		cord.append([x,y])
	except:
		pass

#How Gender and Skin Tone Modifiers Affect Emoji Semantics in Twitter
output_file("emoji-modifier.html", title="*sem 2018 - Emoji Modifiers", mode="cdn")
#TOOLS="save,resize,crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select"
TOOLS="save,crosshair,pan,wheel_zoom,reset"
plot = figure(tools=TOOLS, x_range=(-12,12), y_range=(-12,12))
#plot.toolbar.active_scroll = plot.select_one("wheel_zoom") 

#images
width = 0.55
height = 0.55
circledim = 0.45

#pre stuff (lines + target)

plot.line([-100,100], [0,0],line_color="grey", line_width=0.5)
plot.line([0,0], [-100,100],line_color="grey", line_width=0.5)

mul = 2
a, b = 10, 8 
source = ColumnDataSource(dict(url = ["./emo/male-sign.png"]*1))
image1 = ImageURL(url="url", x=-a, y=0, w=width*mul, h=height*mul, anchor="center", dilate=False)
plot.add_glyph(source, image1)

source = ColumnDataSource(dict(url = ["./emo/female-sign.png"]*1))
image1 = ImageURL(url="url", x=a, y=0, w=width*mul, h=height*mul, anchor="center", dilate=False)
plot.add_glyph(source, image1)

source = ColumnDataSource(dict(url = ["./emo/skin-0.png"]*1))
image1 = ImageURL(url="url", x=0, y=b, w=width*mul, h=height*mul, anchor="center", dilate=False)
plot.add_glyph(source, image1)

source = ColumnDataSource(dict(url = ["./emo/skin-4.png"]*1))
image1 = ImageURL(url="url", x=0, y=-b, w=width*mul, h=height*mul, anchor="center", dilate=False)
plot.add_glyph(source, image1)

#add emojis
for i in range(len(cord)):
	l=labels[i]
	xp = cord[i][0]
	yp = cord[i][1]		
	emoPath = './emo/'+ l
	if os.path.exists(emoPath):
		#plot.circle(x=xp, y=yp, radius=circledim, line_width=0,fill_alpha=0.45, color=col[clusters[i]], legend="Cluster "+str(clusters[n]+1))
		url = emoPath #'./emo/'+ l +'.png'
		source = ColumnDataSource(dict(url = [url]*1))
		image1 = ImageURL(url="url", x=xp, y=yp, w=width, h=height, anchor="center", dilate=False)
		plot.add_glyph(source, image1)
	else:
		mtext(plot, [xp], [yp], l, col[0])


show(plot)