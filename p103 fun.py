def table():
    n=int(input("Enter your Number =>"))
    for i in range(1, 11):
        print(n,"x",i,"=",n*i)


def areaoftriangle():
    h = float(input("h =>"))
    b = float(input("b =>"))
    print("Area of Tringle= ", h * b * 0.5)


def areaofcircle():
    r = float(input("r =>"))
    print("Area of circle= ", 3.14 * r * r)


def max3():
   a=int(input("Enter no1 =>"))
   b=int(input("Enter no2 =>"))
   c=int(input("Enter no3 =>"))
   if a>b or a>c:
       print("no1 is greater")
   elif b>a or b>c:
       print("no2 is greater")
   elif c>a or c>b:
       print("no3 is greater")


def oddeven():
    Number = int(input("Enter no =>"))

    if Number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")


def cube():
    no1 = int(input("Enter number =>"))

    print("Cube  =", no1 * no1 * no1)



table()
areaoftriangle()
areaofcircle()
max3()
oddeven()
cube()