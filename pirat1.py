from math import sqrt
from copy import copy

class Point:
	def __init__(self, x, y, m, id):
		self.x = x
		self.y = y
		self.id = id
		self.m = m

def dist(p1, p2):
	return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

n, p, k, M = map(int, input().split())

points = []

x, y, m = map(int, input().split())
f = Point(x, y, m, 1)

for i in range(2, n+1):
	x, y, m = map(int, input().split())
	points += [Point(x, y, m, i)]

c = copy(f)
print(1, end=' ')

h = [m]

while points:
	points.sort(key=lambda x: x.m - p*dist(c, x), reverse=True)
	for i in points:
		if sum(h[-k:])+i.m <= M:
			h += [i.m]
			n = i
			break
	else:
		print(1)
		break
	n = points[0]
	if n.m - p*dist(c, n) > 0:
		print(n.id, end = ' ')
		points.remove(n)
		c = copy(n)
	else:
		print(1)
		break
else:
	print(1)