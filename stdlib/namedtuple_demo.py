#%% named tuple是不可变的，轻量级的对象
from collections import namedtuple
import math

Point = namedtuple('Point','x y')
pt1 = Point(1.0, 2.0)
pt2 = Point(2.0, 3.5)

length = math.sqrt((pt2.x - pt1.x) ** 2 + (pt2.y - pt1.y) ** 2)
print(length)

#%%
'''
Furthermore, you can also replace ordinary immutable classes that have no functions, only fields with them. You can even use your named tuple types as base classes:

class Point(namedtuple('Point', 'x y')):
    [...]
'''