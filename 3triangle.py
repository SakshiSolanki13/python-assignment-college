def calculate_triangle_area(a, b, c):
    
    s = (a + b + c) / 2
    
    
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    
    return area


side_a = float(input("Enter the length of side a: "))
side_b = float(input("Enter the length of side b: "))
side_c = float(input("Enter the length of side c: "))

triangle_area = calculate_triangle_area(side_a, side_b, side_c)

print(f"The area of the triangle with sides {side_a}, {side_b}, {side_c} is {triangle_area}")
