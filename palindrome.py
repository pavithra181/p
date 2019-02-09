n=int(input())
while n!=0:
	if n<=1000:
		t=n%10
		n=int(n/10)
		print(t,end="")
