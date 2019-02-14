n,k=map(int,input().split())
arr=[]
i=1
while i<=n:
	a=i
	i=i+1
	arr.append(a)
print(sum(arr[0:k]))
