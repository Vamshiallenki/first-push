def check_triangle_type(a, b, c):
   
    if a + b > c and a + c > b and b + c > a:
        print("It is a Valid triangle ")

      
        if a == b == c:
            print("The triangle is Equilateral")
      
        elif a == b or b == c or a == c:
            print("It is an Isosceles")
        
        elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
            print("It is a Right-angled Triangle")
        else:
            print("It is a Scalene")
    else:
        print("Not a valid triangle")


s1 = float(input("Enter side 1: "))
s2 = float(input("Enter side 2: "))
s3 = float(input("Enter side 3: "))

check_triangle_type(s1,s2,s3)




  

