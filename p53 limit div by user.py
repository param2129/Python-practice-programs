limit=int(input("Enter Limit =>"))
Divisible=int(input("Enter Number =>"))
for i in range(1,limit+1):
      if i % Divisible == 0:
        print(i)