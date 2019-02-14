n=int(input())
a=n
sum=0
order=len(str(n))
if n<=100000:
	while n!=0:
		r=n%10
		sum=sum+(r**order)
		n=n//10
if a==sum:
	print(a,"is an armstrong number")
else:
	print(a,"is not an armstrong number")
