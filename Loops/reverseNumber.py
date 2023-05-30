
import sys
class Solution:
    def reverse(x: int) -> int:
        reverse = 0
        while(x != 0):
            n = (x % 10)
            # if ((n > sys.maxsize/10) or (n < -sys.maxsize-1/10)):
            #    return 0
            reverse = reverse*10 + n
            x //= 10
        return reverse

# Driver Code
    n = 40506
    print(reverse(n))
               