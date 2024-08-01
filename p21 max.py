Value1=int(input("Enter your First value =>"))
Value2=int(input("Enter your Second value =>"))
Value3=int(input("Enter your Third value =>"))

if Value1>Value2 and Value1>Value3:
    print("First value is greater")
elif Value2>Value3 and Value2>Value1:
    print("Second value is greater")
elif Value3>Value2 and Value3>Value1:
    print("Third value is greater")
else:
    print("Value is equal")