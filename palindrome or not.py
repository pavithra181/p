n=int(input())
a=n
pal=0
while n!=0:
	r=n%10
	n=n//10
	pal=(pal*10)+r
if a==pal:
	print("pal")
else:
	print("not")
