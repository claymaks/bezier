import matplotlib.pyplot as plt

from bezier import Curve

# line
c = Curve((0,0), (1,1))
plt.plot(*zip(*c.curve))
plt.scatter(*zip(*c.points))
plt.savefig("line_0-0-1-1.png")
plt.show()

c = Curve((0,0), (0,1), (1,1))
plt.plot(*zip(*c.curve))
plt.scatter(*zip(*c.points))
plt.savefig("curve_0-0-0-1-1-1.png")
plt.show()

# integral
c = Curve((0.4,0), (0.5,0), (0.5,1), (0.6,1))
plt.plot(*zip(*c.curve))
plt.scatter(*zip(*c.points))
plt.xlim([0, 1])
plt.savefig("curve_0_4-0-0_5-0-0_5-1-0_6-1.png")
plt.show()

# loop
c = Curve((0,0), (1,0.5), (0,1), (0.5,0))
plt.plot(*zip(*c.curve))
plt.scatter(*zip(*c.points))
plt.savefig("curve_0-0-1-0_5-0-1-0_5-0.png")
plt.show()

# edge
c = Curve((0,0), (1,1), (0,1), (1,0), auto_generate=False)
print(c.curve)
c.generate()
plt.plot(*zip(*c.curve))
plt.scatter(*zip(*c.points))
plt.savefig("curve_0-0-1-1-0-1-1-0.png")
plt.show()
