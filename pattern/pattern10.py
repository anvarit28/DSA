# D 
# C D 
# B C D
# A B C D

# Function to demonstrate printing pattern
def pypart(n):
	
	num = 65
	for i in range(1, n+1):
		character = chr(num + n - i)
		for j in range(1, i+1):
				
			print (character,end=" ")
			character = chr(num+n-i+1)
			
		print("\r")	

# Driver Code
n = 4
pypart(n)
