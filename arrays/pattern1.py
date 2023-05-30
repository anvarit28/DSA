# print("Enter a number")

# def pattern(n):
    
#     i=1
#     #outer loop for rows
#     while(i<n):
#         # inner loop to handle number of columns
#         # values changing acc. to outer loop
#         j=1
#         while(j<i):
         
#             # printing stars
#             print("* ",end="")
      
#         # ending line after each row
#         print("\r")

# n=5
# pattern(n)
# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern
def pypart(n):
	
	# outer loop to handle number of rows
	# n in this case
	for i in range(1, n+1):
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(1, n+1):
		
			# printing stars
			print(j ,end="")
	
		# ending line after each row
		print("\r")

# Driver Code
n = 4
pypart(n)
