/*Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
*/ 

class shuffleArray{

    public static void main(String []args){
        int input[] = {2,5,1,3,4,7};
        int n = 3;
        int a[] = shuffle(input,3);

        for(int i=0;i<(2*n);i++){
            System.out.print(a[i] + " ");
        }

    }
    public static int[] shuffle(int[] nums, int n){
       int l = nums.length;
       int nums1[] = new int[2*n];
       for(int i=0;i<2*n;i++){
        if(i%2==0)
            nums1[i]=nums[i/2];
        
       else 
            nums1[i]=nums[n+(i/2)];
       }
        return nums1;
    }
}