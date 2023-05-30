# A 
# B B 
# C C C 
# D D D D 

# Function to demonstrate printing pattern
def pypart(n):
	
	num = 64
	for i in range(1, n+1):
		character = chr(num + i)
		for j in range(1, i+1):
			
			print (character,end=" ")
			
		print("\r")	

# Driver Code
n = 4
pypart(n)
