num = int(input("Enter a number: "))
if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print("Non Prime Number")
           break
   else:
       print("Prime Number")
else:
   print("Non Prime Number")