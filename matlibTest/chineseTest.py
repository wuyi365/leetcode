# -*- coding: utf-8 -*-

from numpy import *
import matplotlib.pyplot as plt
from matplotlib import font_manager

# 如果要保存为pdf格式，需要增加如下配置
#from matplotlib import rcParams
#rcParams["pdf.fonttype"] = 42

chf = font_manager.FontProperties(fname='chinese.stzhongs.ttf')
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

plot1, = plt.plot(a,b)
plot2, = plt.plot(a,c)

plt.title(u'中文测试图样', fontproperties=chf)
plt.legend([plot1,plot2],[u"测试第一", u"测试第二"], prop=chf)
plt.show()

#plt.plot(arange(0, 10, 1), arange(0, 10, 1))

#plt.legend((u'图例',), 'lower right', prop=chf)
#plt.savefig('test.png', format='png')    # 或者pdf