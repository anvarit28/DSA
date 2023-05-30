/*Given an array nums of size n . Complete a function isPalindrome which returns true if array is palindrome else return false
Palindrome is a sequence which reads the same forwards and backwards

Example 1:

Input : nums=[1,2,3,3,2,1]
Output : true
Explanation : The given array nums reads same from forward and backward
*/ 

class palindromeArray{

    public static void main(String []args){
        int input[] = {1,2,3,0,3,2,1};
        boolean flag = isPalindrome(input);
        System.out.println(flag);

    }
    public static Boolean isPalindrome(int[] nums){
        int start = 0, end = nums.length-1;
        while(start<end){
            if(nums[start] != nums[end])
                return false;
            start++;
            end--;    

        }
       
        return true;
    }
}