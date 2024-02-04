def triangle_type(side1, side2, side3):
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        if side1 == side2 == side3:
            return "Equilateral Triangle"
        elif side1 == side2 or side1 == side3 or side2 == side3:
            return "Isosceles Triangle"
        else:
            return "Scalene Triangle"
    else:
        return "Not a Triangle"
    
side1 = float(input("Enter the length of a side 1 : "))
side2 = float(input("Enter the length of a side 2 : "))
side3 = float(input("Enter the length of a side 3 : "))

result = triangle_type(side1, side2, side3)
print(result)