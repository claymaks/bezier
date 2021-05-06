"""De Casteljau's algorithm."""

class Curve(object):
    """Generate bezier curves with variable control points.

        Attributes:
            points ( list(tuples(int, int)) ): List of control points
            curve ( list(tuples(int, int)) ): List of points along path

        """
    
    def __init__(self, *args: (()), auto_generate=True):
        """Create Curve object and generate path given control points.

        Args:
            *args ( tuple(int, int) ): List of tuples representing control points
            auto_generate ( bool ): Indicates whether curve should be generated on initialization

        """
        self.points = list(args)
        self.curve = []
        if auto_generate:
            self.generate()

    def generate(self, path_resolution=1000):
        """Generate path using control points at a user defined granularity.

        Args:
            path_resolution ( int ): Number of points used to create curve

        """
        self.curve = []
        
        C = len(self.points) - 1
        for i in range(path_resolution):
            t = i/path_resolution
            self.curve.append([0,0])
            for k,p in enumerate(self.points):
                self.curve[-1][0] += ((1-t)**(C-k)) * (t**(k)) * p[0] * (C if k not in [0, C] else 1)
                self.curve[-1][1] += ((1-t)**(C-k)) * (t**(k)) * p[1] * (C if k not in [0, C] else 1)

