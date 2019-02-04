x=int(input())
if x%4==0 and x%100!=0:
 if x%400==0:
  print("leap")
else:
 print("not")
