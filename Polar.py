# Application to find the polar coordinates when given an x and a y
import sys
import math

x = float(sys.argv[1])
y = float(sys.argv[2])

r = math.sqrt((x**2)+(y**2))
theta = math.atan2(y,x)

print(r, " ", theta)
