# coding:gbk
from copy import deepcopy
d = {}
d['names'] = ['Tom','Jack']
c = d.copy()
dc = deepcopy(d)
d['names'].append ('海伦')
print c
print dc


















