/*Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
*/ 

class maxSubArray{

    public static void main(String []args){
        int input[] = {-2,1,-3,4,-1,2,1,-5,4};
        int sum = maxsubArray(input);
        System.out.println(sum);

    }
    public static int maxsubArray(int[] nums){
        int max_sofar = Integer.MIN_VALUE;
        int max_here = 0;

        for(int i : nums){
            max_here = max_here + i;
            if(max_sofar < max_here)
                max_sofar = max_here;
            if(max_here < 0)
                max_here = 0;
        }
        return max_sofar;
    }
}