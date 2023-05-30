# 1 
# 2 3 
# 3 4 5 
# 4 5 6 7


# Function to demonstrate printing pattern
def pypart(n):
	
	#for i in reversed(range(1, n+1)):
	for i in range(1, n+1):
		# c=i
		for j in range(1, i+1):
			
			print (i+j-1,end=" ")
			# c = c+1
		print("\r")	

# Driver Code
n = 4
pypart(n)
