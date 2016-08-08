# -*- coding: utf-8 -*-

"""
Demo of a basic pie chart plus a few additional features.

In addition to the basic pie chart, this demo shows a few optional features:

    * slice labels
    * auto-labeling the percentage
    * offsetting a slice with "explode"
    * drop-shadow
    * custom start angle

Note about the custom start angle:

The default ``startangle`` is 0, which would start the "Frogs" slice on the
positive x-axis. This example sets ``startangle = 90`` such that everything is
rotated counter-clockwise by 90 degrees, and the frog slice starts on the
positive y-axis.
"""
import matplotlib.pyplot as plt

from pylab import *  
from matplotlib import font_manager
# mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体  
  
# mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题 

#chf = font_manager.FontProperties(fname='chinese.stzhongs.ttf')

prop = font_manager.FontProperties(fname='chinese.stzhongs.ttf')
print(prop.get_name())
mpl.rcParams['font.family'] = prop.get_name()


# The slices will be ordered and plotted counter-clockwise.
plt.title(u'显示中文')
labels = u'签约', u'中午', '大树', '小草'
sizes = [15, 30, 45, 10]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
explode = (0, 0, 0.05, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')


# Set aspect ratio to be equal so that pie is drawn as a circle.

#
patches, texts, autotexts = plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=90)
#plt.legend(patches, labels, loc="best", prop=chf)
print(texts)
matplotlib.rcParams.update({'font.size': 21})
#texts[:].set_fontsize(20)
#plt.setp(autotexts, fontproperties=chf)
#plt.setp(texts, fontproperties=chf)
#plt.legend(prop={'family':'SimHei','size':25}) 
#plt.legend(prop=chf) 
plt.text(1.2, 0.99, r'鲜花')

plt.axis('equal')

fig = plt.figure()
ax = fig.gca()
import numpy as np

ax.pie(np.random.random(4), explode=explode, labels=labels, colors=colors,
       autopct='%1.1f%%', shadow=True, startangle=90,
       radius=0.25, center=(0, 0), frame=True)
ax.pie(np.random.random(4), explode=explode, labels=labels, colors=colors,
       autopct='%1.1f%%', shadow=True, startangle=90,
       radius=0.25, center=(1, 1), frame=True)
ax.pie(np.random.random(4), explode=explode, labels=labels, colors=colors,
       autopct='%1.1f%%', shadow=True, startangle=90,
       radius=0.25, center=(0, 1), frame=True)
ax.pie(np.random.random(4), explode=explode, labels=labels, colors=colors,
       autopct='%1.1f%%', shadow=True, startangle=90,
       radius=0.25, center=(1, 0), frame=True)

ax.set_xticks([0, 1])
ax.set_yticks([0, 1])
ax.set_xticklabels(["Sunny", "Cloudy"])
ax.set_yticklabels(["Dry", "Rainy"])
ax.set_xlim((-0.5, 1.5))
ax.set_ylim((-0.5, 1.5))

# Set aspect ratio to be equal so that pie is drawn as a circle.
ax.set_aspect('equal')

plt.show()
