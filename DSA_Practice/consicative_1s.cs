public class Solution {
    public int FindMaxConsecutiveOnes(int[] nums) {
        int count=0;
        for(int i=0; i<nums.Length;i++)
        {
            if(nums[i]== 1)
            {
                count += 1;
                
            }
            else
            {
                count = 0;
            }
        }
        return count;
        
    }

}
public class Main
{
    public static void Main (string[] args)
    {
        int[] nums =[1,1,0,1,1,1];
        Solution sol= new Solution();
        sol.FindMaxConsecutiveOnes(nums);
    }
}
