class Rectangle:
    width = None
    height = None
    photo = ""

    #INIT Function
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def __str__(self):
        return "Rectangle(width="+str(self.width)+", height="+str(self.height)+")"
    

    def set_width(self,width):
        self.width = width
    
    
    def set_height(self,height):
        self.height = height
    

    def get_area(self):
        return (self.width*self.height)


    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)
    

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        c = 0
        photo = ""
        while c < self.height:
            photo += (self.width * "*") + "\n"
            c += 1
        return (photo)
    

    def get_amount_inside(self, ob):
        print (self.get_area())
        print (ob.get_area())
        return self.get_area() // ob.get_area()

class Square(Rectangle):

    def __init__(self, length):
        self.width = length
        self.height = length

    def __str__(self):
        return "Square(side="+str(self.width)+")"
    
    def set_side(self,length):
        self.width = length
        self.height = length
        


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

