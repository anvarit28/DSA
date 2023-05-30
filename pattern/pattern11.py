#    *
#   **
#  ***
# ****

# Function to demonstrate printing pattern
def pypart(n):
	
	for i in range(1, n+1):
		space = n-i
		for k in range(1, space+1):
			print (" ", end=" ")
			space = space - 1
		for j in range(1, i+1):
			print ("*",end=" ")	
		print("\r")	

# Driver Code
n = 4
pypart(n)
