def CalculateAreaOfASquare(side):
    return side*side

def CalculateAreaOfARectangle(length, breadth):
    return length*breadth

def CalculateAreaOfATriangle(height, base):
    return (height*base)/2

print("Welcome! This program calculates area of different shapes")
choice = input("1 for triangle, 2 for rectangle, 3 for square: ")
while(choice != 'q'):
    if(choice == '1'):
        height = input("Enter height of the triangle: ")
        base = input("Enter base of the triangle: ")
        height = int(height)
        base = int(base)
        AreaOfTriangle = CalculateAreaOfATriangle(height, base)
        print(AreaOfTriangle)
    if(choice == '2'):
        length = input("Enter length of the rectangle: ")
        breadth = input("Enter breadth of rectangle: ")
        length = int(length)
        breadth = int(breadth)
        AreaOfRectangle = CalculateAreaOfARectangle(length, breadth)
        print(AreaOfRectangle)
    if(choice == '3'):
        side = input("Enter side of the square: ")
        side = int(side)
        Area = CalculateAreaOfASquare(side)
        print(Area)
    choice = input("1 for triangle, 2 for rectangle, 3 for square. press q to quit: ")