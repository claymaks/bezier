def unzip(tuple_obj):
    x = []
    y = []
    for i in tuple_obj:
        x.append(i[0])
        y.append(i[1])
    return [x,y]

class bezier(object):
    def __init__(self, order, pts):
        self.order = order
        self.pts = pts
        self.curve = []
        self.generate()

    def generate(self):
        xl = []
        yl = []
        p = self.order
        for tb in range(0,1000):
            t = tb/1000
            x = (((1-t)**(p-1)) * self.pts[0][0])
            y = (((1-t)**(p-1)) * self.pts[0][1])
            for i in range(1, p-1):
                
                x += (p-1) * (((1-t)**((p-1)-i)) * (t**i) * self.pts[i][0])
                y += (p-1) * (((1-t)**((p-1)-i)) * (t**i) * self.pts[i][1])
            x += (t**(p-1)) * self.pts[p-1][0]
            y += (t**(p-1)) * self.pts[p-1][1]
            xl.append(x)
            yl.append(y)
        self.curve = [xl,yl]

class bezier_smooth(object):
    #development
    def __init__(self, order, pts):
        self.order = order
        self.pts = pts
        self.curve = []
        self.generate()

    def generate(self):
        xl = []
        yl = []
        p = self.order
        for tb in range(0,1000):
            t = tb/1000
            x = (((1-t)**(p-1)) * self.pts[0][0])
            y = (((1-t)**(p-1)) * self.pts[0][1])
            for i in range(1, p-1):
                
                x += (p-1) * (((1-t)**((p-1)-i)) * (t**i) * self.pts[i][0]) * ((((p-i)/p)*self.pts[0][0])) + ((i/p)*self.pts[-1][0])
                y += (p-1) * (((1-t)**((p-1)-i)) * (t**i) * self.pts[i][1]) * ((((p-i)/p)*self.pts[0][1])) + ((i/p)*self.pts[-1][1])
            x += (t**(p-1)) * self.pts[p-1][0]
            y += (t**(p-1)) * self.pts[p-1][1]
            xl.append(x)
            yl.append(y)
        self.curve = [xl,yl]

if __name__ == "__main__":
    import matplotlib
    import matplotlib.pyplot as plt

    b = bezier(12, [(0,0),(1,2),(4,8),(3,7),(6,4),(5,1),(9,9),(9,1),(3,5),(6,6),(7,4),(10,10)])
    plt.plot(b.curve[0], b.curve[1])
    plt.scatter(unzip(b.pts)[0], unzip(b.pts)[1])
    plt.show()


    
    b = bezier(4, [(0,0),(1.66,0),(3.33,5),(5,5)])
    plt.plot(b.curve[0], b.curve[1])
    plt.scatter(unzip(b.pts)[0], unzip(b.pts)[1])
    plt.show()


                                                                                

    b = bezier(5, [(0,0),(3,3),(2,4),(0,3),(1,2)])
    plt.plot(b.curve[0], b.curve[1])
    plt.scatter(unzip(b.pts)[0], unzip(b.pts)[1])
    plt.show()


    b = bezier(6, [(0,0),(1,6),(2,3),(3,5),(4,4), (3, 3)])
    plt.plot(b.curve[0], b.curve[1])
    plt.scatter(unzip(b.pts)[0], unzip(b.pts)[1])
    plt.show()

    b = bezier(5, [(6,0),(0,3),(3,5),(6,3),(0,0)])
    plt.plot(b.curve[0], b.curve[1])
    plt.scatter(unzip(b.pts)[0], unzip(b.pts)[1])
    plt.show()



