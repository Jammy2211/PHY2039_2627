# Hand-in 4 solution 

```python
class Cuboid:
    """
    Create a cuboid object c = Cuboid(x,y,z)
    returns a cuboid with side lengths x,y,z
    """
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def volume(self):
        """
        Return the volume of the cuboid
        """
        return self.x * self.y * self.z

    def surface_area(self):
        """
        return the surface area of the cuboid
        """
        return 2 * (self.x * self.y + self.y * self.z + self.x * self.y)

    def is_square_cuboid(self):
        """
        returns true if the cuboid is a "square
        cuboid" (two sides are the same length)
        """
        return (self.x == self.y or self.y == self.z or self.z == self.x)
   
    def is_cube(self):  
        """
        returns true if the cuboid is a cube
        """
        return (self.x == self.y == self.z)

    def scale(self, s):
        """
        Scales the cube sides
        """
        self.x *= s
        self.y *= s
        self.z *= s
```