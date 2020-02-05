from turtle import *
import time
from bezier import bezier

b = bezier(12, [(0,0),(1,2),(4,8),(3,7),(6,4),(5,1),(9,9),(9,1),(3,5),(6,6),(7,4),(10,10)])
speed(0)
hideturtle()
penup()
setx(b.curve[0][0]*50)
sety(b.curve[1][0]*50)
pendown()
for i in range(1,len(b.curve[0]),4):
    setx(b.curve[0][i]*50)
    sety(b.curve[1][i]*50)
print("done")
done()

#pensize(5)
#time.sleep(1)
#pendown()
#forward(5)
