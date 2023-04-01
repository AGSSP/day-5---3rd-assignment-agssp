appy=int(input("please enter the number: "))

if appy%3==0 and appy%5==0:
   print("fizzbuzz")
elif appy%5==0:
     print("buzz")
elif appy%3==0:
     print("fizz")
elif appy%3!=0 and appy%5!=0:
     print("appy")