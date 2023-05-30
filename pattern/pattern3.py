# Function to demonstrate printing pattern
def pypart(n):
	c=1
	#for i in reversed(range(1, n+1)):
	for i in range(1, n+1):
		
		for j in range(1, n+1):
			print (c,end=" ")
			c=c+1
		print("\r")	

# Driver Code
n = 4
pypart(n)
